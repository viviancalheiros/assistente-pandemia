#Entrada
def loginsenha():
    login = input('Login: ')
    senha = input('Senha: ')
    return login, senha

estados_no_amarelo = ['Amazonas', 'Roraima', 'Amapá', 'Pará', 'Mato Grosso', 'Mato Grosso do Sul', 'Paraná', 'Santa Catarina', 'Rio Grande do Sul', 'Rio de Janeiro', 'Espírito Santo', 'Minas Gerais', 'Goiás', 'Bahia', 'Tocantins', 'Pernambuco', 'Piauí', 'Maranhão', 'Distrito Federal']
estados_no_azul = ['Acre', 'Rondônia', 'Ceará', 'Rio Grande do Norte', 'Paraíba', 'Alagoas', 'Sergipe', 'São Paulo']

idade = 1

login = 1
senha = 1 
opçoes = '''Opções:
1 - Fazer cadastro
2 - Fazer login 
3 - Verificar situação de contaminação no seu estado
4 - Verificar situação da vacinação no Brasil
5 - Sair'''
opçao = 1

while opçao != 5:
    print()
    print(opçoes)
    opçao = int(input('Digite a opção escolhida: '))
    if opçao == 1:
     login = input('Crie um login para cadastro (apenas com letras e/ou números, sem espaços): \n')
     senha = input('Crie também uma senha: \n')
     with open('Dados_usuario', 'a') as file:
         dados_usuario = open ('Dados_usuario', 'a')
         dados_usuario.writelines(login + '\n') 
         dados_usuario.writelines(str(senha) + '\n') 
         dados_usuario.close()
     print('Cadastro realizado com sucesso!')
     iniciar = int(input('Iniciar uso do app?\n1 - Sim\n2 - Não\n'))
     if iniciar == 2:
        continue
    if opçao == 2:
        arq = open ('Dados_usuario', 'r')
        login, senha = loginsenha()
        registrados = arq.readlines()
        if  login + '\n' not in registrados:
            print('Cadastro não realizado.')
            continue
        while login + '\n' in registrados and senha + '\n' not in registrados:
          print ('Login ou senha incorreto(a). Digite novamente.\n')
          login, senha = loginsenha()
        if login + '\n' in registrados and senha + '\n' in registrados:
            print('Login e senha corretos.')
            iniciar = int(input('Iniciar uso do app?\n1 - Sim\n2 - Não\n'))
        arq.close()
    if opçao == 3:
        estado = input('Digite aqui o estado em que você mora:\n')
        if estado in (estados_no_amarelo):       
            print (f'O estado: {estado}, está na fase amarela.')  
        if estado in (estados_no_azul):
            print(f'O estado: {estado}, está na fase azul.')
            continue
    if opçao == 4:
        print('Mais de 33 milhões de pessoas estão totalmente vacinadas, isso corresponde a 15,8% da população brasileira.')
        print('Mais de 91 milhões de pessoas já receberam a primeira dose.')
        print('Já foram aplicadas mais de 121 milhões de doses no Brasil.')
        print('#VacinaSim')
        continue

    trabalho = 1
    horas_estudo = 0
    
    if opçao == 5:
      iniciar = 2
      break 
    
    if iniciar == 1:
      print('Digite abaixo as seguintes informações:')
      idade = int(input('Sua idade: '))
      estado = input('Estado em que reside: ')
      if idade <= 25:
        resposta = input('Você estuda? (sim ou não) ')
        if resposta.lower() == 'sim':
            home_office_ou_presencial = input('Home office ou presencial? ')
            if home_office_ou_presencial.lower() == 'presencial':
                horas_estudo = int(
                    input(
                        "Quantas horas por dia você passa no seu local de estudos? "
                    ))
            if home_office_ou_presencial.lower() == 'home office':
                print(
                    'Lembre-se de manter todos os cuidados necessários ao sair de casa!\n'
                )
        if resposta.lower() == 'não':
            trabalho = input('Você trabalha? ')
            if trabalho.lower() == 'sim':
                horas_trabalho = int(
                    input('Quantas horas você passa no trabalho? '))
      else:
        trabalho = input('Você trabalha? ')
        if trabalho.lower() == 'sim':
            horas_trabalho = int(input('Quantas horas você passa no trabalho? '))
        else: 
          resposta = 1

      saidas_por_dia = int(input('Quantas vezes por dia você sai de casa, em média? (Incluindo trabalho ou estudo) '))
      if saidas_por_dia == 0:
        saidas_por_dia = 1
      horas_fora = int(input('Quantas horas você fica fora de casa por dia, em média? '))
      if horas_fora == 0:
        horas_fora = 1

    #Processamanto
    
      if trabalho == 'sim':
        trabalho1 = trabalho
        resposta = 1
        resposta1 = resposta
        home_office_ou_presencial = 1
        home_office_ou_presencial1 = home_office_ou_presencial
      if resposta == 'sim':
        resposta1 = resposta
        trabalho == 'não'
        trabalho1 = trabalho
        home_office_ou_presencial == 'presencial'
        home_office_ou_presencial1 = home_office_ou_presencial
      if trabalho == 'não':
        trabalho1 = trabalho
        resposta = 'não'
        resposta1 = resposta
        home_office_ou_presencial = 0
        home_office_ou_presencial1 = home_office_ou_presencial

      alcool_em_gel = (horas_fora * 50)
      if trabalho1 == 'sim':
        mascara = round((horas_trabalho/2)+0.5)
      if resposta1 == 'sim' and home_office_ou_presencial1 == 'presencial':
        mascara = round((horas_estudo/2)+0.5)

      for i in estados_no_amarelo:
        if estado == i:
            print('Seu estado está na fase amarela. Continue mantendo os cuidados necessários!\n')
      if estado == 1:
        if saidas_por_dia >= 3:
            print('Seu estado esta na fase amarela! Você está saindo muitas vezes de casa e corre grande risco de se contaminar. Esse vírus é perigoso. Se cuide!\n'
            )
        else:
            print('Seu estado está na fase amarela! Você está saindo poucas vezes ao dia. Continue se cuidando!\n')
      if estado == 2:
        if saidas_por_dia == 0:
            print('Continue mantendo seus cuidados!')
        else:
            print('Seu estado esta na fase vermelha! Fique em casa, saia apenas se for necessário!')



      print(
        f'{login}, você deve levar 50 ml de álcool em gel para cada vez que você sai de casa, ou seja, no total você devem ser utilizados {alcool_em_gel} ml de álcool em gel.\n'
    )

      if trabalho1 == 'sim':
        print(
            f'É recomendado trocar de máscara a cada 2 horas, como você fica cerca de {horas_trabalho} hora(s) por dia trabalhando, você precisa de {mascara} máscara(s), aproximadamente.\n'
        )
      if resposta1 == 'sim' and home_office_ou_presencial1 == 'presencial':
        print(
            f'É recomendado trocar de máscara a cada 2 horas, como você fica cerca de {horas_estudo} hora(s) por dia no seu local de estudos, você precisa de {mascara} máscara(s), aproximadamente.\n'
        )

      mascara_total = round((horas_fora/2)+0.5)

    #Saída
      print('Recomendações:')
      print(f'Levar {mascara_total} máscara(s);')
      print(f'Levar {alcool_em_gel} ml de álcool em gel.')

      if saidas_por_dia >= 3:
        print('Sair menos de casa!')

      print()
      print(opçoes)
      opçao = int(input('Digite a opção escolhida: '))

print('Obrigado por utilizar nosso app e continue se cuidando!')
input()
