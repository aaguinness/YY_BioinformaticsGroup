#load packages
import pandas
from plotnine import *

#read in hmm search output files and add column names for ggplot
Transcript1 = pd.read_csv("1.sequences.table", sep=' ', header=None)
Transcript1.columns = ["Mouse", "Match sequence", "Score"]
Transcript2 = pd.read_csv("2.sequences.table", sep=' ', header=None)
Transcript2.columns = ["Mouse", "Match sequence", "Score"]
#note: there were no matches for Transcript 6 in any mouse
#so this is empty
Transcript6 = pd.read_csv("6.sequences.table", sep=' ', header=None)
Transcript6.columns = ["Mouse", "Match sequence", "Score"]
Transcript8 = pd.read_csv("8.sequences.table", sep=' ', header=None)
Transcript8.columns = ["Mouse", "Match sequence", "Score"]
#note: there were no matches for Transcript 9 in any mouse
Transcript9 = pd.read_csv("9.sequences.table", sep=' ', header=None)
Transcript9.columns = ["Mouse", "Match sequence", "Score"]
Transcript10 = pd.read_csv("10.sequences.table", sep=' ', header=None)
Transcript10.columns = ["Mouse", "Match sequence", "Score"]

#Plot of Expression for each transcript based on mouse identity
expressionT1 = (ggplot(Transcript1,aes(x="Mouse"))
    +geom_bar(fill='red')
    +ggtitle("Transcript 1")
    +ylab("Relative Expression")
    +theme_classic())
expressionT2 = (ggplot(Transcript2,aes(x="Mouse"))
    +geom_bar(fill='orange')
    +ggtitle("Transcript 2")
    +ylab("Relative Expression")
    +theme_classic())
expressionT8 = (ggplot(Transcript8,aes(x="Mouse"))
    +geom_bar(fill='green')
    +ggtitle("Transcript 8")
    +ylab("Relative Expression")
    +theme_classic())
expressionT10 = (ggplot(Transcript10,aes(x="Mouse"))
    +geom_bar(fill='blue')
    +ggtitle("Transcript 10")
    +ylab("Relative Expression")
    +theme_classic())
print(expressionT1)
print(expressionT2)
print(expressionT8)
print(expressionT10)


