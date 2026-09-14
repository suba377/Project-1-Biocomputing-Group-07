with open("results/translated_protein.txt") as f:
    translated = f.read().strip()

with open("results/deposited_protein.txt") as f:
    deposited = f.read().strip()

translated_length = len(translated)
deposited_length = len(deposited)

print("Translated protein length:", translated_length)
print("Deposited protein length:", deposited_length)
print("Difference:", abs(translated_length - deposited_length))
