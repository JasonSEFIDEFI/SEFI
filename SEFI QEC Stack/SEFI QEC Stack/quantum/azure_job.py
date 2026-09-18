from quantum.azure_bridge import AzureBridge


class AzureSEFIJob:
    """
    Azure Quantum submission wrapper.
    """

    def __init__(self):

        self.bridge = AzureBridge()

    def connect(self):

        return self.bridge.connect()

    def status(self):

        return self.bridge.status()

    def submit_register(self, register):

        return {
            "submitted": True,
            "logical_qubits": len(register.bits),
            "status": "simulated",
        }
``