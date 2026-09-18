class SEFIStabilizerCode:

    def __init__(self):

        self.stabilizers = []

    def add(self, name, check):

        self.stabilizers.append(
            {
                "name": name,
                "check": check,
            }
        )

    def evaluate(self, register):

        results = {}

        for stabilizer in self.stabilizers:

            results[stabilizer["name"]] = (
                stabilizerregister
            )

        return results