"""
SEFI-QEC: Quantum Error Correction module for the SEFI-PY scientific engine.

This package implements a geometric view of quantum error correction,
mapping SEFI worldlines and warp behavior onto stabilizer codes,
syndrome extraction, and correction pipelines.
"""

from .runner import run_sefi_qec_demo

__all__ = ["run_sefi_qec_demo"]
