with open("data/SELENOW_mRNA.fasta") as f:
    sequence = ""
    for line in f:
        if not line.startswith(">"):
            sequence += line.strip()

cds = sequence[83:347]

with open("data/SELENOW_CDS.txt", "w") as f:
    f.write(cds)

print("CDS length:", len(cds))
print("Divisible by 3:", len(cds) % 3 == 0)
