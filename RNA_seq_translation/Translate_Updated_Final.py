mport pandas
import numpy as np
import scipy
import scipy.integrate as spint
import glob
from plotnine import *
import os
os.getcwd()

codonmap = {}
with open("codonmap.txt") as f:
    for line in f:
       (val, key) = line.split()
       codonmap[key] = val
  
def translate(seq):
    peptide = ''
    
    start = seq.find('ATG')
    seqtrimmed = seq[int(start):]
    for n in range(0,len(seqtrimmed),3):
        codon = seqtrimmed[n:n+3]
        aa = codonmap.get(codon, '*')
        if aa != 'Stop':
            peptide += aa
        else:
            break
    return peptide
    
for fasta_file in glob.iglob('newseq/*.fasta'):
    InFile=open(fasta_file,"r") #Open fasta file as read-only
    Out_file = os.path.basename(fasta_file)
    with open(Out_file.split(".")[0]+"_translated.fasta",'a') as f:
        for line in InFile: #Loop through each line in fasta file
            if '>' in line:
                f.write(line)#Check line for >, if present, skip to next line
                continue
        
            else:
                f.write(translate(line)+'\n') #Translation
f.close()            
InFile.close()
            
        