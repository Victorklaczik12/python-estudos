# Hora 2: prática (escreva sem ajuda de IA)
# DESAFIO 01: Programa que pede seu nome e responde “Olá, [nome]!”.
# DESAFIO 02: Programa que pede dois números e mostra a soma, a subtração e a multiplicação. Atenção: input() devolve texto, então use int() ou float().
# DESAFIO 03: Conversor de reais para dólar, com a cotação em uma variável.
# DESAFIO 04: Programa que pede o preço de um produto e mostra o preço com 10% de desconto.
# Fechamento (5 min)
# Anote em um arquivo: o que aprendeu e o que travou.
# Suba os 4 programas em uma pasta nova no GitHub (python-estudos), com git add, git commit e git push. Assim você pratica Git desde o primeiro dia.


#desafio 01 facil
# nome=input ('Qual é seu nome Sr.?')
# print('Olá Sr.',nome)





#desafio 02 
# import os #importando biblioteca que limpa a tela se o usuário decidir continuar
# while True:
#     numero01 = int(input('digite um numero:'))
#     numero02 = int(input('digite mais um numero, vou lhe apresentar algumas operações:'))
#     soma= numero01 + numero02
#     sub= numero01 - numero02
#     mult= numero01 * numero02
#     print(f'essa é a soma dos numeros:{soma}')
#     print(f'essa é a subtração do primeiro numero com o segundo:{sub}')
#     print(f'essa é a multiplicação do primeiro numero com o segundo:{mult}')


# #estrutura condicional
#     stop = int(input('quer continuar a brincadeira? 1 - Sim / 2 - Não:'))

#     if stop == 1: 
#         print('reiniciando...')
#         # 2. Esse comando limpa a tela: 'cls' no Windows, 'clear' no Linux/Mac
#         os.system('cls' if os.name == 'nt' else 'clear')
#         # O comando 'continue' faz o código ignorar o resto e voltar lá para o topo do 'while'
#         continue

#     else:
#         # 2. Esse comando limpa a tela: 'cls' no Windows, 'clear' no Linux/Mac
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print('Programa encerrado! Até logo!')
#         #comando 'break' quebra o 'while' e finaliza o programa.
#         break




#     #desafio 03: Conversor de reais para dólar, com a cotação em uma variável ( pegue uma API para cotação atual do US$).
# import requests
# # buscar a cotação atualizada na API:
# try: 
#     url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
#     resposta = requests.get(url)
#     dados = resposta.json()
# # estrair o valor atual de compra do dolar:
#     cotacao_dolar = float(dados["USDBRL"]["bid"]) #dados["USDBRL"]["bid"]: Navega pelos dados para capturar a taxa de compra do momento.
#     print('Cotação atual do Dólar: U$ 1 = R$ {:.2f}'.format(cotacao_dolar))
#     valor = float(input('Digite quantos reais você tem em sua carteira? R$'))
#  # 3. Calcula a conversão
#     dolares_comprados = valor / cotacao_dolar
#     print ('Com R${:.2f} você pode trocar/comprar US${:.2f}'.format(valor, dolares_comprados))

# except requests.exceptions.RequestException:
#     print("Erro: Não foi possível conectar à API para buscar a cotação.")
# except KeyError:
#     print("Erro: Estrutura de dados inválida retornada pela API.")
# except ValueError:
#     print("Erro: Digite apenas números válidos para o valor em carteira.")


# DESAFIO 04: Programa que pede o preço de um produto e mostra o preço com 10% de desconto.

# produto = float(input('Você está querendo sabe o preço de algum produto com 10% de desconto. então digite o valor desse produto: R$'))
# desconto = produto * 0.10
# preco_final = produto - desconto
# print(f"Preço original do produto: R${produto:.2f}")
# print(f"Preço com o desconto de 10%: R${preco_final:.2f}")
