def obter_nome_usuario():
    return input("Digite seu nome: ")

def main():
    nome = obter_nome_usuario()
    print(f"Olá, {nome}! Bem-vindo ao projeto prático da DIO.")

if __name__ == "__main__":
    main()
