#Primeiro criamos a variável de controle do loop
continua = "sim"
print()
print("⚔️ Bem-vindo nobre guerreiro! ⚔️ ") 
print("Vamos delegar seu nível se baseando em sua xp.")
#Agora iniciamos o loop que continuará enquanto o usuário desejar
while continua == "sim":
    print()
    print("Por favor responda as perguntas a seguir:")
    nome = input("Digite seu nome: ")
    xp = int(input("Digite sua XP: "))
    #não é necessário criar uma nova variável para i, podemos usar xp diretamente
    i = xp

    #Não é necessário utilizar operadores lógico "AND" pois no if já testou a condição anterior
    if i < 1000:
        nivel = " Ferro"
        mensagem = "Seus inimigos estão ferrados!"

    elif i <= 2000:
        nivel = "Bronze"
        mensagem = "Pegastes um bronze hoje!"

    elif  i <= 5000:
        nivel = "Prata"
        mensagem = "Medalha de prata nem sempre é ruim!"

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

    print()
    # adicionado f antes das aspas para formatar a string
    print(f"O Herói de nome {nome} está no nível {nivel} com {i} de XP.")
    print(mensagem)
    #adicionado espaço entre uma interação e outra para facilitar a leitura
    print("")

    continua = input("Queres avaliar outro jovem guerreiro?(sim/não) ")
    print("")
    
    #adicionado uma condicional para sair do loop caso o usuário digite "não"
    #melhor adicionar != "sim"pois assim não irá aparecer a mensagem no caso de querer avaliar outro guerreiro
    if continua != "sim":
     break
    #Aqui não e necessário colocar else, pois se o usuário digitar "não" o loop já terá sido encerrado
    #Adicionado uma outra mensagem pois não faz sentido dar boas vindas novamente
    print("Vamos avaliar outro pequeno gafanhoto!")
    print("Você já sabe como funciona!")

print("Agora vás lutar!")
print("Saibas que um filho teu não foge a luta!")