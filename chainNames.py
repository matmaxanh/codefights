#You're given an array of names, where each name is given as a string.
#Your task is to link these names into a chain, so that the ith name starts with the same letter the (i - 1)th name ends, and return this chain as a list.
#All names should be used. It is guaranteed that each name starts with a unique letter. It is also guaranteed that there is only one solution.

def chainNames(n):
    d = {s[0].lower():s for s in n}
    for w in d:
        l = dict(d)
        c = []
        while w:
            w = l.pop(w[-1],0)
            c += w,
            if not l:
                return c

# Test
names = ["Raymond",  "Nora", "Daniel", "Louie", "Peter", "Esteban"]
print chainNames(names) == ["Peter", "Raymond", "Daniel", "Louie", "Esteban", "Nora"]

names = ["Tigran"]
print chainNames(names) == ["Tigran"]
