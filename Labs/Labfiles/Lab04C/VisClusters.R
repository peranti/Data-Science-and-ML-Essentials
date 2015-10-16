frame1 <- maml.mapInputPort(1)
library(ggplot2)

## Compute principal components and 
## plot the clusters projected by the first two.
numCols <- c("FFMC", "DMC", "DC", "ISI", "temp",   
             "RH", "wind", "area")
pcfit <- princomp(frame1[, numCols])
pcframe <- data.frame( as.matrix(frame1[, numCols]) 
                       %*% pcfit$loadings[, 1:2],
                       Assignments = frame1$Assignments)
      
ggplot(pcframe, aes(Comp.1, Comp.2)) + 
  geom_point(aes(shape = factor(Assignments), 
                 color = factor(Assignments)), 
             alpha = 0.3, size = 4) +
  ggtitle(paste("clusters by first two principle components")) +
  xlab("Pricipal component 1") + ylab("Principal component 2")


## Create scatter plots of certain numeric columns vs. area.
numCols <- c("FFMC", "DMC", "DC", "ISI", "temp",   
             "RH", "wind")
plot.clusts <- function(x){
  ggplot(frame1, aes_string(x, 'area')) +
           geom_point(aes(shape = factor(Assignments), 
                          color = factor(Assignments)), 
                      alpha = 0.3, size = 4) +
           ggtitle(paste("clusters for", x, "vs. area"))
}
lapply(numCols, plot.clusts)


## Look at scatter plots of the clusters by FFMC.
numCols <- c("DC", "DMC", "ISI", "temp",   
             "RH", "wind", "area")

plot.clusts2 <- function(x){
  ggplot(frame1, aes_string(x, 'FFMC')) +
    geom_point(aes(shape = factor(Assignments), 
                   color = factor(Assignments)), 
               alpha = 0.3, size = 4) +
    ggtitle(paste("clusters for", x, "vs. FFMC"))
}
lapply(numCols, plot.clusts2)
