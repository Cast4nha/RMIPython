import Pyro4

uri = input("Qual é o URI Pyro do objeto FileServer? ").strip()
file_server = Pyro4.Proxy(uri)  # Obter um proxy Pyro para o objeto FileServer

# Menu de opções
while True:
    print("\n=== MENU ===")
    print("1. Fazer upload de um arquivo")
    print("2. Consultar informações sobre os arquivos disponíveis")
    print("3. Fazer download de um arquivo")
    print("4. Registrar interesse em um arquivo")
    print("5. Cancelar registro de interesse")
    print("0. Sair")

    choice = input("Escolha uma opção: ")
    if choice == "1":
        filename = input("Digite o nome do arquivo: ")
        filedata = input("Digite os dados do arquivo: ")
        file_server.upload_file(filename, filedata)
    elif choice == "2":
        files = file_server.get_file_info()
        if files:
            print("Arquivos disponíveis:")
            for filename in files:
                print(filename)
        else:
            print("Nenhum arquivo disponível.")
    elif choice == "3":
        filename = input("Digite o nome do arquivo: ")
        file_content = file_server.download_file(filename)
        if file_content:
            print(f"Conteúdo do arquivo '{filename}': {file_content}")
        else:
            print(f"Arquivo '{filename}' não encontrado.")
    elif choice == "4":
        filename = input("Digite o nome do arquivo: ")
        client_reference = input("Digite a referência do objeto remoto do cliente: ")
        validity_period = int(input("Digite a validade do registro de interesse em segundos: "))
        file_server.register_interest(filename, client_reference, validity_period)
    elif choice == "5":
        filename = input("Digite o nome do arquivo: ")
        client_reference = input("Digite a referência do objeto remoto do cliente: ")
        file_server.cancel_interest(filename, client_reference)
    elif choice == "0":
        break
    else:
        print("Opção inválida. Digite novamente.")
