#comando input () : permitir que o usuario digite

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
dobro = idade*2
#saída

print(f"Boa noite, seu nome é {nome}")
print (f"Sua idade é {idade} anos")
print ("O dobro da sua idade é {}".format(dobro))
