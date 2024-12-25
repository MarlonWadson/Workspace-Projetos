#%% Jupyter
"""ARQUIVO PRINCIPAL"""
import uuid
import time
from datetime import datetime, timedelta
import customtkinter as ctk
from win10toast import ToastNotifier
from openpyxl import Workbook
import pandas as pd

class SuperMarket:
    """Esta classe representa um Supermercado, onde os produtos serão armazenados e manipulados."""
    def gerar_codigo(self) -> str:
        """Método para gerar o código de produto."""
        # GERADOR DO CÓDIGO
        code = str( uuid.uuid4().hex[:12])

        # PREFIXO DO CÓDIGO
        prefix = "PROD"

        #CÓDIGO GERADO
        codigo = f'{prefix}-{code}'

        return codigo

    def __init__(self, itens_pereciveis:dict, itens_nao_pereciveis:dict, validade=None):
        """Atributos do Supermercado

        Args:
            itens_pereciveis (dict): Itens perecíveis
            itens_nao_pereciveis (dict): Itens não-perecíveis
            validade (str, optional): Prazo dos itens da prateleira. Defaults to None.
        """
        validade = validade or []
        vencimento = datetime.today().date().strftime("%d/%m/%Y")

        self.itens_pereciveis = itens_pereciveis = {
            "Item": [],
            "Código": [],
            "Quantidade": [],
            "Preço": [],
            "Validade": validade,
            "Categoria": "Perecível"
        }

        self.itens_nao_pereciveis = itens_nao_pereciveis = {
            "Item": [],
            "Código": [],
            "Quantidade": [],
            "Preço": [],
            "Validade": vencimento,
            "Categoria": "Não-Perecível"
        }

        self.prateleira = {
            "Perecíveis": itens_pereciveis,
            "Não-Perecíveis": itens_nao_pereciveis
        }

    def show_notificacao(self, titulo, mensagem, duracao=10):
        """Função para exibir um alerta.\n>

            Args:
                titulo (str): Identificador da mensagem
                mensagem (str): Conteúdo da notificação
                duracao (int, optional): Duração da notificação. Defaults to 10.
        """
        notificacao = ToastNotifier()
        duracao = duracao is not None
        notificacao.show_toast(
            titulo,
            mensagem,
            icon_path=None,
            threaded=True
        )

    def menu(self):
        """Método para escolha do usuário."""
        while True:
            try:
                print("\nMenu Principal")
                print("O que desejas? Digite")
                print("1. Adicionar produto")
                print("2. Ver prateleira")
                print("3. Procurar produto")
                print("4. Excluir item da prateleira")
                print("5. Ver estado da prateleira")
                print("0.Encerrar")
                confirmacao = int( input("Confirme: "))
                print("\n")

                match confirmacao:
                    case 1:
                        self.adicionar_produto()

                    case 2:
                        self.exibir_prateleira()

                    case 3:
                        self.procurar_produto()

                    case 4:
                        self.excluir_produto()

                    case 5:
                        self.averiguar_produto()

                    case 0:
                        print("Saindo...")
                        time.sleep(3)
                        return
            except ValueError:
                print("Valor inserido inválido! Tente novamente.")
                time.sleep(2)

    def adicionar_produto(self):
        """Método para adição de produto."""
        print("O produto é perecível? Digite")
        print("1. Para confirmar")
        print("0. Para negar")
        confirmacao = int( input(">> "))

        #Se Perecível⬇️
        if confirmacao == 1:
            while True:
                item = input("\nAdicione um item: ").lower()
                code = self.gerar_codigo()
                qntd = int( input("Digite a quantidade do item: "))
                price = float( input("Digite o preço do item: R$"))
                validade = input("Digite a validade do item (DD/MM/AA): ")
                validade = datetime.strptime(validade, "%d/%m/%Y").date()

                self.prateleira["Perecíveis"]["Item"].append(item)
                self.prateleira["Perecíveis"]["Código"].append(code)
                self.prateleira["Perecíveis"]["Quantidade"].append(qntd)
                self.prateleira["Perecíveis"]["Preço"].append(price)
                self.prateleira["Perecíveis"]["Validade"].append(validade)

                if len(self.itens_pereciveis["Item"]) == 3:
                    break

            df = pd.DataFrame(self.prateleira["Perecíveis"])
            print("\n", df)

        #Se Não-Perecível⬇️
        elif confirmacao == 0:
            while True:
                tamanho = len(self.prateleira["Não-Perecíveis"]["Item"])
                item = input("\nDigite um item: ").lower()
                code = self.gerar_codigo()
                qntd = int( input("Digite a quantidade do item: "))
                price = float( input("Digite o preço do item: R$"))

                self.prateleira["Não-Perecíveis"]["Item"].append(item)
                self.prateleira["Não-Perecíveis"]["Código"].append(code)
                self.prateleira["Não-Perecíveis"]["Quantidade"].append(qntd)
                self.prateleira["Não-Perecíveis"]["Preço"].append(price)

                if len(self.itens_nao_pereciveis["Item"]) == 3: #<<<<<<<<<<<<<<TROCAR POR MODELO GENÉRICO>>>>>>>>>>>>>>>>>>>
                    break

            df = pd.DataFrame(self.prateleira["Não-Perecíveis"])
            print("\n", df)

        tamanho = 0
        for item in (self.prateleira["Perecíveis"]["Item"]):
            tamanho += len(self.prateleira["Perecíveis"]["Item"])
            break

        print("\nProdutos adicionados com sucesso!")
        print("Quantidade de produtos adicionados: ", tamanho)

    def exibir_prateleira(self):
        """Método para exibição da prateleira."""
        print("Exibição")
        print("1. Escolher tipo exibido")
        print("2. Exibir prateleira")
        confirmacao = int( input(">> "))
        print("\n")

        match confirmacao:
            #Exibição seletiva da prateleira
            case 1:
                print("Menu")
                print("3. Exibir itens perecíveis")
                print("4. Exibir itens não-perecíveis")
                confirmacao = int( input(">> "))

                if confirmacao == 3:
                    pereciveis_df = pd.DataFrame(self.prateleira["Perecíveis"])
                    print(pereciveis_df)

                    tamanho = 0
                    for item in self.prateleira["Perecíveis"]:
                        tamanho += len(self.prateleira["Perecíveis"]["Item"])
                        print("Quantidade de itens na prateleira: ", tamanho)
                        break

                elif confirmacao == 4:
                    nao_pereciveis_df = pd.DataFrame(self.prateleira["Não-Perecíveis"])
                    print(nao_pereciveis_df)

                    tamanho = 0
                    for item in self.prateleira["Não-Perecíveis"]:
                        tamanho += len(self.prateleira["Não-Perecíveis"]["Item"])
                        print("Quantidade de itens na prateleira: ", tamanho)
                        break

            #Exibição da prateleira
            case 2:
                if not self.itens_pereciveis and not self.itens_nao_pereciveis:
                    print("A prateleira está vazia")
                    print("Saindo da exibição...")
                    time.sleep(3)
                    self.menu()

                else:
                    pereciveis_df = pd.DataFrame(self.prateleira["Perecíveis"])
                    nao_pereciveis_df = pd.DataFrame(self.prateleira["Não-Perecíveis"])
                    tam_total = len(self.prateleira["Perecíveis"]["Item"]) + len(self.prateleira["Não-Perecíveis"]["Item"])
                    print("\n", pereciveis_df)
                    print("\n", nao_pereciveis_df)
                    print("\nQuantidade de itens na prateleira: ", tam_total)

    def procurar_produto(self):
        """Método para procurar produtos."""
        print("Procura")
        print("1. Sabe o nome do produto?")
        print("2. Sabe o código do produto?")
        confirmacao = int( input(">> "))
        print("\n")

        match confirmacao:
            #Caso sabe nome do produto
            case 1:
                item = input("Produto: ").lower()

                if item in self.prateleira["Perecíveis"]["Item"]:
                    try:
                        index_perecivel = self.prateleira["Perecíveis"]["Item"].index(item)

                        df_pereciveis = pd.DataFrame(self.prateleira["Perecíveis"]).iloc[[index_perecivel]]
                        print(df_pereciveis)

                    except ValueError:
                        print("Entrada inválida!")

                elif item in self.prateleira["Não-Perecíveis"]["Item"]:
                    try:
                        index_nao_perecivel = self.prateleira["Não-Perecíveis"]["Item"].index(item)

                        df_nao_perecivel = pd.DataFrame(self.prateleira["Não-Perecíveis"]).iloc[[index_nao_perecivel]]
                        print(df_nao_perecivel)

                    except ValueError:
                        print("Entrada inválida!")
                else:
                    print("Produto não encontrado!")

            #Caso sabe o código do produto
            case 2:
                code = input("Código: ")

                if code in self.prateleira["Perecíveis"]["Código"]:
                    try:
                        index_perecivel_code = self.prateleira["Perecíveis"]["Código"].index(code)

                        df_pereciveis_code = pd.DataFrame(self.prateleira["Perecíveis"]).iloc[[index_perecivel_code]]
                        print(df_pereciveis_code)

                    except ValueError:
                        print("Entrada inválida!")

                elif code in self.prateleira["Não-Perecíveis"]["Código"]:
                    try:
                        index_nao_perecivel_code = self.prateleira["Não-Perecíveis"]["Código"].index(code)

                        df_nao_pereciveis_code = pd.DataFrame(self.prateleira["Não-Perecíveis"]).iloc[[index_nao_perecivel_code]]
                        print(df_nao_pereciveis_code)

                    except ValueError:
                        print("Entrada inválida!")
                else:
                    print("Produto não encontrado!")

    def excluir_produto(self):
        """Método para exclusão de um produto"""
        print("Exclusão")
        print("1. Excluir produto perecível")
        print("2. Excluir produto não-perecível")
        confirmacao = int( input(">> "))

        #Excluir perecível
        if confirmacao == 1:
            item = input("\nProduto que será excluído: ").lower()
            code = input("Digite o código do produto: ")

            try:
                index = self.prateleira["Perecíveis"]["Código"].index(code)

                if self.prateleira["Perecíveis"]["Item"][index] == item:
                    self.prateleira["Perecíveis"]["Item"].pop(index)
                    self.prateleira["Perecíveis"]["Código"].pop(index)
                    self.prateleira["Perecíveis"]["Quantidade"].pop(index)
                    self.prateleira["Perecíveis"]["Preço"].pop(index)
                    self.prateleira["Perecíveis"]["Validade"].pop(index)

                    print(f"\nProduto, {item}, retirado da prateleira com sucesso!")
                    df = pd.DataFrame(self.prateleira["Perecíveis"])
                    print("\n", df)

                else:
                    print("Código inválido ou produto não encontrado!")

            except ValueError:
                print("Produto não corresponde ao código informado!")

        #Excluir não-perecível
        if confirmacao == 2:
            item = input("Produto que será excluído: ").lower()
            code = input("Código do produto: ")

            try:
                index = self.prateleira["Não-Perecíveis"]["Código"].index(code)

                if self.prateleira["Não-Perecíveis"]["Item"][index] == item:
                    if index != -1:
                        if self.prateleira["Não-Perecíveis"]["Item"][index] == item:
                            self.prateleira["Não-Perecíveis"]["Item"].pop(index)
                            self.prateleira["Não-Perecíveis"]["Código"].pop(index)
                            self.prateleira["Não-Perecíveis"]["Validade"].pop(index)

                            print(f"\nProduto, {item}, retirado da prateleira com sucesso!")
                            df = pd.DataFrame(self.prateleira["Não-Perecíveis"])
                            print("\n", df)

                    else:
                        print("Código inválido ou produto não encontrado!")

            except ValueError:
                print("Código não corresponde ao produto informado!")

    def averiguar_produto(self, estragavel=None, deterioravel=None):
        """Método para averiguação da prateleira e dos produtos."""
        data_atual = datetime.today()
        estragavel = pd.DataFrame(self.prateleira["Perecíveis"])
        deterioravel = pd.DataFrame(self.prateleira["Não-Perecíveis"])

        #Define o estado dos produtos perecíveis e não-perecíveis
        if self.prateleira["Perecíveis"]["Item"]:
            estragavel["Validade"] = pd.to_datetime(estragavel["Validade"])

            #Exibe os produtos pereciveis e não-pereciveis
            print(estragavel, "\n", deterioravel)

            #Verifica se o produto está estragando ou vencido
            if estragavel:
                prod_estragando = estragavel["Validade"] <= data_atual
                prod_vencido = estragavel["Validade"] > data_atual

            #Notifica caso algum produto esteja estragando
                if not prod_estragando.empty:
                    self.show_notificacao("ALERTA", "Há produtos próximos da validade!")
                    print("\nProdutos próximos da validade:")
                    print(prod_estragando)

            #Notifica caso algum produto esteja vencido
                if not prod_vencido.empty:
                    self.show_notificacao("ALERTA", "Há produtos vencidos!")
                    print("\nProdutos vencidos:")
                    print(prod_vencido)

        #Verifica se o produto está deteriorando
        if self.prateleira["Não-Perecíveis"]["Item"]:
            deterioravel["Validade"] = pd.to_datetime(deterioravel["Validade"])

            if deterioravel:
                validade = datetime.now() - timedelta(days=365)
                prod_deteriorando = deterioravel["Validade"] > validade

            #Notifica caso algum produto esteja deteriorando
                if not prod_deteriorando.empty:
                    self.show_notificacao("ALERTA", "Há produtos deteriorando!")
                    print("\nProdutos deteriorando:")
                    print(prod_deteriorando)
#IMPLEMENTANDO!

def main():
    """Início do programa."""
    mercado = SuperMarket(itens_pereciveis={}, itens_nao_pereciveis={})
    mercado.menu()

if __name__ == "__main__":
    main()
