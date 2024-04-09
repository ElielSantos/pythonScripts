
print('Bem-vindo a Loja!)
#IMPRIME AS BOAS VINDAS DO PROGRAMA

produto1 = float(input('Entre com o valor do produto:'))
#VARIAVEL DO VALOR DO PRODUTO

quantidade2 = int(input('Entre com a quantidade de produtos:'))
#VARIAVEL DE ENTRADA PARA A QUANTIDADE DE PRODUTO

frete3 = 0
#RECEBE O VALOR DO FRETE, DEPENDENDO DA QUANTIDADE DE PRODUTOS INSERIDOS

if quantidade2 <11:
   frete3 = 30

elif quantidade2 <101:
   frete3 = 60

elif quantidade2 <1001:
   frete3 = 120

else:
   frete3 = 240

valorParcial = float(produto1 * quantidade2)
#DEFINE A VARIAVEL valorParcial COM O VALOR PARCIAL DA MULTIPLICAÇÃO ENTRE O produto * A QUANTIDADE

valorTotal = float(valorParcial + frete3)
#DEFINE A VARIAVEL valorTotal COM O VALOR TOTAL DA SOMA ENTRE O valorParcial + O frete3

print('O VALOR SEM FRETE É: R${:.2f}'.format(valorParcial))  #iIMPRIME O valorParcial FORMATADO
#COM DUAS CASAS DECIMAIS APÓS O PONTO

print('COM DESCONTO FICOU: R${:.2f} '.format(valorTotal) + '(FRETE DE R$ {:.2f})'.format(frete3))
#IMPRIME O valorTotal FORMATADO COM DUAS CASAS DECIIMAIS APÓS O PONTO

print('OBRIGADO PELA PREFERÊNCIA!')
#FIM DO PROGRAMA


