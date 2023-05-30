import pandas as pd
import csv

df = pd.read_csv("../../data/finalScreen.tsv", sep="\t")
fids = list(set(df["fragId"]))
ds = pd.read_csv("../../data/fid2naked.tsv", sep="\t")
f2s = {}
with open("../../data/fid2naked.tsv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for r in reader:
        f2s[r[0]] = r[1]

with open("../../assets/screened_smiles.smi", "w") as f:
    for fid in fids:
        f.write(f2s[fid]+"\n")