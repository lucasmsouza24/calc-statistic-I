#1
p <- 200000
n <- 20000
set.seed(1234)
idade <- abs(round(rnorm(n, 35, 7),0)) 

#2
altura <- abs(round(rnorm(n, 1.50, 0.1), 2))

#3
peso <- abs(round(rnorm(n, 55, 4), 2)) 

#4 
imc <- round(peso/altura^2, 2)

#5
salario <- abs(round(rnorm(n, 3000, 400), 2))

#6
pop.carros <- rep(c(0,1,2,3), p)
carros<-sample(pop.carros,n) 

#7
set.seed(1)
pop.filhos<-rep(c(0,1,2),p) 
filhos <- sample(pop.filhos, n) 


#8
pop.escolaridade <- rep(c(0, 1, 2, 3, 4, 5, 6), p)
set.seed(1234)
escolaridade.temp <- sample(pop.escolaridade, n)
escolaridade <- factor(escolaridade.temp,
                       levels = c(0, 1, 2, 3, 4, 5, 6),
                       labels = c("Analfabeto", "1º Grau", "2º Grau", "3º Grau",
                                 "Mestrado", "Doutorado", "PósDoc"), 
                       ordered = TRUE
                       ) 
rm(pop.escolaridade, escolaridade.temp) 
# str(escolaridade) 
barplot(table(escolaridade), col = rainbow(10))

#9
set.seed(1234)
fumante.n <- rbinom(n, 1, .40)
fumante.f <- factor(fumante.n,
                      levels = c(0, 1),
                      labels = c("não", "sim"),
                      ordered = TRUE)
# str(fumante.f)

#10
pop.sexo <- rep(c(1, 2), p)
set.seed(1234)
sexo.temp <- sample(pop.sexo, n)
sexo <- factor(sexo.temp,
                 levels = c(1, 2),
                 labels = c("M", "F"),
                 ordered = TRUE)
rm(pop.sexo, sexo.temp) 
# print(sexo)
barplot(table(sexo), col = rainbow(2))

# 11
pop.profissao <- rep(0:2, p)
set.seed(1234)
profissao.temp <- sample(pop.profissao, n)
profissao <- factor(
  profissao.temp,
  levels = c(0, 1, 2),
  labels = c("Humanas", "Exatas", "Biológicas"),
    ordered = TRUE
)

rm(profissao.temp, pop.profissao)

barplot(table(profissao), col = rainbow(3))
#print(summary(profissao))
str(profissao)

#12 
df <- data.frame(
  id = 1:n,
  altura, 
  peso,
  imc,
  sexo,
  escolaridade,
  profissao,
  fumante.f,
  fumante.n,
  salario,
  carros,
  filhos
)

write.table(df, file = "projeto01.csv", sep = ",", col.names = TRUE, fileEncoding = "UTF-8")
