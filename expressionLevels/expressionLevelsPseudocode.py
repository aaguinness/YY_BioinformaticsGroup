import pandas
from plotnine import *
Transcript1 = pandas.read_csv("1.sequences.table")
###somehow add column titles so ggplot knows what to do
Transcript2 =
Transcript6 = 
Transcript9 = 
Transcript10 =
expression = ggplot(data=Transcript1,aes(x="",color="red"))
    +geom_bar(Transcript2,aes(x="mouse type",color="orange"))
    +geom_bar(Transcript3,aes(x="mouse type",color="green"))
    +geom_bar(Transcript4,aes(x="mouse type",color="blue"))
    +geom_bar(Transcript5,aes(x="mouse type",color="blue"))
    +geom_bar(Transcript6,aes(x="mouse type",color="blue"))
