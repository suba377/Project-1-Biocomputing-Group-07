# Reading mRNA FASTA file
with open("data/NM_002046.7.fasta", "r") as f:
	lines = f.readlines()
# Extracting the sequence lines (ignoring header)
mrna_sequence = ""
for line in lines:
    if not line.startswith(">"):
        mrna_sequence = mrna_sequence + line.strip()
#GenBank 1-based coordinates were 77 to 1084 so we will first change the coordinates according to python which is 0 based,
# thus new coordinates will be 76 to 1084
cds_seq = mrna_sequence[76:1084]
print("CDS Length:", len(cds_seq))
print("Divisible by 3:", len(cds_seq) % 3 == 0)
# now save CDS sequence to data folder
output_file = open("data/GAPDH_cds.fasta", "w")
output_file.write(">GAPDH_CDS_77_1084\n")
output_file.write(cds_seq + "\n")
output_file.close()
