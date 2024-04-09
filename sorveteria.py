
print('Bem-vindo a sorveteria!')

#VARIÁVEL QUE DEMOSTRA AO CLIENTE OS PEDIDOS DISPONIVEIS, E RESPECTIVAS CARACTERISTICAS#
print('.......................CARDÁPIO..........................')
print('|CÓDICO | DESCRIÇÃO  | Tamanho P | Tamanho M | Tamanho G|')
print('|       |            | 500 ml    | 1000 ml   | 2000 ml  |')
print('|.......|............|...........|...........|..........|')
print('|  TR   | Sabor      | R$ 6,00   | R$ 10,00  | R$ 18,00 |')
print('|.......| Tradicional|...........|...........|..........|')
print('|  ES   | Sabor      | R$ 7,00   | R$ 12,00  | R$ 21,00 |')
print('|.......| Especial   |...........|...........|..........|')
print('|  PR   | Sabor      | R$ 8,00   | R$ 14,00  | R$ 24,00 |')
print('|       | Premium    |           |           |          |')
print('.........................................................')

#DEFINIDO AS VARIÁVEIS (=)
#PEDINDO OS DADOS DO PRODUTO

acumulador = 0

#VARIAVEL QUE PEDE AO CLIENTE PARA COLOCAR, CÓDICO E TAMANHO DO PRODUTO#
while True:
      tamanho = input('Escolha o tamanho do pote de sorvete desejado(P|M|G):')
      tamanho = tamanho.upper() #RESOLVE O PROBLEMA DE DIGITAR 'P' e 'p'...#
      if tamanho !='P' and tamanho !='M' and tamanho !='G':
         print('TAMANHO INVÁLIDO!!!')
         continue #SE USUARIO DIGITAR ALGO INVÁLIDO, VOLTA PARA O INICIO DO WHILE#

      codico = input('Escolha o códico do sorvete(TR|ES|PR):')
      codico = codico.upper() #RESOLVE O PROBLEMA DE DIGITAR 'TR' e 'tr'...#
      if codico !='TR' and codico !='ES' and codico !='PR':
         print('CÓDICO INVÁLIDO!!!')
         continue #SE USUARIO DIGITAR ALGO INVÁLIDO, VOLTA PARA O INICIO DO WHILE#

      if codico =='TR' and tamanho =='P':
         print('Você escolheu sabor TRADICIONAL - P de R$ 6,00')
         acumulador = acumulador + 6  #PEGA O VALOR QUE TINHA NO ACUMALADOR E SOMA COM 6#
         print('..............................................')

      elif codico =='TR' and tamanho =='M':
         print('Você escolheu sabor TRADICIONAL - M de R$ 10,00')
         acumulador = acumulador + 10  #PEGA O VALOR QUE TINHA NO ACUMALADOR E SOMA COM 10#
         print('...............................................')

      elif codico =='TR' and tamanho =='G':
         print('Você escolheu sabor TRADICIONAL - G de R$ 18,00')
         acumulador = acumulador + 18  #PEGA O VALOR QUE TINHA NO ACUMALADOR E SOMA COM 18#
         print('...............................................')

      elif codico =='ES' and tamanho =='P':
         print('Você escolheu sabor Especial - P de R$ 7,00 ')
         acumulador = acumulador + 7  #PEGA O VALOR QUE TINHA NO ACUMALADOR E SOMA COM 7#
         print('...............................................')

      elif codico =='ES' and tamanho =='M':
         print('Você escolheu sabor ESPECIAL - M R$ 12,00')
         acumulador = acumulador + 12  #PEGA O VALOR QUE TINHA NO ACUMALADOR E SOMA COM 12#
         print('...............................................')

      elif codico =='ES' and tamanho =='G':
         print('Você escolheu sabor ESPECIAL - G de R$ 21,00')
         acumulador = acumulador + 21  #PEGA O VALOR QUE TINHA NO ACUMALADOR E SOMA COM 21#
         print('...............................................')

      elif codico =='PR' and tamanho =='P':
         print('Você escolheu sabor PREMIUM - P de R$ 8,00 ')
         acumulador = acumulador + 8  #PEGA O VALOR QUE TINHA NO ACUMALADOR E SOMA COM 8#
         print('...............................................')

      elif codico =='PR' and tamanho =='M':
         print('Você escolheu sabor PREMIUM - M de R$ 14,00')
         acumulador = acumulador + 14  #PEGA O VALOR QUE TINHA NO ACUMALADOR E SOMA COM 14#
         print('...............................................')

      elif codico =='PR' and tamanho =='G':
         print('Você escolheu sabor PREMIUM G de R$ 24,00')
         acumulador = acumulador + 24  #PEGA O VALOR QUE TINHA NO ACUMALADOR E SOMA COM 24#
         print('...............................................')

      pedir_mais = input('Deseja pedir mais algum sabor(S/N):')
      pedir_mais = pedir_mais.upper() #RESOLVE O PROBLEMA DE DIGITAR 'S' e 's' ou 'N' e 'n'#
      print("")

      if pedir_mais == 'S': #SE O CLIENTE QUISER PEDIR MAIS ALGUM SABOR DIGITAR 'S', SE 'N' O VALOR A SER PAGO SERÁ SOLTO
        continue
      else:
        print('Valor total a ser pago: R${:.2f}' .format(acumulador))
        break


