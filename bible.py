############ Sistema de gerenciamento de Livros ########################
############ Pedro L. Lourenço #############################

# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

class Livro:

    # As entradas solicitadas
    def __init__(self,titulo,autor,genero,quantidade):

        self.title = titulo
        self.aut = autor
        self.gen = genero
        self.cont = quantidade

    # Registro de novo livro
    def newbook(self):

        self.title = input('Digite o nome do novo livro para cadastro: ')
        self.aut = input('Digite o nome do autor do novo livro: ')
        self.gen = input('Digite o gênero literário: ')
        self.cont = int(input('Digite a quantidade disponível: '))

    # Confirmação de registro

    def show(self):

        print(f'{self.title}|{self.gen}|{self.aut}|{self.cont} Exemplares')

def save(lista):
    with open('livros.dat','w', encoding='utf-8') as f:
        for livro in lista:
            linha = f'{livro.title};{livro.aut};{livro.gen};{livro.cont}\n'
            f.write(linha)

def charge():

    lista = []
    try:
        with open('livros.dat','r', encoding='utf-8') as f:
            for linha in f:
                    titulo,autor,genero,quant = linha.strip().split(';')
                    lista.append(Livro(titulo,autor,genero,int(quant)))
    except FileNotFoundError:
        print('Biblioteca Vazia. Registre novos livros.')
    
    return lista

def biblioteca(lista):
    print('Livros disponíveis:\n')

    for i,livro in enumerate(lista):
        print(f'{i}|{livro.title}|{livro.gen} - {livro.cont} unidades disponíveis\n')

def retire(lista):

    biblioteca(lista)

    try:

        i = int(input('Escolha o índice do livro:'))

        print(f'Livro {lista[i]} está sendo retirado')

        if lista[i].cont > 0:
            lista[i].cont -= 1
            print('Exemplar retirado.')
        else:
            print('Exemplares indispooníveis.')
    
    except:
        print('Tente novamente.')

def menu():
    livros = charge()

    while True:
        print("\n========= MENU =========")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Retirar livro")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == '1':
            novo = Livro('', '', '', 0)
            novo.newbook()
            livros.append(novo)
            save(livros)

        elif op == '2':
            biblioteca(livros)

        elif op == '3':
            retire(livros)
            save(livros)


        elif op == '0':
            save(livros)
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

menu()




