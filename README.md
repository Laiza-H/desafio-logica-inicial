# 🛡️ Classificador de Nível de Herói

Este projeto é uma aplicação em Python desenvolvida para classificar o nível de um herói com base na sua quantidade de Experiência (XP). O projeto foi criado como parte de um desafio de lógica de programação para praticar conceitos fundamentais de desenvolvimento.

## 📝 O Desafio

O objetivo principal era criar uma estrutura de decisão para apresentar mensagens específicas baseadas no XP do herói.

### Regras de Classificação:

| XP | Nível |
| :--- | :--- |
| Menor que 1.000 | Ferro |
| Entre 1.001 e 2.000 | Bronze |
| Entre 2.001 e 5.000 | Prata |
| Entre 5.001 e 7.000 | Ouro |
| Entre 7.001 e 8.000 | Platina |
| Entre 8.001 e 9.000 | Ascendente |
| Entre 9.001 e 10.000 | Imortal |
| Maior ou igual a 10.001 | Radiante |

> **Saída esperada:** "O Herói de nome **{nome}** está no nível de **{nivel}**".

---

## 🚀 Tecnologias e Conceitos Utilizados

A solução utiliza diversos pilares da programação:

* **Variáveis e Tipos:** Armazenamento de nomes e XP.
* **Estruturas de Repetição:** Uso de `while` para manter o programa rodando e `for` para percorrer listas de heróis.
* **Listas (Arrays):** Armazenamento de múltiplos nomes, níveis e mensagens personalizadas.
* **Estruturas de Decisão:** Uso de `if/elif/else` para determinar a categoria correta baseada no XP.

---

## 🛠️ Como Funciona o Código

1. **Entrada:** O usuário define a quantidade de heróis que deseja avaliar.
2. **Coleta de Dados:** O programa solicita o nome e o XP para cada herói inserido.
3. **Processamento:** O código percorre a lista de XP, define o nível e uma mensagem divertida para cada um.
4. **Relatório:** Exibe o nome, nível e XP formatado de cada herói.
5. **Opção de Saída:** O programa pergunta se o usuário deseja realizar uma nova avaliação ou encerrar a execução.

---

## 🏃 Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. Salve o código em um arquivo chamado `desafio1_r.py`.
3. No terminal, execute:
   ```bash
   python desafio1_r.py
