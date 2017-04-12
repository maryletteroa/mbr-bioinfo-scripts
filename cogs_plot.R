setwd('E:/Mtb/05_draft/snpsCog/')
library(ggplot2)
library(grid)
library(gridExtra)
df = read.csv2('nr.cogcounts.txt.1',sep='\t',header=FALSE)

df.sorted <- df[order(-df$V2),]

p1 <- ggplot(data=df.sorted, aes(x=reorder(V1,-V2),y=V2)) +
       geom_bar(stat='identity') +
       geom_text(aes(label=V2), vjust=-0.3, color="black", size=3.5)+
       coord_cartesian(ylim=c(0,410)) +
       theme(plot.margin=unit(c(0,0,0,0),"lines")) +
       theme_minimal() +
       labs(x='Cluster of Orthologous Groups (COGs)', y='Number of genes' )
p1
