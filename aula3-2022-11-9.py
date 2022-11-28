print("Ola")

contador = 1 

#estrutura de repetição
while(contador <=10):
  print (contador)
  contador = contador+1


#contador += 1 tb funciona
# Laço for 
fruta = "morango"
print (fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "maça"

#lista
#linguagem começa contando em 0
frutas =["morango", "melancia", "laranja"]

#para exibir a terceira fruta
print(frutas[2])

#exibir quantas frutas tem na lista
print(len(frutas)) #length

#incluir fruta nova
frutas.append("manga")
print(len(frutas))
print(frutas)

i = 0
while(i<4):
  print(frutas[i])
  i=i+1

#poderia ser com len tb. No caso acima, caso eu acrescentasse uma nova fruta ele não mostraria pois eu precisaria atualizar o <4
  
#while(i<len(frutas)):
  #print(frutas[i])
  #i=i+1
print("Exemplo de frutas com FOR")
for fruta in frutas:
  print(fruta)
