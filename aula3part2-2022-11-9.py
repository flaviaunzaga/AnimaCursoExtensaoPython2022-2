#criação de funções

preco = 1999.90

imposto = preco * 0.05
print(imposto)

#função de calcular imposto de 5% e retorna a quem pediu 

def calcular_imposto(preco_produto):
  imposto = preco_produto *0.07
  return imposto


preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui é com a função (7%): {imposto}")

#variavel local x global
print(preco)#??
preco_produto = 100
print(preco_produto)#?

#calculo de imposto com aliquota 7%
valores = [1.99, 24.50, 78.27, 1515.5]
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 7)}")

#E se agora o imposto for 10%?
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")