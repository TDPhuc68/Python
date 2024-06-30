def format_number_with_commas(n):
    s = str(n)
    parts =[]
    while len(s) > 3 :
        parts.insert(0,s[-3:])
        s = s[:-3]
    parts.insert(0,s)
    return ",".join(parts)

n =input()
print(format_number_with_commas(n))