t = (1, 2, 3, 2, 4, 5, 1)
repeated = set([x for x in t if t.count(x) > 1])
print(repeated)