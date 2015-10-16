
frame1 <- maml.mapInputPort(1)

## Assign scores to the cases.
frame1$Score = ifelse(frame1$readmi_class == 'YES' & frame1$ScoredLabels == 'YES', 'TP',
          ifelse(frame1$readmi_class == 'NO' & frame1$ScoredLabels == "YES", 'FP',
          ifelse(frame1$readmi_class == 'NO' & frame1$ScoredLabels == 'NO', 'TN', 'FN')))

## Compair outcomes for various levels of 
## factor (categorical) features. 
library(ggplot2)
library(dplyr)
bar.plot <- function(x){
  if(is.factor(frame1[, x])){
    sums <- summary(frame1[, x], counts = n())
    msk <- names(sums[which(sums > 100)])
    tmp <- frame1[frame1[, x] %in% msk, c('Score', x)]
    if(strsplit(x, '[-]')[[1]][1] == x){
      g <- ggplot(tmp, aes_string(x)) +
        geom_bar() +
        facet_grid(. ~ Score) +
        ggtitle(paste('Readmissions by level of', x))
      print(g)    
    }    
  }    
}
cols <- names(frame1)
cols <- cols[1:(length(cols) - 1)]
lapply(cols, bar.plot)

## Box plot the numeric features
box.plot <- function(x){
  if(is.numeric(frame1[, x])){
    ggplot(frame1, aes_string('Score', x)) +
      geom_boxplot(alpha = 0.1) +
      ggtitle(paste('Readmissions by', x))
  }
}
dropCols <- ncol(frame1)
dropCols <- c((dropCols - 2):dropCols)
lapply(names(frame1[, -c(dropCols)]), box.plot)
