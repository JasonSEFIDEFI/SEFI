# SEFI-PY
A modular scientific engine implementing the Single Entity Field Interpretation (SEFI), Dynamic Entity Field Integration (DEFI), and the Geometric Waveform Model (GWFM).  
SEFI-PY provides a unified geometric framework for worldlines, warp modes, curvature, torsion, collapse behavior, and quantum error correction.

---

## Core Architecture

### SEFI (Single Entity Field Interpretation)
A geometric field model describing:
- Worldline stability
- Field origin, authorship, and sovereignty layers
- Warp modes (tangent, normal, binormal)
- Collapse geometry and measurement behavior

### DEFI (Dynamic Entity Field Integration)
A dynamic realignment model used for:
- Correction
- Stabilization
- Worldline restoration
- Error integration and geometric consistency

### GWFM (Geometric Waveform Model)
A waveform interpretation built on geometric invariants.

---

## SEFI-QEC: Quantum Error Correction Subsystem

SEFI-QEC integrates quantum error correction directly into the geometric field engine.  
Logical qubits are represented as SEFI worldlines, and physical qubits are geometric samples of that worldline.

### Features
- Real Pauli operations (X, Z, Y)
- Stabilizer parity checks (Z1Z2, Z2Z3)
- Syndrome extraction
- DEFI-based correction
- Warp-mode → error-mode mapping
- Warp-residual geometric alignment
- Pauli-frame consistency checking
- Majority-vote logical consistency
- Stabilizer-energy minimization decoder
- Multi-angle QEC benchmarking

### QEC Checking Suite (5 independent decoders)
1. **Stabilizer Parity Check**  
   Classical repetition-code stabilizers.

2. **Majority Vote Check**  
   Independent logical consistency decoder.

3. **Pauli-Frame Consistency**  
   Frame-based mismatch detection.

4. **Warp-Residual Geometric Check**  
   SEFI-native geometric deviation analysis.

5. **Stabilizer-Energy Minimization**  
   Physics-inspired energy-based decoder.

These decoders run independently and can be cross-validated, providing a multi-angle correction suite.

---

## Benchmarking

SEFI-QEC includes a benchmarking module that:
- Injects random X/Z/Y errors
- Runs all decoders
- Applies DEFI correction
- Measures recovery success rate

The full suite currently passes at **100%**.

---

## Project Status
SEFI-PY remains fully green across all modules:
- SEFI core
- DEFI integration
- GWFM
- Warp simulation
- Quantum warp simulation
- SEFI-QEC subsystem
- Multi-decoder QEC suite
- Benchmarking

All tests pass at 100%.

---

## Running the QEC Demo

```python
from sefi_qec.runner import run_sefi_qec_demo
run_sefi_qec_demo()
