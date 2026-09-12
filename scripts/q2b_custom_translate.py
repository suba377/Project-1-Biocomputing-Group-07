genetic_code = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}
# Opening and readinf the extracted CDS file
cds_file = open("data/GAPDH_cds.fasta", "r")
lines = cds_file.readlines()
cds_file.close()
# Extracting the only the sequence text
cds_sequence = ""
for line in lines:
    if not line.startswith(">"):
        cds_sequence = cds_sequence + line.strip()
#translation
protein_sequence = ""
for i in range(0, len(cds_sequence), 3):
    codon = cds_sequence[i:i+3]

    if codon in genetic_code:
        amino_acid = genetic_code[codon]
        if amino_acid == "*":
            break

        protein_sequence = protein_sequence + amino_acid
print("First 30 amino acids:", protein_sequence[:30])
print("Total translated protein length:", len(protein_sequence))
# Saving  translated protein to results folder
output_file = open("results/GAPDH_custom_translated.fasta", "w")
output_file.write(">GAPDH_custom_translation\n")
output_file.write(protein_sequence + "\n")
output_file.close()
