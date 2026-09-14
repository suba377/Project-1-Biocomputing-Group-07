from Bio.Seq import Seq

with open("data/SELENOW_CDS.txt") as f:
    dna = f.read().strip()

biopython_protein = str(Seq(dna).translate())

print("Biopython translation:")
print(biopython_protein)

print("\nMy translation:")
with open("results/translated_protein.txt") as f:
    my_protein = f.read().strip()

print(my_protein)

print("\nComparison:")

if biopython_protein == my_protein + "*":
    print("The sequences agree except for the internal TGA and terminal stop codon.")
else:
    print("The sequences do not completely agree.")
