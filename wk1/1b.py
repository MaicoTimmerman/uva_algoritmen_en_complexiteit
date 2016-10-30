def NPerms (seq):
    "computes the factorial of the length of "
    return reduce (lambda x, y: x * y, range (1, len (seq) + 1), 1)

def PermN2 (seq, index):
    "Returns the th permutation of lexografical order"
    seqc = list(seq[:])
    result = []
    fact = NPerms(seq)
    index = index % fact
    while seqc:
        fact = fact / len(seqc)
        choice = index // fact
        index = index % fact
        result = result + [seqc.pop (choice)]
    return result

print PermN2(list(range(0,25)),5170403347776995327994765)
