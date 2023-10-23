def agenda_de_telefone():
    # Lista de dicionarios com telefone e nome
    agenda = []
    while True:
        try:
            contato = {}
            print("---------------------------------------------------------------------------------------------------")
            print(f"\n\t\t\t\t\t\t\t\t\t\t(OPTIONS)")
            print(f"\n\t|(1)Adicionar-contato|(2)Adicionar-telefone|(3)Excluir-Contato|(4)Consultar-contato|(5)Exit|")
            option = int(input(f"\n\tOption:"))
            # Salvando contato
            if option == 1:
                # Pegando o nome do contato
                contato["nome"] = input(f"\n\tDigite o nome do contato:")
                if contato["nome"].strip() == "":
                    print("\n\tNome invalido!")
                    continue
                # Guardando contato na list agenda
                agenda.append(contato)
                # Incluindo numero do contato
            elif option == 2:
                confirm = False
                # Pegando o nome do contato|key
                nome_busca = input(f"\n\tDigite o nome do contato:")
                # Procurando contato na agenda
                for nome in agenda:
                    if "nome" in nome and nome["nome"] == nome_busca:
                        telefones = len(nome)
                        # Adicionando telefone ao contato
                        nome[f"Telefone{telefones}"] = input(f"\n\tDigite o telefone do contato:")
                        confirm = True
                        break
                # Se não foi confirmado que o contato foi encotrado
                if confirm is not True:
                    # Aviso avisando que o contato digitado nao foi encontrado
                    print(f"\n\tNão foi possivel encontrar o contato!")
            # Excluindo contato
            elif option == 3:
                confirm = False
                contato_index = -1
                # Pegando o nome do contato|key
                nome_busca = input(f"\n\tDigite o nome do contato:")
                # Procurando contato na agenda
                for nome in agenda:
                    # Contando até o index do contato desejado
                    contato_index += 1
                    # Se nome iterado igual a nome digitado ...
                    if "nome" in nome and nome["nome"] == nome_busca:
                        # Removendo contato no index do contato buscado
                        agenda.pop(contato_index)
                        confirm = True
                        # E parando o loop for
                        break
                # Se não foi confirmado que o contato foi encotrado
                if confirm is not True:
                    # Aviso avisando que o contato digitado nao foi encontrado
                    print(f"\n\tNão foi possivel encontrar o contato!")
            # Buscando dados salvos do contato
            elif option == 4:
                confirm = False
                # Pegando o nome do contato|key
                nome_busca = input(f"\n\tDigite o nome do contato:")
                # Procurando contato na agenda
                for nome in agenda:
                    # Se nome iterado igual a nome digitado ...
                    if "nome" in nome and nome["nome"] == nome_busca:
                        # Mostrando contato e telefones
                        print(f"\n\t{nome}")
                        confirm = True
                        # Parando o loop for
                        break
                # Se não foi confirmado que o contato foi encotrado
                if confirm is not True:
                    # Aviso avisando que o contato digitado nao foi encontrado
                    print(f"\n\tNão foi possivel encontrar o contato!")
            # Encarrando programa
            elif option == 5:
                print(f"\n\tEncerrando...")
                break
        except ValueError:
            print(f"\n\tError!")
        except RuntimeError:
            print(f"\n\tError!")
        except KeyboardInterrupt:
            print(f"\n\tError!")

