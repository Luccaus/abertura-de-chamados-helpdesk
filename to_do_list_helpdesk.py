
lista_chamados = [ ]
setor_chamados = [ ]

def chamado():
    print()
    print("Qual suporte você precisa? \n")

    while True:
        try:
            chamados = int(input("[1] Técnico [2] Redes: "))
            if chamados == 1:
                lista_chamados.append("Suporte Técnico")
                break
            elif chamados == 2:
                lista_chamados.append("Suporte Redes")
                break
            else:
                print("Digite [1] ou [2]")
                continue

        except ValueError:
            print("Digite um valor válido!")
            continue


def setor():
    print()
    print("Qual o seu setor? \n")

    while True:
        try:
            setores = input("[F]inanceiro [J]urídico: ").lower()
            print()
            if setores == "f":
                setor_chamados.append("Financeiro")
                break
            elif setores == "j":
                setor_chamados.append("Jurídico")
                break
            else:
                print("Digite um setor válido")
                continue

        except ValueError:
            print("Digite um setor válido")
            continue

def menu():
    print("-----BEM VINDO A CENTRAL DE CHAMADOS-----\n")
    print("Digite o proximo passo\n")
    while True:
        try:
            menu = input("[N]ovo chamado [L]ista [S]air: ").lower() 
            
            if menu == "n":
                suporte = chamado()
                setorista = setor()
                print("///////////////////////////////")
                print("Chamado registrado com sucesso!")
                print("///////////////////////////////")
                print()
    
                continue 

            elif menu == "l":
                if lista_chamados == []:
                    print("No momento não temos chamados em aberto!")
                    continue
                else:
                    for i in range(len(lista_chamados)):
                        print(f"Lista de chamados: {lista_chamados[i]} no setor {setor_chamados[i]}\n")
                        continue
            else:
                print("Digite [N], [L] ou [S] para continuar!")
                break
    
        except ValueError:
            print("Digite um comando válido! \n")
            continue

gerenciador = menu()
print()
print("Obrigado por usar nosso gerenciador de chamados! :)")