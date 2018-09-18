# Argumentos:
# Posicionais vs Nomeados

def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
          .format(nome, sobrenome, idade, sexo))

#dados_pessoais("Mateus", "Israel", 19, "M")
dados_pessoais(sobrenome="Israel",idade=19, sexo="M", nome="Mateus")
