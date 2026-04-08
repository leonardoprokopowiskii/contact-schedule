contacts = []

while True:
    print("----- Agenda de Contatos -----")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Visualizar contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    choice = input("\nDigite sua escolha: ")

    if choice == "7":
        break