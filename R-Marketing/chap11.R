theMatrix <- matrix(1:9, nrow =3)
apply(theMatrix,2,sum)
rowSums(theMatrix)
colSums(theMatrix)
theMatrix[2,1]  <- NA
apply(theMatrix,2,sum,na.rm = TRUE)