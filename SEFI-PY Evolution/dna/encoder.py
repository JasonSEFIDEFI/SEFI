class DNAEncoder:
    """
    Encodes genomic nucleotide sequences into 4D SEFI identity components.
    """
    NUCLEOTIDE_MAP = {
        'A': [1.0, 0.0, 0.0, 0.0],
        'T': [0.0, 1.0, 0.0, 0.0],
        'C': [0.0, 0.0, 1.0, 0.0],
        'G': [0.0, 0.0, 0.0, 1.0]
    }

    @classmethod
    def encode_sequence(cls, sequence: str):
        return [cls.NUCLEOTIDE_MAP.get(n.upper(), [0.0, 0.0, 0.0, 0.0]) for n in sequence]