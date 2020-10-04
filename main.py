import requests

while True:

    try:
        print("\n===CONVERSOR DE MOEDAS===")
        print("\nOpções:")
        print("1 - Lista de moedas;")
        print("2 - Conversor;")
        print("3 - Sair.")

        opcao = input()

        if opcao == "1":
            url = "https://currency-exchange.p.rapidapi.com/listquotes"
            headers = {
                'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
                'x-rapidapi-key': "8da8a604b4msh5e010b771fe4cd8p18d10ajsnb6372429e66d"
            }
            response = requests.request("GET", url, headers=headers)
            print("Moedas válidas:")
            print(response.text)

        elif opcao == "2":
            print("\nInsira a moeda a ser comparada:")
            moeda1 = input()
            if len(moeda1) == 0:
                raise Exception

            print("\nInsira a moeda comparadora: ")
            moeda2 = input()

            if len(moeda1) == 0:
                raise Exception

            url = "https://currency-exchange.p.rapidapi.com/exchange"
            querystring = {"q": "1.0", "from": moeda1.upper(), "to": moeda2.upper()}
            headers = {
                'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
                'x-rapidapi-key': "8da8a604b4msh5e010b771fe4cd8p18d10ajsnb6372429e66d"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(moeda1.upper() + " vale " + response.text + " vezes a moeda " + moeda2.upper() + "\n")

            dados = open("dados.csv", "w+")
            dadosStr = moeda1.upper() + "," + response.text + "," + moeda2.upper()
            dados.write(dadosStr)
            dados.close()
            print("Dados salvos no arquivo *dados.csv*.\nRetornando ao Menu Principal...")

        elif opcao == "3":
            print("Saindo do programa...")
            break

        else: raise Exception

    except:
        print("Opção inválida.")
