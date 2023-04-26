
def combine_halves(a, b):
    len_a = len(a)
    len_b = len(b)
    half_a = (len_a + 1) // 2
    half_b = (len_b + 1) // 2
    return a[:half_a] + b[:half_b] + a[half_a:] + b[half_b:]

print (combine_halves("abcd", "efgh"))
print (combine_halves("abcde", "12345"))