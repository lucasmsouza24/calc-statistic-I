# setando obsevacoes, amostras, media e desvio padrao.
observacoes <- 20000
amostra <- 20000
media <- 37
desvio_padrao <- 7

# settando seed de geração pseudorandomica
set.seed(1234)

# randomizando valores
idade <- abs(round(rnorm(amostra, media, desvio_padrao), 0))

# visualizando distribuição normal
hist(idade)
