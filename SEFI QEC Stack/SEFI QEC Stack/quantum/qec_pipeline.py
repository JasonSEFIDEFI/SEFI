from quantum.logical_register import LogicalPhiRegister
from quantum.sefi_stabilizers import (
    authorship_stabilizer,
    metric_stabilizer,
    origin_stabilizer,
    sovereignty_stabilizer,
    warp_stabilizer,
)
from quantum.stabilizer_code import SEFIStabilizerCode


def build_quantum_pipeline(phi):

    register = LogicalPhiRegister(phi)

    code = SEFIStabilizerCode()

    code.add(
        "origin",
        origin_stabilizer
    )

    code.add(
        "authorship",
        authorship_stabilizer
    )

    code.add(
        "sovereignty",
        sovereignty_stabilizer
    )

    code.add(
        "warp",
        warp_stabilizer
    )

    code.add(
        "metric",
        metric_stabilizer
    )

    return {
        "register": register,
        "syndrome": code.evaluate(register),
    }