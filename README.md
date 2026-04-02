# Sistema de Gerenciamento de Livros

Projeto desenvolvido utilizando **Python e R** com o objetivo de criar um sistema simples de gerenciamento de biblioteca, incluindo armazenamento de dados e visualização gráfica.

---

## Funcionalidades

* Cadastro de novos livros
* Listagem de livros disponíveis
* Retirada de exemplares (controle de estoque)
* Salvamento automático em arquivo `.dat`
* Carregamento automático dos dados
* Análise e visualização gráfica por gênero literário

---

## Estrutura do Projeto

O projeto é composto por um sistema principal em Python responsável pela manipulação dos dados e um script em R para análise e visualização.

Arquivos principais:

* Sistema principal em Python
* Arquivo de dados (`livros.dat`)
* Script em R para geração de gráficos

---

##  Parte 1 — Sistema em Python

O sistema foi construído com base em Programação Orientada a Objetos (POO), utilizando uma classe para representar os livros.

Cada livro possui:

* Título
* Autor
* Gênero literário
* Quantidade disponível

O sistema permite ao usuário interagir por meio de um menu no terminal, possibilitando:

* Adicionar novos livros
* Visualizar a lista completa
* Retirar exemplares (com atualização automática do estoque)

Os dados são armazenados em um arquivo `.dat`, garantindo persistência entre execuções do programa.

---

##  Banco de Dados

Os dados são armazenados em formato texto, onde cada linha representa um livro com seus respectivos atributos separados por ponto e vírgula.

Esse formato simples permite fácil leitura tanto pelo Python quanto pelo R.

---

## Parte 2 — Análise em R

A linguagem R foi utilizada para realizar a análise dos dados armazenados.

O processo inclui:

* Leitura do arquivo `.dat`
* Organização dos dados em formato tabular
* Conversão dos valores numéricos
* Agrupamento das quantidades por gênero literário

A visualização foi feita por meio de um gráfico de barras, permitindo comparar a quantidade total de livros em cada gênero.

---

##  Execução do Projeto

O sistema em Python deve ser executado para gerenciamento da biblioteca, enquanto o script em R pode ser utilizado para gerar os gráficos a partir dos dados armazenados.


---

## Aprendizados

Este projeto proporcionou experiência prática em:

* Manipulação de arquivos em Python
* Programação Orientada a Objetos
* Estruturas de dados
* Integração entre linguagens (Python e R)
* Visualização de dados
* Tratamento de erros

---

##  Possíveis Melhorias

* Implementação de busca por título
* Remoção de livros do sistema
* Controle de empréstimos por usuário
* Integração com banco de dados (SQLite)
* Criação de interface gráfica
* Uso de bibliotecas avançadas de visualização

---

## Autor

Pedro L. Lourenço

---

## Status do Projeto

Funcional e em evolução, com potencial para expansão e melhorias.  
