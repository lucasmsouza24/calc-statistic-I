p <- 200000
n <- 20000

set.seed(1)

idade <- abs(round(rnorm(n, 30, 15)))
altura <- abs(rnorm(n, 1.75, 0.05))   
peso <- abs(rnorm(n, 75, 5))

imc <- c()
for(i in 1:n) {
  imctemp <- peso[i] / (altura[i] ** 2)
  imc <- c(imc, round(imctemp, 1))
}

salario <- abs(rnorm(n, 3000, 300))

hist(salario)