def add_contact(contacts, contact_name, contact_phone, contact_email):
    contact = {"name": contact_name, "phone": contact_phone, "email": contact_email, "favorite": False}
    contacts.append(contact)
    print(f"Contato '{contact_name}' adicionado com sucesso!")


def visualize_contacts(contacts):
    print("\n----- Lista de Contatos -----")
    for index, contact in enumerate(contacts, start=1):
        favorite = "★" if contact['favorite'] else " "
        print(f"{index}. [{favorite}] {contact['name']} - {contact['phone']} - {contact['email']}")


def visualize_fields():
    print(f"\n----- Lista de Campos do Contato -----")
    print("1. Nome")
    print("2. Telefone")
    print("3. Email")


def edit_contact(contacts, chosen_contact):
    try:
        if int(chosen_contact) in range(1, (len(contacts) + 1)):
            adjusted_chosen_contact = int(chosen_contact) - 1
        else:
            print("Não existe um contato registrado para o índice inserido!")
            return
    except Exception as e:
        print(f"Erro: {e}")
        return

    visualize_fields()
    chosen_field = input("\nDigite o número do campo que deseja editar: ")

    if chosen_field == "1":
        new_contact_name = input("Digite o novo nome do contato: ")
        contacts[adjusted_chosen_contact]['name'] = new_contact_name
        print(f"Nome do contato foi alterado para '{new_contact_name}' com sucesso!")
    elif chosen_field == "2":
        new_phone = input("Digite o novo número do contato: ")
        contacts[adjusted_chosen_contact]['phone'] = new_phone
        print(f"Telefone do contato foi alterado para '{new_phone}' com sucesso!")
    elif chosen_field == "3":
        new_email = input("Digite o novo email do contato: ")
        contacts[adjusted_chosen_contact]['email'] = new_email
        print(f"Email do contato alterado para '{new_email}' com sucesso!")
    else:
        print("Opção inválida!")


def mark_as_favorite_contact(contacts, chosen_contact):
    try:
        if int(chosen_contact) in range(1, (len(contacts) + 1)):
            adjusted_chosen_contact = int(chosen_contact) - 1
        else:
            print("Não existe um contato registrado para o índice inserido!")
            return
    except Exception as e:
        print(f"Erro: {e}")
        return
    
    if contacts[adjusted_chosen_contact]['favorite'] == False:
        contacts[adjusted_chosen_contact]['favorite'] = True
        print(f"Contato '{contacts[adjusted_chosen_contact]['name']}' foi marcado como favorito!")
    else:
        contacts[adjusted_chosen_contact]['favorite'] = False
        print(f"Contato '{contacts[adjusted_chosen_contact]['name']}' foi desmarcado como favorito!")


def visualize_favorites_contacts(favorite_valid):
    print("\n----- Lista de Contatos Favoritos -----")
    for index, contact in enumerate(favorite_valid, start=1):
        print(f"{index}. [★] {contact['name']} - {contact['phone']} - {contact['email']}")


def delete_contact(contacts, chosen_contact):
    try:
        if int(chosen_contact) in range(1, (len(contacts) + 1)):
            adjusted_chosen_contact = int(chosen_contact) - 1
        else:
            print("Não existe um contato registrado para o índice inserido!")
            return
    except Exception as e:
        print(f"Erro: {e}")
        return
    contact_removed = contacts.pop(adjusted_chosen_contact)
    print(f"Contato '{contact_removed['name']}' apagado com sucesso!")

contacts = []

while True:
    print("\n----- Agenda de Contatos -----")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Visualizar contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    choice = input("\nDigite sua escolha: ")

    if choice == "1":
        print("\n----- Adicionando Contato -----")
        contact_name = input("Digite o nome do seu contato: ")
        contact_phone = input("Digite o telefone: ")
        contact_email = input("Digite o email: ")
        add_contact(contacts, contact_name, contact_phone, contact_email)
    elif choice == "2":
        if len(contacts) > 0:
            visualize_contacts(contacts)
        else:
            print("Nenhum contato registrado!")
    elif choice == "3":
        if len(contacts) > 0:
            visualize_contacts(contacts)
            chosen_contact = input("\nDigite o número do contato que deseja editar: ")
            edit_contact(contacts, chosen_contact)
        else:
            print("Nenhum contato registrado!")
    elif choice == "4":
        if len(contacts) > 0:
            visualize_contacts(contacts)
            chosen_contact = input("\nDigite o número do contato que deseja marcar/desmarcar como favorito: ")
            mark_as_favorite_contact(contacts, chosen_contact)
        else:
            print("Nenhum contato registrado!")
    elif choice == "5":
        favorite_valid = []
        if len(contacts) > 0:
            for contact in contacts:
                if contact['favorite']:
                    favorite_valid.append(contact)
        if len(favorite_valid) > 0:
            visualize_favorites_contacts(favorite_valid)
        else:
            print("Nenhum contato marcado como favorito. Visualização indisponível!")
    elif choice == "6":
        if len(contacts) > 0:
            visualize_contacts(contacts)
            chosen_contact = input("\nDigite o número do contato que deseja apagar: ")
            delete_contact(contacts, chosen_contact)
        else:
            print("Nenhum contato registrado. Função indisponível!")
    elif choice == "7":
        print("Programa Encerrado!")
        break
    else:
        print("Opção inválida!")