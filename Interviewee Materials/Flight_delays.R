library(ggplot2)
# Reading the data
CancelledFlights <- read.csv(file="CancelledFlights.csv",head=FALSE,sep=",")
# adding column names
colnames(CancelledFlights) <- c("Canceled","Month","DepartureTime","UniqueCarrier","SchedElapsedTime","ArrDelay","DepDelay","Distance")
# Reading first few columns
head(CancelledFlights)
# checking if there is any na data
sum(is.na(CancelledFlights))


attach(CancelledFlights)
# some data exploration
table(Month,Canceled)

par(mfrow = c(1,2))
cancel_month <- table(Canceled,Month)
barplot(cancel_month, col=c("darkblue","red"),legend = rownames(cancel_month))
cancel_unique_carrier <- table(Canceled,UniqueCarrier)
barplot(cancel_unique_carrier, col=c("darkblue","red"),legend = rownames(cancel_unique_carrier))
