
def e(d1,d2):
    d1.update(d2)

    return d1



d1 ={"a": 1, "b": 2, "c": 1}
d2 ={"d": 3, "e": 2, "f": 4}
print(f"The unique values are: {e(d1, d2)}")
marge={**d1,**d2}
print(marge)