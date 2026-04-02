
dados <- read.table("livros.dat",
                    sep = ";",
                    header = FALSE,
                    stringsAsFactors = FALSE,
                    fileEncoding = "UTF-8")


colnames(dados) <- c("Título", "Autor", "Gênero Literário", "Quantidade")


dados$Quantidade <- as.numeric(dados$Quantidade)


soma_genero <- tapply(dados$Quantidade,
                      dados$`Gênero Literário`,
                      sum)


soma_genero <- sort(soma_genero, decreasing = TRUE)


barplot(soma_genero,
        col = "#dc7425",   
        border = "black",
        main = "Quantidade de Livros por Gênero",
        xlab = "Gênero Literário",
        ylab = "Total de Livros",
        las = 2,       
        cex.names = 0.8 
)


valores <- barplot(soma_genero, plot = FALSE)

text(x = valores,
     y = soma_genero,
     label = soma_genero,
     pos = 3,  
     cex = 0.8)