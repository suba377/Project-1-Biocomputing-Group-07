with open("results/translated_protein.txt") as f:
    translated = f.read().strip()

with open("results/deposited_protein.txt") as f:
    deposited = f.read().strip()

print("Translated protein:")
print(translated)

print("\nDeposited protein:")
print(deposited)

print("\nComparison:")

if translated == deposited:
    print("The two sequences are identical.")
else:
    print("The two sequences are different.")
