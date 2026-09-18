// Shared globals for 2D + 3D
let scene;
let camera;
let renderer;

let worldline3D;
let originLayer3D;
let authLayer3D;
let warpLayer3D;

let warpVolume;
let sovereigntyShell;

// 2D canvas
const canvas = document.getElementById("fieldCanvas");
const ctx = canvas.getContext("2d");
function drawLayers() {
  if (!showLayers.checked) return;

  // Origin
  ctx.strokeStyle = originColor.value;
  ctx.lineWidth = 1;
  ctx.beginPath();
  for (let t = 0; t < 2000; t++) {
    const o = Number(originStability.value);
    const p = {
      x: t * 0.4,
      y: canvas.height / 2 + o * Math.sin((t + t0) * 0.01)
    };
    if (t === 0) ctx.moveTo(p.x, p.y);
    else ctx.lineTo(p.x, p.y);
  }
  ctx.stroke();

  // Authorship
  ctx.strokeStyle = authColor.value;
  ctx.lineWidth = 1;
  ctx.beginPath();
  for (let t = 0; t < 2000; t++) {
    const a = Number(authorshipStrength.value);
    const p = {
      x: t * 0.4,
      y: canvas.height / 2 + a * Math.sin((t + t0) * 0.005)
    };
    if (t === 0) ctx.moveTo(p.x, p.y);
    else ctx.lineTo(p.x, p.y);
  }
  ctx.stroke();

  // Warp
  ctx.strokeStyle = warpColor.value;
  ctx.lineWidth = 1;
  ctx.beginPath();
  for (let t = 0; t < 2000; t++) {
    const w = Number(warpIntensity.value);
    const p = {
      x: t * 0.4,
      y: canvas.height / 2 + w * Math.sin((t + t0) * 0.02)
    };
    if (t === 0) ctx.moveTo(p.x, p.y);
    else ctx.lineTo(p.x, p.y);
  }
  ctx.stroke();
}

function drawMainWorldline() {
  ctx.strokeStyle = mainColor.value;
  ctx.lineWidth = 2;

  ctx.beginPath();
  for (let t = 0; t < 2000; t++) {
    const p = r(t);
    if (t === 0) ctx.moveTo(p.x, p.y);
    else ctx.lineTo(p.x, p.y);
  }
  ctx.stroke();
}
presetOrigin.onclick = () => {
  originStability.value = 120;
  authorshipStrength.value = 0;
  warpIntensity.value = 0;
};

presetAuthorship.onclick = () => {
  originStability.value = 20;
  authorshipStrength.value = 140;
  warpIntensity.value = 0;
};

presetSovereignty.onclick = () => {
  sovereigntyLock.checked = true;
  originStability.value = 60;
  authorshipStrength.value = 60;
  warpIntensity.value = 0;
};

presetWarp.onclick = () => {
  originStability.value = 0;
  authorshipStrength.value = 0;
  warpIntensity.value = 160;
};

presetFull.onclick = () => {
  originStability.value = 80;
  authorshipStrength.value = 80;
  warpIntensity.value = 80;
  sovereigntyLock.checked = true;
};
function drawFieldDensity() {
  const img = ctx.createImageData(canvas.width, canvas.height);
  const data = img.data;

  for (let y = 0; y < canvas.height; y += 4) {
    for (let x = 0; x < canvas.width; x += 4) {
      let minDist = Infinity;
      for (let t = 0; t < 2000; t += 10) {
        const p = r(t);
        const dx = p.x - x;
        const dy = p.y - y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < minDist) minDist = dist;
      }

      const intensity = Math.max(0, 1 - minDist / 200);
      const idx = (y * canvas.width + x) * 4;
      data[idx] = 20;
      data[idx + 1] = 20;
      data[idx + 2] = 40 + intensity * 200;
      data[idx + 3] = intensity * 120;
    }
  }

  ctx.putImageData(img, 0, 0);
}

function blendLayers() {
  ctx.globalCompositeOperation = "lighter";
}

function drawWarpTrail() {
  ctx.strokeStyle = warpColor.value + "88";
  ctx.lineWidth = 1;

  ctx.beginPath();
  for (let t = 0; t < 2000; t++) {
    const p = applyWarp(t, Number(warpIntensity.value), Number(warpIntensity.value) * 0.5);
    const trailY = p.y + Math.sin((t + t0) * 0.03) * 20;
    if (t === 0) ctx.moveTo(p.x, trailY);
    else ctx.lineTo(p.x, trailY);
  }
  ctx.stroke();
}
function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  blendLayers();

  drawFieldDensity();
  drawLayers();
  drawMainWorldline();
  drawWarpComposite();
  drawWarpTrail();
  drawCurvature();

  // Sync 3D
  if (scene) {
    if (originLayer3D) scene.remove(originLayer3D);
    if (authLayer3D) scene.remove(authLayer3D);
    if (warpLayer3D) scene.remove(warpLayer3D);

    build3DLayers();

    if (warpVolume) {
      const scale = 1 + Number(warpIntensity.value) / 200;
      warpVolume.scale.set(scale, scale, scale);
    }

    if (sovereigntyShell) {
      sovereigntyShell.material.opacity = sovereigntyLock.checked ? 0.15 : 0.02;
    }
  }

  const speed = Number(timeSpeed.value) / 1000;
  t0 += speed * 10;

  requestAnimationFrame(draw);
}
