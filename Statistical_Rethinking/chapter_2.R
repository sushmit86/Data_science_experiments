## R code 2.1
ways <- c( 0 , 3 , 8 , 9 , 0 )
ways/sum(ways)

## R code 2.2
dbinom( 6 , size=9 , prob=0.5 )

## R code 2.3
# define grid
<<<<<<< HEAD
p_grid <- seq( from=0 , to=1 , length.out=20 )
=======
p_grid <- seq( from=0 , to=1 , length.out=20)
>>>>>>> d2b19e41c4906ee01f451a8c47b9a1fdbc2e692e

# define prior
prior <- rep( 1 , 20 )

# compute likelihood at each value in grid
likelihood <- dbinom( 6 , size=9 , prob=p_grid )

# compute product of likelihood and prior
unstd.posterior <- likelihood * prior

# standardize the posterior, so it sums to 1
posterior <- unstd.posterior / sum(unstd.posterior)

## R code 2.4
plot( p_grid , posterior , type="b" ,
      xlab="probability of water" , ylab="posterior probability" )
mtext( "20 points" )


## R code 2.5
prior <- ifelse( p_grid < 0.5 , 0 , 1 )
prior <- exp( -5*abs( p_grid - 0.5 ) )

## R code 2.6
library(rethinking)
globe.qa <- map(
  alist(
<<<<<<< HEAD
    w ~ dbinom(9,p) ,  # binomial likelihood
    p ~ dunif(0,1)     # uniform prior
  ) ,
  data=list(w=6) )
=======
    w ~ dbinom(36,p) ,  # binomial likelihood
    p ~ dunif(0,1)     # uniform prior
  ) ,
  data=list(w=24) )
>>>>>>> d2b19e41c4906ee01f451a8c47b9a1fdbc2e692e

# display summary of quadratic approximation
precis( globe.qa )

