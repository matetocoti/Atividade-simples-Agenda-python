def agenda_de_telefone():
    # Lista de dicionarios com telefone e nome
    agenda = []
    while True:
        contato = {}
        print("---------------------------------------------------------------------------------------------------")
        print(f"\n\t\t\t\t\t\t\t\t\t\t(OPTIONS)")
        print(f"\n\t|(1)Adicionar-contato|(2)Adicionar-telefone|(3)Excluir-Contato|(4)Consultar-contato|(5)Exit|")
        option = int(input(f"\n\tOption:"))
        # Salvando contato
        if option == 1:
            # Pegando o nome do contato
            contato["nome"] = input(f"\n\tDigite o nome do contato:")
            # Guardando contato na list agenda
            agenda.append(contato)
            # Incluindo numero do contato
        elif option == 2:
            # Pegando o nome do contato|key
            nome_busca = input(f"\n\tDigite o nome do contato:")
            # Procurando contato na agenda
            for nome in agenda:
                if "nome" in nome and nome["nome"] == nome_busca:
                    telefones = len(nome)
                    # Adicionando telefone ao contato
                    nome[f"Telefone{telefones}"] = input(f"\n\tDigite o telefone do contato:")
                    break
        # Excluindo contato
        elif option == 3:
            contato_index = -1
            # Pegando o nome do contato|key
            nome_busca = input(f"\n\tDigite o nome do contato:")
            # Procurando contato na agenda
            for nome in agenda:
                contato_index += 1
                if "nome" in nome and nome["nome"] == nome_busca:
                    agenda.pop(contato_index)
                    break
        # Buscando dados salvos do contato
        elif option == 4:
            # Pegando o nome do contato|key
            nome_busca = input(f"\n\tDigite o nome do contato:")
            # Procurando contato na agenda
            for nome in agenda:
                if "nome" in nome and nome["nome"] == nome_busca:
                    print(f"\n\t{nome}")
                    break
        # Encarrando programa
        elif option == 5:
            print(f"\n\tEncerrando...")
            break
