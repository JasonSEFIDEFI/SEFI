# SEFI‑PY: Single Entity Field Interpretation (Python Core)

SEFI‑PY is a geometric field engine that models a single entity’s identity, autonomy, and dynamic behavior as a layered field. It is the Python implementation of SEFI (Single Entity Field Interpretation), designed to be structurally parallel to SEFI‑JS and suitable for research, simulation, and extension.

---

## Core Concept

An entity is represented as a **field** with layered interpretation:

- **FIELD ORIGIN** — raw geometric state (position, momentum)
- **FIELD AUTHORSHIP** — expressed identity derived from origin
- **FIELD SOVEREIGNTY** — autonomous persistence and self‑governance
- **WARP:EXPRESSION** — dynamic expression of the sovereign field
- **WARP:DEFI** — Dynamic Entity Field Integration (active manipulation of the field)

Each layer is geometric, minimal, and stable, and each builds directly on the previous.

---

## Project Structure

```text
SEFI-PY/
    main.py
    core/
        __init__.py
        field_origin.py
        field_authorship.py
        field_sovereignty.py
        warp_expression.py
        warp_defi.py
    utils/
        __init__.py
        geometry.py
        stability.py
    tests/
        test_core.py
# SEFI-PY Engine

SEFI-PY is the Python implementation of the Single Entity Field Interpretation (SEFI) engine.

## Features
- Full SEFI layer stack (Origin, Authorship, Sovereignty, Expression, DEFI)
- Simulation engine with:
  - geometric evolution
  - behavioral layer
  - multi-entity interaction
  - environment forces
  - DNA identity configuration
- Config-driven architecture
- Full test suite

## Run Simulation

## Render a PowerPoint Video

The presentation runner renders the canonical narrative sequence and assembles a single PowerPoint-ready 16:9 MP4 at 1920x1080 and 30 fps:

```powershell
.\render_presentation.ps1
```

The final video is written to `animations/presentation/SEFI-boardroom.mp4`. Use a fast half-resolution preview while iterating:

```powershell
.\render_presentation.ps1 -Preview
```

To render another scene, pass its source file and class name:

```powershell
.\render_presentation.ps1 core/animations/sefi_core.py SEFICore
```

To render one scene in isolation, pass its source file and class name:

```powershell
.\render_presentation.ps1 core/animations/sefi_core.py SEFICore
```

The assembled MP4 and individual clips are saved in `animations/presentation`. Insert `SEFI-boardroom.mp4` into PowerPoint as a video.
