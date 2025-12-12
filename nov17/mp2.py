
def e(t):
    u = set()
    for d in t:
        u.update(d.values())
    return u
dicts = [
    {"a": 1, "b": 2, "c": 1},
    {"d": 3, "e": 2, "f": 4},
    {"g": 1, "h": 5, "i": 3}
]

vals = list(e(dicts))
s=sum(vals)
print(f"The unique values are: {vals}")
print(f"The sum of unique values is: {s}")