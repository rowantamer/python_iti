def all_unique(seq):
    return len(seq) == len(set(seq))

print (all_unique([1, 2, 3, 4, 5]))
print (all_unique([1, 2, 3, 3, 4, 5]))