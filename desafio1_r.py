#Primeiro criamos a variável de controle do loop
continua = "sim"
print("\nBem-vindo ao classificador de níveis de nobres guerreiros baseado em XP!")
#Agora iniciamos o loop que continuará enquanto o usuário desejar
while True:

    catidade = int(input("Quantos hérois você quer avaliar? "))
    print("Digite o nome dos hérois e suas respectivas XP's para descobrir seus níveis: ")
    
    #Crio uma lista fora para ir adicionando os valores de xp e nome que o loop vai resultar
    #Faço a mesma coisa para nível e mensagem
    nome = []
    xps = []
    niveis = []
    mensagens = []

    for i in range(catidade):

        heroi = input(f"Héroi {i+1}: ") 
        xp = int(input(f"Xp {i+1}: "))
        #append adiciona os valores nas listas nome e xps
        #mas antes preciso criar um vetor vazio
        #vetor.adiciona(variavel)
        nome.append(heroi)
        xps.append(xp)

    #for é necessário para percorrer os valores do vetor xps
    #utilizo o i como índice para simular o valor de xp e quando bater o valor de i com xp ele irá me 
    #retornar o nível correspondente
    #não preciso colocar o range com len(xps) pois i já está representando o valor de xp
    for i  in xps:

        #para esse caso é mehor utilizar o if/elif do que case pois o case não verifica o calculo ele só verifica se a o valor da variável é True ou False. 
        #O case somente funciona para testar valores exatos que sejam ou resultem em uma variável booleana. Ele compara diretamente a variável, sem conseguir fazer cálculos ou comparações mais complexas.
        #Não é necessário utilizar operadores lógico "AND" pois no if já testou a condição anterior
        if i < 1000:
            nivel = "Ferro"
            mensagem = "Seus inimigos estão ferrados!"

        elif i <= 2000:
            nivel = "Bronze"
            mensagem = "Pegastes um bronze hoje!"

        elif  i <= 5000:
            nivel = "Prata"
            mensagem = "Surfista Prateado!"

        elif i  <= 7000:
            nivel = "Ouro"
            mensagem = "Ouro é o novo preto!"

        elif i  <= 8000:

            nivel = "Platina"
            mensagem = "Platinastes as madeixas!"


        elif i <= 9000:
            nivel = "Ascendente" 
            mensagem = "Segura essa espada!"


        elif i <= 10000:
            nivel = "Imortal"
            mensagem = "Imortal até morrer!"
            
        else:
            nivel = "Radiante"
            mensagem = "Mr. Sunshine!"

        #Garantir que os termos vão ser adicionados em uma lista    
        niveis.append(nivel)
        mensagens.append(mensagem)    

    # xp.index(i) pega o índice i do vetor xp para relacionar com a variavel de mesmo índice do vetor nome  
    # adicionado f antes das aspas para formatar a string
    print()
    for i in range(catidade):
        print(f"O Herói de nome {nome[i]} está no nível {niveis[i]} com {xps[i]} de XP")
        print(mensagem)

    #adicionado espaço entre uma interação e outra para facilitar a leitura
    #Ao invés de colocar um monte de print() utilizo o. \n para pular linha
    continua = input("\nQueres fazer uma nova avaliação? ").lower()
    
    continua_validos = ["nao", "não", "n", "no" , "not"]
    
    #adicionado uma condicional para sair do loop caso o usuário digite "não"
    if continua in continua_validos:
     break
    #Aqui não e necessário colocar else, pois se o usuário digitar "não" o loop já terá sido encerrado
    #Adicionado uma outra mensagem pois não faz sentido dar boas vindas novamente
    print("\nVamos para mais uma rodada!")
    print("Você já sabe como funciona!\n")

print("Agora vás lutar!")
print("Saibas que um filho teu não foge a luta!")

