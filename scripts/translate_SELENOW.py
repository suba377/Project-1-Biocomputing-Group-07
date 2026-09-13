codon_table = {
"ATG":"M","TTT":"F","TTC":"F","TTA":"L","TTG":"L",
"TCT":"S","TCC":"S","TCA":"S","TCG":"S",
"TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
"TGT":"C","TGC":"C","TGA":"*","TGG":"W",
"CTT":"L","CTC":"L","CTA":"L","CTG":"L",
"CCT":"P","CCC":"P","CCA":"P","CCG":"P",
"CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
"CGT":"R","CGC":"R","CGA":"R","CGG":"R",
"ATT":"I","ATC":"I","ATA":"I","ACT":"T",
"ACC":"T","ACA":"T","ACG":"T",
"AAT":"N","AAC":"N","AAA":"K","AAG":"K",
"AGT":"S","AGC":"S","AGA":"R","AGG":"R",
"GTT":"V","GTC":"V","GTA":"V","GTG":"V",
"GCT":"A","GCC":"A","GCA":"A","GCG":"A",
"GAT":"D","GAC":"D","GAA":"E","GAG":"E",
"GGT":"G","GGC":"G","GGA":"G","GGG":"G"
}

with open("data/SELENOW_CDS.txt") as f:
    dna = f.read().replace("\n", "")

protein = ""

for i in range(0, len(dna), 3):
    codon = dna[i:i+3]

    if codon == "TGA" and i == 36:
        protein += "U"
    elif codon in ["TAA", "TAG", "TGA"]:
        break
    else:
        protein += codon_table[codon]
print("DNA length:", len(dna))
print("Number of codons:", len(dna)//3)
print("Protein length:", len(protein))
print("First 30 residues:", protein[:30])
print("Total length:", len(protein))
print(protein)
with open("results/deposited_protein.txt") as f:
    deposited = f.read().strip()

if protein == deposited:
    print("No difference")
else:
    print("Difference found")
