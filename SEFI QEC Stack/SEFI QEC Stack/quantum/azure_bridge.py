try:
    from azure.quantum import Workspace

    AZURE_AVAILABLE = True

except Exception:

    AZURE_AVAILABLE = False


class AzureBridge:

    def __init__(self):

        self.connected = False

    def connect(self):

        if not AZURE_AVAILABLE:
            return False

        self.connected = True

        return True

    def status(self):

        return {
            "azure_available": AZURE_AVAILABLE,
            "connected": self.connected,
        }