#criar uma lista vazia
lista = []

#Criar uma lista com tamnaho 10
lista2 = [""]*10

#Adicionar m elemnto na lista
lista.append(5)
lista.append(18)
lista.append(1)
lista.append(8)
lista.append(15)
lista.append(20)
lista.append(12)


#Alterar valor da lista
lista[3] = 44
print("Resultado da lista;", lista)

#Calcular tamanho da lista

t = len(lista)
i = 0

while i < t:

    #print("Na posição" , i, "tem o valor", lista[i])
    print("Na posição {} tem o valor {}.".format(i, lista[i]))
    i+= 1

print("=========\n")

#Usando o for da maneira foreach
for x in lista:
    print("Valor da lista", x)

print("=========\n")

#Uso do for normal
#len calcula o tamanho da lista cria uma sequencia numerica
for i in range(len(lista)):
    print("Na posição {} tem o valor {}.".format(i, lista[i]))

#Criação de funções

def dobro(num):
    d = num * 2
    print("O dobro de {} é {}.".format(num, d))
    return d, num

a, b = dobro(5)
print("O retornos de {} é {}.".format(a, b))
