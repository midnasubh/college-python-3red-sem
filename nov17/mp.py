
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

vals = e(dicts)
print(f"The unique values are: {vals}")