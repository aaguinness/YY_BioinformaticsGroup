#load packages
import pandas as pd
from plotnine import *
import os

os.chdir("..")
os.chdir("./NCBI_protien_search_results/hits_table")

#read in hmm search output files and add column names for ggplot
Transcript1 = pd.read_csv("1.sequences.table", sep=' ', header=None)
Transcript1.columns = ["Mouse", "Match sequence", "Score"]
Transcript2 = pd.read_csv("2.sequences.table", sep=' ', header=None)
Transcript2.columns = ["Mouse", "Match sequence", "Score"]
Transcript6 = pd.read_csv("6.sequences.table", sep=' ', header=None)
Transcript6.columns = ["Mouse", "Match sequence", "Score"]
Transcript8 = pd.read_csv("8.sequences.table", sep=' ', header=None)
Transcript8.columns = ["Mouse", "Match sequence", "Score"]
Transcript9 = pd.read_csv("9.sequences.table", sep=' ', header=None)
Transcript9.columns = ["Mouse", "Match sequence", "Score"]
Transcript10 = pd.read_csv("10.sequences.table", sep=' ', header=None)
Transcript10.columns = ["Mouse", "Match sequence", "Score"]

#Plot of Expression for each transcript based on mouse identity
expressionT1 = (ggplot(Transcript1,aes(x="Mouse"))
    +geom_bar(fill='red')
    +ggtitle("Gsta2")
    +ylab("Relative Expression")
    +theme_classic())
expressionT2 = (ggplot(Transcript2,aes(x="Mouse"))
    +geom_bar(fill='orange')
    +ggtitle("Scl7a12")
    +ylab("Relative Expression")
    +theme_classic())
expressionT6 = (ggplot(Transcript6,aes(x="Mouse"))
    +geom_bar(fill='yellow')
    +ggtitle("Ptpn5")
    +ylab("Relative Expression")
    +theme_classic())
expressionT8 = (ggplot(Transcript8,aes(x="Mouse"))
    +geom_bar(fill='green')
    +ggtitle("ATP12a")
    +ylab("Relative Expression")
    +theme_classic())
expressionT9 = (ggplot(Transcript9,aes(x="Mouse"))
    +geom_bar(fill='blue')
    +ggtitle("Lhx2")
    +ylab("Relative Expression")
    +theme_classic())
expressionT10 = (ggplot(Transcript10,aes(x="Mouse"))
    +geom_bar(fill='purple')
    +ggtitle("Synpr")
    +ylab("Relative Expression")
    +theme_classic())
print(expressionT1)
print(expressionT2)
print(expressionT6)
print(expressionT8)
print(expressionT9)
print(expressionT10)

