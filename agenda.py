def add_contact(contacts, contact_name, contact_phone, contact_email):
    contact = {"name": contact_name, "phone": contact_phone, "email": contact_email, "favorite": False}
    contacts.append(contact)
    print(f"Contato '{contact_name}' adicionado com sucesso!")

contacts = []

while True:
    print("\n----- Agenda de Contatos -----")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Visualizar contatos favoritos")
    print("6. Apagar contato")
    print("7. Visualizar detalhes de um contato")
    print("8. Sair")

    choice = input("\nDigite sua escolha: ")

    if choice == "1":
        print("----- Adicionando Contato -----")
        contact_name = input("Digite o nome do seu contato: ")
        contact_phone = int(input("Digite o telefone: "))
        contact_email = input("Digite o email: ")
        add_contact(contacts, contact_name, contact_phone, contact_email)
    elif choice == "8":
        break
    else:
        print("Opção inválida!")