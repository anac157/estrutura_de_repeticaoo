nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while nome == senha:
    print("Sua senha não pode ser seu nome.")
    print("Por favor, digite novamete seu nome e senha")

    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

print("Olá,", nome, "sua senha esta segura comigo ;)")