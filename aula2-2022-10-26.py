#comando input () : permitir que o usuario digite

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
dobro = idade*2
sexo = input("Qual seu genero? ")

#saída
print(f"Boa noite, seu nome é {nome}")
print (f"Sua idade é {idade} anos")
print ("O dobro da sua idade é {}".format(dobro))

#estrutura condicional - if
if idade >=18 and sexo =="masculino":
  print("Você é maior de idade, e precisa se alistar no exército!")

else: 
  print("Você ainda é jovem ):")
  #else atende criterios que forem ao contrario da condição do if


    
