import os

# Lista para armazenar o histórico.
historico_leituras = []


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cadastrar_dados():
    """ Cadastro das Informações. """
    print("--- CADASTRO DE SENSORES ---")
    try:
        temperatura = int(input("Temperatura da nave (°C): "))
        porcentagem_energia = int(input("Nível de energia (0-100%): "))
        status_comunicacao = int(input("Status da comunicação (1-Ativo / 0-Falha): "))

        leitura = {
            "temp": temperatura,
            "energia": porcentagem_energia,
            "comunicacao": status_comunicacao
        }
        historico_leituras.append(leitura)
        print("\n[OK] Dados registrados com sucesso!")
    except ValueError:
        print("\n[ERRO] Digite apenas números inteiros.")

    input("\nPressione Enter para continuar...")


def analisar_missao(dados):
    """ Verificação Automática. """
    temp = dados["temp"]
    ener = dados["energia"]
    comm = dados["comunicacao"]

    if temp > 80 and ener > 20 and comm == 1:
        print("Alerta de superaquecimento!")
    elif temp < 80 and ener < 20 and comm == 1:
        print("Modo de Economia de energia ligado!")
    elif temp < 80 and ener > 20 and comm == 0:
        print("Falha na Comunicação!")
    elif temp > 80 and ener < 20 and comm == 1:
        print("Alerta de superaquecimento e Modo de Economia de energia ligado!")
    elif temp > 80 and ener > 20 and comm == 0:
        print("Alerta de superaquecimento e falha na Comunicação!")
    elif temp < 80 and ener < 20 and comm == 0:
        print("Modo de Economia de energia ligado e falha na Comunicação!")
    elif temp > 80 and ener < 20 and comm == 0:
        print("Alerta de superaquecimento, Modo de Economia de energia ligado e falha na Comunicação!")
    else:
        print("Status da missão válidos!" "\n Nave pronta para prosseguir!")


def exibir_historico():
    """ Histórico das leituras. """
    if not historico_leituras:
        print("\nNenhum dado no histórico.")
    else:
        print("--- HISTÓRICO DE MONITORAMENTO ---")
        for i, d in enumerate(historico_leituras, 1):
            print(f"Leitura {i} -> Temp: {d['temp']}°C | Energia: {d['energia']}% | Comunicação: {d['comunicacao']}")

    input("\nPressione Enter para voltar ao menu...")


def menu_principal():
    """ Menu Interativo. """
    while True:
        limpar_tela()
        print("=" * 40)
        print("  SISTEMA DE MONITORAMENTO ESPACIAL")
        print("=" * 40)
        print("1. Inserir Dados (Sensores)")
        print("2. Executar Análise (Status Atual)")
        print("3. Histórico das Leituras")
        print("4. Encerrar Sistema")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == '1':
            limpar_tela()
            cadastrar_dados()
        elif opcao == '2':
            limpar_tela()
            if historico_leituras:
                print("--- RESULTADO DA ANÁLISE ---")
                analisar_missao(historico_leituras[-1])
            else:
                print("Insira dados primeiro para analisar!")
            input("\nPressione Enter para continuar...")
        elif opcao == '3':
            limpar_tela()
            exibir_historico()
        elif opcao == '4':
            print("Encerrando monitoramento da missão...")
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para tentar novamente...")


if __name__ == "__main__":
    menu_principal()