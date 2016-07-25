library(MASS)
set.seed(1)
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

error_vec = rep(0,nrow(CancelledFlights))
for (i in 1:dim(CancelledFlights)[1] ){
  glm.fit = glm(Canceled ~ ., data =CancelledFlights[-i,],family = binomial)
  pos_prob = predict(glm.fit, CancelledFlights[i,],type = "response")
  if(pos_prob > 0.5)
  {
    predicted_value = 1
  }else{
    predicted_value = 0
  }
  if(predicted_value!=CancelledFlights[i,]$Canceled) {
    error_vec[i] = 1
  }
}

print('The Logistic MSE is : ')
print(mean(error_vec))
### lda
error_vec = rep(0,nrow(CancelledFlights))
for (i in 1:dim(CancelledFlights)[1] ){
  lda.fit = lda(Canceled ~ ., data =CancelledFlights[-i,])
  pos_prob =predict(lda.fit, CancelledFlights[i, ])$posterior[,1]
  if(pos_prob < 0.5)
  {
    predicted_value = 1
  }else{
    predicted_value = 0
  }
  if(predicted_value!=CancelledFlights[i,]$Canceled) {
    error_vec[i] = 1
  }
}
print('The LDA MSE is : ')
print(mean(error_vec))


summary(glm.fit)

# Input a dataframe with same structure 
predict.flightdelays = function(CancelledFlights) {
  for (i in 1:dim(CancelledFlights)[1]) {
    pos_prob = predict(lda.fit, CancelledFlights[i,])$posterior[, 1]
  }
  
  if (pos_prob < 0.5)
  {
    print(" There is a high probability of Cancellation")
  } else{
    print(" There is a low probability of Cancellation")
  }
  
}
  








