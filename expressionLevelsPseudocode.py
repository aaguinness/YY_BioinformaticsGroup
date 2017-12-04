from plotnine import *
expression = ggplot(data=RNAseqfile1,aes(x="mouse type",color="red"))
    +geom_bar(RNAseqfile2,aes(x="mouse type",color="orange"))
    +geom_bar(RNAseqfile3,aes(x="mouse type",color="green"))
    +geom_bar(RNAseqfile4,aes(x="mouse type",color="blue"))
    