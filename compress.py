from sys import getsizeof
def compress(gene: str) -> int:
    res = 1
    for c in gene.upper():
        res <<= 2
        if c == "A":
            res |= 0b00
        elif c == "C":
            res |= 0b01
        elif c == "G":
            res |= 0b10
        elif c == "T":
            res |= 0b11
    return res
gene = "ACTGGGTACCGTTTTTTAAAACGCGCTAAATTTTTTTGGGCGCGCGCAAAGTGTGTGTGCACACA"
print(getsizeof(gene))
print(getsizeof(compress(gene)))