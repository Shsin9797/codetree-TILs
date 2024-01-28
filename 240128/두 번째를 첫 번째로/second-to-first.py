s = input()

fir = s[0]
sec= s[1]

s = list(s)

for i in range(len(s)):
    if s[i] == sec:
        s[i] = fir

print("".join(s))