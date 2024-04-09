
#..........INICIO DAS VARIÁVEIS GLOBAIS..........
listaFuncionarios=[]
codicoFuncionario=0
#..........FIM DAS VARIÁVEIS GLOBAIS..........

#..........INICIO DE CADASTRAR FUNCIONÁRIO..........
def cadastrarFuncionario(codico):
   print('Bem-vindo ao menu de cadastrar funcionário:')
   print('Escolha o CÓDICO do funcionário {}'.format(codico))
   nome=input('Escolha um NOME:')
   setor=input('Escolha um SETOR:')
   salario=float(input('Escolha o SALÁRIO(R$):'))
   dicionarioFuncionario ={'codico' : codico,
                           'nome'   : nome,
                           'setor'  : setor,
                           'salario': salario,}
   listaFuncionarios.append(dicionarioFuncionario.copy())
#..........FIM DE CADASTRAR FUNCIONÁRIO..........

#..........INICIO DE CONSULTAR FUNCIONÁRIO..........
def consultarFuncionario():
   print('Bem-vindo ao menu de consultar funcionário:')
   while True:
    #OPÇÕES DISPONÍVEIS PARA O USUARIO ESCOLHER#
    opcaoConsultar=input('Escolha a opção desejada:\n'+
                       '1-Consultar TODOS os Funcionários:\n'+
                       '2-Consultar Funcionário por ID:\n'+
                       '3-Consultar Funcionário(s) por SETOR:\n'+
                       '4-Retornar\n'+
                       '>>>')

    if opcaoConsultar=='1':
       print('Escolheu opção consultar TODOS os funcionário!')
       for funcionario in listaFuncionarios:#FUNCIONARIO VAI VARRER TODA LISTA DE FUNCIONÁRIOS#
         print('............................')
         for key, value in funcionario.items():#VARRER TODOS OS CONJUNTOS CHAVES E VALOR DO DICIONARIO FUNCIONÁRIO#
           print('{}: {}'.format(key, value))
         print('............................')

    elif opcaoConsultar == '2':
       print('Escolheu opção consultar funcionário por iD!')
       valorDesejado = float(input('Escolha o iD do funcionário:'))
       for funcionario in listaFuncionarios:
         if funcionario['codico']== valorDesejado:#O VALOR DE CAMPO CÓDICO DESSE DICIONÁRIO É IGUAL A ESSE#
           print('............................')
           for key, value in funcionario.items():#VARRER TODOS OS CONJUNTOS CHAVES E VALOR DO DICIONARIO FUNCIONÁRIO#
            print('{}: {}'.format(key, value))
           print('............................')

    elif opcaoConsultar == '3':
       print('Escolheu opção consultar funcionário(s) por SETOR!')
       valorDesejado = (input('Escolha o SETOR do funcionário:'))
       for funcionario in listaFuncionarios:
        if funcionario['setor'] == valorDesejado:#O VALOR DE CAMPO CÓDICO DESSE DICIONÁRIO É IGUAL A ESSE#
         print('............................')
         for key, value in funcionario.items():#VARRER TODOS OS CONJUNTOS CHAVES E VALOR DO DICIONARIO FUNCIONÁRIO#
           print('{}: {}'.format(key, value))
         print('............................')
    elif opcaoConsultar =='4':
      return

    else:
      print('Digite somente uma das opções do MENU')
      continue
#..........FIM DE CONSULTAR FUNCIONÁRIO..........

#..........INICIO DE REMOVER FUNCIONÁRIO..........
def removerFuncionario():
   print('Bem-vindo ao menu Remover funcionário:')
   valorDesejado = int(input('Escolha o iD do funcionário a ser removido:'))
   for funcionario in listaFuncionarios:
    if funcionario['codico']==valorDesejado:
       listaFuncionarios.remove(funcionario)
       print('!!FUNCIONÁRIO REMOVIDO!!')
       print('................................')
#..........FIM DE REMOVER FUNCIONÁRIO..........

#..........INICIO DO MAIN..........
print('Bem-vindo ao controle de funcionários da empresa LTDA')
while True:
  #OPÇÕES DISPONÍVEIS PARA O USUARIO ESCOLHER#
  opcaoMenu=input('Escolha a opção desejada:\n'+
                       '1-Cadastrar Funcionário:\n'+
                       '2-Consultar Funcionário(s):\n'+
                       '3-Remover Funcionário:\n'+
                       '4-Sair\n'+
                       '>>>')
  if opcaoMenu =='1':
     codicoFuncionario = codicoFuncionario + 1
     cadastrarFuncionario(codicoFuncionario)

  elif opcaoMenu == '2':
     consultarFuncionario()

  elif opcaoMenu == '3':
     removerFuncionario()

  elif opcaoMenu == '4':
     print('Programa finalizado!')
     break #FINALIZA O PROGRAMA, CASO USUÁRIO DIGITE '4'

  else:
     print('Digite somente uma das opções do MENU')
     continue
#..........FIM DO MAIN.........
