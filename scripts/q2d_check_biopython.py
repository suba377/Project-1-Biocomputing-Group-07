from Bio.Seq import Seq

# Reading raw CDS text and filter out the header line
f = open("data/GAPDH_cds.fasta", "r")
lines = f.readlines()
f.close()
dna = ""
for line in lines:
    if not line.startswith(">"):
        dna += line.strip()

# Translating it now using BioPython and print result
bio_protein = (Seq(dna).translate(to_stop=True))
print("Biopython translation:")
print(bio_protein)

# Reading my translated protein from Q2(b)
f_my = open("results/GAPDH_custom_translated.fasta", "r")
my_lines = f_my.readlines()
f_my.close()

seq_my_trans = ""
for line in my_lines:
    if not line.startswith(">"):
        seq_my_trans += line.strip()

print("Biopython translation:")
print(bio_protein)
print("\nMy custom translation:")
print(seq_my_trans)

# Verify agreement
if bio_protein == seq_my_trans:
    print("\nResult: Both translations AGREE 100%.")
else:
    print("\nResult: Translations DO NOT AGREE.")
