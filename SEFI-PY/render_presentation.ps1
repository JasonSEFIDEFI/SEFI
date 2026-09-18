param(
    [switch]$Preview,
    [switch]$ReuseClips,
    [string]$SceneFile,
    [string]$Scene
)

$ErrorActionPreference = "Stop"
$outputDirectory = "animations/presentation"
$clipDirectory = Join-Path $outputDirectory "clips"
$finalVideo = Join-Path $outputDirectory "SEFI-boardroom.mp4"
$concatFile = Join-Path $outputDirectory "boardroom.concat.txt"

$scenes = @(
    @{ File = "core/animations/intro_card.py"; Scene = "SEFIUnifiedIntro" },
    @{ File = "core/animations/sefi_ontology.py"; Scene = "SEFIOntologyJourney" },
    @{ File = "core/animations/gwfm_intro.py"; Scene = "GWFMIntro" },
    @{ File = "core/animations/sefi_core.py"; Scene = "SEFICore" },
    @{ File = "core/animations/sefi_sovereignty.py"; Scene = "SEFISovereigntyMorph" },
    @{ File = "core/animations/transition_warp.py"; Scene = "WarpExpressionBridge" },
    @{ File = "core/animations/sefi_photonics.py"; Scene = "SEFIPhotonics" },
    @{ File = "core/animations/defi_flow.py"; Scene = "DEFILayerFlow" },
    @{ File = "core/animations/outro_card.py"; Scene = "SEFIUnifiedOutro" }
)

if ($SceneFile -and $Scene) {
    $scenes = @(@{ File = $SceneFile; Scene = $Scene })
}

New-Item -ItemType Directory -Force -Path $clipDirectory | Out-Null
$qualityArguments = if ($Preview) {
    @("--resolution", "960,540", "--frame_rate", "15")
} else {
    @("--resolution", "1920,1080", "--frame_rate", "30")
}

$clipPaths = @()
foreach ($entry in $scenes) {
    $clipPath = Join-Path $clipDirectory "$($entry.Scene).mp4"
    if ($ReuseClips -and (Test-Path $clipPath)) {
        Write-Host "Reusing $($entry.Scene)..."
        $clipPaths += $clipPath
        continue
    }
    Write-Host "Rendering $($entry.Scene)..."
    $manimArguments = @(
        "-m", "manim", "render", $entry.File, $entry.Scene,
        "--format", "mp4", "--media_dir", $outputDirectory,
        "--disable_caching", "--output_file", $entry.Scene
    ) + $qualityArguments

    $env:PYTHONDONTWRITEBYTECODE = "1"
    & python @manimArguments
    if ($LASTEXITCODE -ne 0) {
        throw "Manim failed while rendering $($entry.Scene)."
    }
    $renderedClip = Get-ChildItem -Path (Join-Path $outputDirectory "videos") -Recurse -Filter "$($entry.Scene).mp4" |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
    if (-not $renderedClip) {
        throw "Manim completed but did not produce a clip for $($entry.Scene)."
    }
    Copy-Item -Path $renderedClip.FullName -Destination $clipPath -Force
    $clipPaths += $clipPath
}

if ($scenes.Count -gt 1) {
    $concatLines = $clipPaths | ForEach-Object {
        "file '$((Resolve-Path $_).Path)'"
    }
    Set-Content -Path $concatFile -Value $concatLines -Encoding ascii

    Write-Host "Assembling $finalVideo..."
    $ffmpegArguments = @(
        "-y", "-f", "concat", "-safe", "0", "-i", $concatFile,
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", $finalVideo
    )
    & ffmpeg @ffmpegArguments
    if ($LASTEXITCODE -ne 0) {
        throw "FFmpeg failed while assembling the presentation."
    }
    Write-Host "Boardroom presentation written to $finalVideo."
} else {
    Write-Host "Scene render written to $($clipPaths[0])."
}