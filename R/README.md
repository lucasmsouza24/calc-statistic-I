# R

- [Download](#download)
- [Introdução](#introdução)
- [Média, mediana e moda](#média-mediana-e-moda)
- [Boxplot](#boxplot)
- [Gerando Imagens](#gerando-imagens)
- [Variância e Desvio Padrão](#variância-e-desvio-padrão)

## Download

[Clique aqui](https://cran.r-project.org/bin/windows/base/) para acessar a página de download.

## Introdução

### Criando uma variável

~~~r
varname <- 2
~~~

### Listas

c() é um método que retorna uma lista contendo os argumentos passados.
~~~r
lista <- c(1, 2, 2, 3, 5)
~~~

Operações podem ser realizadas em cada valor de uma lista, retornando uma nova lista com os resultados.

~~~r
lista * 3
~~~

### histogramas

Abre uma janela com um histograma de acordo com os valores passados.

~~~r
hist(c(1, 2, 3, 4))
~~~

ou

~~~r
hist(lista)
~~~

> um dado do tipo lista deve ser passado como argumento

## Média, mediana e moda

retorna a média dos valores da lista

~~~r
mean(lista)
~~~

retorna a mediana dos valores da lista

~~~r
median(lista)
~~~

exibe quartis, mediana e média de uma lista

~~~r
summary(lista)
~~~

realiza um teste para descobrir se a lista é uma distribuição normal

~~~r
shapiro.test(lista)
~~~

> se o valor de p-value for menor que 0.05, não é uma distribuição normal

## Boxplot

Boxplot é um gráfico que exibe a amplitude da distribuição.

~~~r
boxplot(lista)
~~~

> a função boxplot por padrão já limpa os outliers

## Gerando Imagens

~~~r
#definindo local de armazenamento da imagem e seu tamanho
png(file="c://users//lucas//desktop//boxplot.png", width=700, height=700)

#realizando comando que gera a imagem
boxplot(list)

#finalizando geração de imagem
dev.off()
~~~

## Variância e Desvio Padrão

retorna variância de uma distribuição

~~~r
var(lista)
~~~

retorna desvio padrão de uma distribuição

~~~r
sd(lista)
~~~
