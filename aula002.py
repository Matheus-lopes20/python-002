faturamento = 100
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento * 100

print(f"Faturamento da empresa: {faturamento}, custo: {custo}, lucro: {lucro} ")

email = "lopes040504@gmail.com"

# maiscula
email_cliente = email
email_cliente = email_cliente.upper()
print(email_cliente)
# minuscula
email_cliente = email_cliente.lower()
print(email_cliente)

# "@"
print(email_cliente.find("@")) # -1 quando não encontra

# tamanho do texto
print(len(email_cliente))

# pegar um caractere
print(email_cliente[5])

print(email_cliente[-4])

# pegar um pedaço do texto
print(email_cliente[1:5])

# trocar um pedaço do texto
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
print(novo_email)

nome = "matheus Lopes "
# trabalhar com nomes
print(nome.capitalize())
print(nome.title())

# pegar o servidor do email
posicao_arroba = email_cliente.find("@") +1
servidor = email_cliente[posicao_arroba:]
servidor = email_cliente[12:]
print(servidor)

# pegar 1º nome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]

# pegar o sobrenome
sobrenome = nome[posicao_espaco+1:]
print(primeiro_nome)
print(sobrenome)

#casos especiais - formatações numéricas em texto
print(f"Faturamento da empresa: R${faturamento}, custo: R${custo}, lucro: R${lucro}, Margem: {margem_lucro:.0%} ")