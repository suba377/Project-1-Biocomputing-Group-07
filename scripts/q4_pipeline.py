from Bio import SeqIO
from Bio.Seq import Seq


def read_fasta(file):
    record = SeqIO.read(file, "fasta")
    return str(record.seq)


def compare(a, b):
    if a == b:
        return "Y", "None"

    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return "N", str(i + 1)

    return "N", "Length difference"


# SELENOW
with open("data/SELENOW_CDS.txt") as f:
    selenow_cds = f.read().strip()

selenow_protein = read_fasta("data/SELENOW_protein.fasta")

selenow_translated = ""

for i in range(0, len(selenow_cds), 3):
    codon = selenow_cds[i:i+3]

    if codon == "TGA" and i == 36:
        selenow_translated += "U"
    elif codon in ["TAA", "TAG", "TGA"]:
        break
    else:
        selenow_translated += str(Seq(codon).translate())


# MT-ND4
mt_record = SeqIO.read(
    "data/MT-ND4_Mitochondrial_Gene.gb", "genbank"
)

mt_cds = ""

for feature in mt_record.features:
    if feature.type == "CDS":
        if "ND4" in str(feature.qualifiers.get("gene", "")):
            mt_cds = str(feature.extract(mt_record.seq))
            break

mt_protein = read_fasta("data/MT-ND4_Protein.fasta")

mt_translated = str(Seq(mt_cds).translate(table=2))[:-1]


# GAPDH
gapdh_cds = read_fasta("data/GAPDH_cds.fasta")
gapdh_protein = read_fasta("data/NP_002037.2.fasta")

gapdh_translated = str(Seq(gapdh_cds).translate(to_stop=True))


# Final comparison
results = [
    ["SELENOW", "A", selenow_cds, selenow_translated, selenow_protein],
    ["MT-ND4", "B", mt_cds, mt_translated, mt_protein],
    ["GAPDH", "C", gapdh_cds, gapdh_translated, gapdh_protein]
]


print("Gene       Category   CDS    Translated   Deposited   Identical   Mismatch")
print("-" * 80)

for gene, category, cds, translated, deposited in results:

    identical, mismatch = compare(translated, deposited)

    print(
        f"{gene:<10} {category:<10} {len(cds):<6} "
        f"{len(translated):<12} {len(deposited):<11} "
        f"{identical:<10} {mismatch}"
    )
