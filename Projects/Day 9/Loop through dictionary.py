dictionary={
    "Messi":"The all-time best player.",
    "Ronaldo":"The second best player.",
    "Neymar":"One of the best player."
}
#print keys
for n in dictionary:
    print(n)
#print values
for n in dictionary:
    print(dictionary[n])
#print both in one line
for n in dictionary:
    print(f"{n}:{dictionary[n]}")