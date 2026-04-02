livros_dados = [
    ("Sombras de Orion", "Lucas Valente", "Ficção Científica", 5),
    ("O Código de Ébano", "Marina Torres", "Mistério", 3),
    ("Corações em Chamas", "Rafael Duarte", "Romance", 8),
    ("A Espada do Norte", "Helena Braga", "Fantasia", 6),
    ("Ecos do Passado", "André Farias", "Drama", 4),

    ("Galáxia Perdida", "Renato Silveira", "Ficção Científica", 7),
    ("O Enigma da Torre", "Patrícia Nunes", "Mistério", 2),
    ("Amor em Verona", "Clara Mendes", "Romance", 10),
    ("Reino das Cinzas", "Bruno Cavalcante", "Fantasia", 5),
    ("Vidas Cruzadas", "Juliana Pires", "Drama", 6),

    ("Horizonte Azul", "Eduardo Lima", "Ficção Científica", 9),
    ("Segredos Ocultos", "Fernanda Rocha", "Mistério", 3),
    ("Entre Dois Mundos", "Diego Alves", "Romance", 4),
    ("O Último Dragão", "Camila Freitas", "Fantasia", 7),
    ("Silêncio da Alma", "Marcelo Teixeira", "Drama", 2),

    ("Planeta Sombrio", "Thiago Moreira", "Ficção Científica", 6),
    ("O Caso do Relógio", "Beatriz Cardoso", "Mistério", 5),
    ("Paixão Proibida", "Larissa Gonçalves", "Romance", 8),
    ("A Coroa de Ferro", "Gustavo Ribeiro", "Fantasia", 4),
    ("Destinos Partidos", "Sabrina Lopes", "Drama", 3),

    ("Estrelas Caídas", "Vinícius Martins", "Ficção Científica", 5),
    ("Noite sem Fim", "Aline Barros", "Mistério", 6),
    ("Doce Ilusão", "Paulo Henrique", "Romance", 7),
    ("Guardião das Runas", "Felipe Aragão", "Fantasia", 2),
    ("Caminhos da Vida", "Tatiane Souza", "Drama", 9),

    ("Universo Infinito", "Igor Santana", "Ficção Científica", 4),
    ("O Mistério do Lago", "Vanessa Ribeiro", "Mistério", 3),
    ("Amor e Destino", "Ricardo Nogueira", "Romance", 6),
    ("A Profecia Antiga", "Daniel Castro", "Fantasia", 8),
    ("Fragmentos de Nós", "Renata Dias", "Drama", 5),

    ("Além das Estrelas", "Leonardo Campos", "Ficção Científica", 7),
    ("Código Mortal", "Bianca Melo", "Mistério", 4),
    ("Para Sempre Você", "Fábio Rezende", "Romance", 10),
    ("O Trono Esquecido", "Arthur Peixoto", "Fantasia", 3),
    ("Laços Eternos", "Carolina Batista", "Drama", 6),

    ("Dimensão Zero", "Rodrigo Pinto", "Ficção Científica", 5),
    ("O Segredo da Chave", "Priscila Andrade", "Mistério", 2),
    ("Amores Perdidos", "Julio César", "Romance", 7),
    ("A Lenda de Eldor", "Márcio Tavares", "Fantasia", 4),
    ("Dias de Tempestade", "Elaine Duarte", "Drama", 8),
]

with open('livros.dat', 'w', encoding='utf-8') as f:
    for livro in livros_dados:
        linha = f"{livro[0]};{livro[1]};{livro[2]};{livro[3]}\n"
        f.write(linha)
