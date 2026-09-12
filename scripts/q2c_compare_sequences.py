# Reading the translated protein generated from Q2(b)
f_my = open("results/GAPDH_custom_translated.fasta", "r")
my_lines = f_my.readlines()
f_my.close()

seq_my_trans = ""
for line in my_lines:
    if not line.startswith(">"):
        seq_my_trans += line.strip()
# Now reading the NCBI deposited protein sequence
f_ncbi = open("data/NP_002037.2.fasta", "r")
ncbi_lines = f_ncbi.readlines()
f_ncbi.close()

seq_ncbi = ""
for line in ncbi_lines:
    if not line.startswith(">"):
        seq_ncbi += line.strip()
# Calculateing sequence lengths
n_my_trans = len(seq_my_trans)
n_ncbi = len(seq_ncbi)

# Comparing all the amino acids at each position
match_cnt = 0
diff_list = []

for idx in range(min(n_my_trans, n_ncbi)):
    if seq_my_trans[idx] == seq_ncbi[idx]:
        match_cnt += 1
    else:
        diff_list.append((idx + 1, seq_my_trans[idx], seq_ncbi[idx]))
# Computing the identity percentage
pid = (match_cnt / max(n_my_trans, n_ncbi)) * 100.0

print("My Translation Length:", n_my_trans)
print("NCBI Deposited Length:", n_ncbi)
print("Matching Residues:", match_cnt)
print("Identity Percent:", round(pid, 2), "%")
print("Total Mismatches:", len(diff_list))

if len(diff_list) > 0:
    for pos, aa1, aa2 in diff_list:
        print(f"Position {pos}: Translated={aa1}, NCBI={aa2}")
