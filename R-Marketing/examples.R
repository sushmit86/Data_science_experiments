satData <- read.csv("http://goo.gl/UDv12g")
satData$Segment <-  factor(satData$Segment)
head(satData)
summary(satData)
library(corrplot)
corrplot.mixed(cor(satData[,-3]))
aggregate(iProdSAT ~ Segment, satData,mean)
sat.anova  <- aov(iProdSAT ~ -1 + Segment,satData)
summary(sat.anova)
library(multcomp)
par(mar = c(4,8,4,2))
plot(glht(sat.anova))
seq(from = -5,to = 28, by =4)
rep(c(1,2,3),each =4)
xSeq =1:10
xSeq[-5:-7]
xNum = 10:20
xSub <- xNum[2:4]
xNum = c(1.0,3.14,5.0,7.0)
xNum
xNum[c(FALSE, TRUE, TRUE,TRUE)]
xNum[xNum > 5]
str(xNum)
xChar <- c("foo","bar","boo","far")
xList <- list(xNum, xChar)
xList[1]
xChar <- c("foo","bar","boo","far")
str(xChar)
list.files()