from Bio.Seq import Seq

with open("data/SELENOW_CDS.txt") as f:
    dna = f.read().replace("\n", "")

protein = Seq(dna).translate()

print("Biopython translation:")
print(protein)
