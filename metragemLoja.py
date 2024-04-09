

#INICIO DA FUNÇÃO DA METRAGEM()
def metragemLimpeza():
    print('..................MENU 1-3 METRAGEM DE LIMPEZA......................')
    metrageM = 0
    while True:
        try:
          metrageM = int(input('Entre com a metragem da casa(m²):'))

        ## Verifica se a metragem esta dentro da faixa com a qual a empresa trabalha
          if 30 <=metrageM <= 300:
            print('É necessário contratar 1 pessoa para limpeza!')
            return metrageM * 0.3 + 60

          elif 300 <= metrageM <= 700:
            print('É necessário contratar 2 pessoas para limpeza!')
            return metrageM * 0.5 + 120

          else:
            print('!!Não aceitamos casas com metragem menor que 30m² e maior que 700 m²!!')
        except ValueError: #CASO O USUÁRIO DIGITE A LETRA C OU 0.30 POR EXEMPLO
            print('!!Pare de digitar valores não inteiros!!')
#FIM DA FUNÇAO DA METRAGEM()

#INICIO DA FUNÇÃO TIPOLIMPEZA()
def tipoLimpeza():
    print('....................MENU 2-3 TIPOS DE LIMPEZA......................')
    while True:
        tipoT = input ('Qual o tipo de limpeza será feita(B/C):\n'+
                     '|B – Básica - Indicada para sujeiras semanais ou quinzenais       |\n'+
                     '|C – Completa - Indicada para sujeiras antigas e/ou não rotineiras|\n'+
                      '>>>')

        tipoT = tipoT.upper() #RESOLVE O PROBLEMA DE DIGITAR 'B' e 'b'and 'C' e 'c'#
        tipoT = tipoT.strip()

        if tipoT == 'B':
          print('.....!!-VOCÊ ESCOLHEU LIMPEZA BÁSICA-!!.....')
          return 1.00

        elif tipoT == 'C':
          print('.....!!-VOCÊ ESCOLHEU LIMPEZA COMPLETA-!!.....')
          return 1.30

        else:
            print('!!OPÇÃO INVALIDA!!')
            continue #RETORNA PARA A PERGUNTA
 #FIM DA FUNÇAO TIPO DE LIMPEZA()

#INICIO DA ADICIONAL DA LIMPEZA()
def adicionaLimpeza():
    print('..................MENU 2-3 ADICIONAIS DE LIMPEZA....................')
    acumulador = 0
    while True: #OPÇÕES QUE VAI APARECER PARA O CLIENTE, CASO DESEJE ADICIONAR MAIS ITENS#
        adicionaL= input('|0-Não desejo mais nada (encerrar)| R$ 0,00 |\n'+
                         '|1-Passar 10 peças de roupas      | R$ 10.00|\n'+
                         '|2-Limpeza de 1 Forno/Micro-ondas | R$ 12,00|\n'+
                         '|3-Limpeza de 1 Geladeira/Freezer | R$ 20,00|\n'+
                         '|Deseja mais algum adicional?\n'+
                         ' >>> ')

        if adicionaL == '0':
         return acumulador

        elif adicionaL == '1':
         acumulador = acumulador + 5
         continue #VOLTA PARA O INICO DO WHILE TRUE#

        elif adicionaL == '2':
         acumulador = acumulador + 6
         continue #VOLTA PARA O INICO DO WHILE TRUE#

        elif adicionaL == '3':
         acumulador = acumulador + 7
         continue #VOLTA PARA O INICO DO WHILE TRUE#

        else:
            print('Você não digitou uma opção válida!')
            return adicionaL
#FIM DA FUNÇÃO ADICIONAL DA LIMPEZA()

#INICIO DO MAIN
print('..........Bem-vindo ao programa de Metragem............')

#EXECUÇÕES DAS FUNÇÕES PARA AMARZENAR SAÍDAS
metragem = metragemLimpeza()
tipo = tipoLimpeza()
adicional = adicionaLimpeza()

#CALCULA E MOSTRA O VALOR TOTAL
total = (metragem * tipo and adicional)
print('Valor a ser pago é:(metragem = R${:.2f} * tipo= R${:.2f} + adicional= R${:.2f})'
.format(total,metragem,tipo,adicional))

