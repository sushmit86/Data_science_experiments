library(ggplot2)
cust.df <- read.csv("http://goo.gl/PmPkaG")
cust.df$cust.id <- factor(cust.df$cust.id)

p1<- ggplot(cust.df, aes(age, credit.score))  + geom_point(color ='blue') +xlab("Customer Age (years)") +
  ylab("Customer Credit Scorel")  + ggtitle("Active Customers as of June 2014")

p2 <- p1 +geom_vline(xintercept = mean(cust.df$age) ,linetype="dotted",color = 'red') + 
  geom_hline(yintercept = mean(cust.df$credit.score))
p2 +scale_x_continuous(limits = c(15, 55)) +scale_y_continuous(limits = c(500, 900))


# Scatterplot with skewed variables and color-coded factors
plot(cust.df$store.spend, cust.df$online.spend, 
     main="Customers as of June 2014", 
     xlab="Prior 12 months in-store sales ($)", 
     ylab="Prior 12 months online sales ($)", 
     cex=0.7)

p1 <- ggplot(cust.df, aes(store.spend,online.spend)) + 
  geom_point() + ggtitle("Active Customers as of June 2014")
p2 <- p1 + xlab("Prior 12 months in-store sales ($)") + 
  ylab("Prior 12 months online sales ($)") + scale_size(0.3)
p2
 

