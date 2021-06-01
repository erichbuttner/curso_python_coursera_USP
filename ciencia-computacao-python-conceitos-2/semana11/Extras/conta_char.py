def conta_letras(frase, contar = "vogais"):

    cont_vogais = 0
    cont_consoantes = 0
    indice = 0

    lista_vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    lista_consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                    "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
                    "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N",
                    "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

    contar = contar.strip()
    contar = contar.lower()

    while indice < len(frase):
        if contar == "vogais" and frase[indice] in lista_vogais:
            cont_vogais += 1
        if contar == "consoantes" and frase[indice] in lista_consoantes:
            cont_consoantes += 1
        indice += 1

    if contar == "vogais":
        return cont_vogais

    if contar == "consoantes":
        return cont_consoantes

# Função que exibe as letras maiúsculas de uma frase

def exibe_maiusculas(frase):
    cont = 0
    letras_maiusculas = ""

    while cont < len(frase):
        if ord(frase[cont]) >= 65 and ord(frase[cont]) <= 90:
            letras_maiusculas += frase[cont]
        cont += 1

    return letras_maiusculas

# Função que inverte uma palavra

def inverte_palavra(string):
    pos = len(string)-1
    string = string.upper()
    while pos >= 0:
        print(string[pos],end = "")
        pos = pos - 1

# Função que checa se letra é vogal

def é_vogal(letra):

    lista_vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    if letra in lista_vogais:
        return True, letra
    else:
        return False

# Coloca lista de strings na ordem lexicográfica
# sem diferenciar minúsculas de maiúsculas

def lex_menor(lista):

    lista_minusculas = []

    for item in lista:
        item = item.lower() # Apagar esse linha para considerar maiúsculas e minúsculas
        lista_minusculas.append(item)

    lista_final = sorted(lista_minusculas)

    return lista_final[0]

# Função que recebe lista de nomes e exibe o mais curto

def nome_mais_curto(lista):
    nome_anterior = ""
    for nome in lista:
        nome = nome.strip()
        if len(nome) < len(nome_anterior) or nome_anterior == "":
            nome_selecionado = nome
            nome_anterior = nome
    nome_selecionado = nome_selecionado.capitalize()
    return nome_selecionado

# Teste para a função de nome mais curto
# Vê se funciona com espaços antes e depois
# Ignora maiúsculas e minúsculas
# Exibe com capitalize

def testa_mais_curto():
    if nome_mais_curto(["   luciana ", "        PaUlO     ", "  AnA    ", "JEFFERSON      "]) == "Ana":
        print("A função está funcionando.")
    else:
        print("A função não está funcionando.")

# Função que coloca uma palavra em maiúsculas e
# minúsculas alternadas

def palavra_maiuscula_minuscula(string):
    pos = 0
    string1 = ""
    string = string.lower()
    stringMa = string.upper()
    while pos < len(string):
        if pos % 2 == 0:
            string1 = string1 + stringMa[pos]
        else:
            string1 = string1 + string[pos]
        pos = pos + 1
    return string1