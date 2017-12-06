import sys
import os
import shutil
import subprocess
import pandas as pd

# load codon table and turn it into a dictionary
with open("codonmap.txt") as fin:
    rows = (line.split('\t') for line in fin)
    codontable = {row[0]: row[1:] for row in rows}

def translate(seq):
    peptide = ''
    start = seq.find('ATG')
    seqtrimmed = seq[int(start):]
    for n in range(0, len(seqtrimmed), 3):
        codon = seqtrimmed[n:n + 3]
        aa = codontable.get(codon, '*')
        if aa != '_':
            peptide += aa
        else:
            break
    return peptide



# load fasta file
fasta = open('control1.fasta',"r")

# loop over the file
for line in fasta:
    line = line.strip()
    if ">" in line:
        seqid = line
        print seqid
    else:
        trans = translate(line)
        print trans


