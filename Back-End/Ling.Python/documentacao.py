"""ARQUIVO DE DOCUMENTAÇÃO E DESCRIÇÃO DAS FUNCIONALIDADES DO PROJETO PARA ~>index.py"""
import uuid
from datetime import datetime, timedelta
from win10toast import ToastNotifier
import pandas

class SuperMarket:
    """Esta classe representa um Supermercado, onde os produtos serão armazenados e manipulados.
    \n>1. Em "SuperMercado", deve-se criar: uma método para menu de decisão, adição de produto,
    exibição de produto, exclusão de produto e averiguação de estado dos produtos.

    \n>2. Inicializar produtos perecíveis e não_perecíveis, como um dicionário.

    \n>3. Definir o tipo do produto: Perecível ou Não-Perecível.

    \n>4. Adicionar (p)'s e ~(p)'s à prateleira.

    \n>5. Prateleira deverá ser um dicionário contendo os produtos perecíveis e os não-perecíveis.

    Args:
        menu (function): Método para escolha do usuário.
        adicionar_produto (function): Método para adicionar produto.
        ver_prateleira (function): Método para exibir prateleira.
        procura_produto (function): Método para procurar produto.
        excluir_produto (function): Método para excluir produtos.
        averiguar_produto (function): Método para averiguar produtos.
    """
    #Implementação futura: Adaptar o código ao TKinter, ao ToastNotifier e ao banco de dados(MySQl)

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
        """Atributos de SuperMarket

        Args:
            itens_pereciveis (dict): Itens perecíveis
            itens_nao_pereciveis (dict): Itens não-perecíveis
            validade (str, optional): Prazo dos itens da prateleira. Defaults to None.
        """
        self.validade = validade or []
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

    def show_notificacao(self, titulo:str, mensagem:str, duracao=10):
        """Função para exibir um alerta.

        Args:
            titulo (str): Identificador da mensagem.
            mensagem (str): Conteúdo da notificação.
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

#Menu de decisão⬇️
    def menu(self):
        """Menu que contém as opções do usuário."""
        print("Menu")
        print("1. Adicionar produto")
        print("2. Ver prateleira")
        print("3. Procurar produto")
        print("4. Excluir produto")
        print("5. Averiguar prateleira")
        print("0. Encerrar o programa")
        confirmacao = int(input(">> "))

        return confirmacao

#Função para adicionar produto à prateleira⬇️
    def adicionar_produto(self, nome:str, quantidade=0, validade=None, price:float=0):
        """Adição de produto\n
        Método para a adição de um produto à prateleira.

        Args:
            nome (str): Objeto que representa o item da prateleira.
            categoria (str): Objeto que representa o tipo do item.
            quantidade (int): Quantidade de itens na prateleira.
            validade (str, optional): Vida-útil do item. Defaults to None.

        Returns: len(self.prateleira) += 1
        """
        validade = validade or []
        price = price if not str(price).isnumeric() else float(price)
        tamanho_dict = 0

        produto = {
            "Nome": [],
            "Quantidade": [],
            "Preço": price,
            "Validade": validade,
            "Categoria": "Perecível" or "Não-Perecível",
        }
        produto["Nome"].append(nome)
        produto["Quantidade"].append(quantidade)
        produto["Preço"].append(price)

        for produto in self.prateleira:
            tamanho_dict += 1
        print(tamanho_dict)

    def ver_prateleira(self):
        """Exibição de item/prateleira\n
            Exibe na tela os itens perecíveis e não_perecíveis ou

            a exibição individual dos itens perecíveis e não_perecíveis.

            Returns:
                Produtos da prateleira
        """
        df = pandas.DataFrame(self.prateleira.items())
        return df
        #OBRIGATÓRIO O USO DO PANDAS

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

                        df_pereciveis = pandas.DataFrame(self.prateleira["Perecíveis"]).iloc[[index_perecivel]]
                        print(df_pereciveis)

                    except ValueError:
                        print("Entrada inválida!")

                elif item in self.prateleira["Não-Perecíveis"]["Item"]:
                    try:
                        index_nao_perecivel = self.prateleira["Não-Perecíveis"]["Item"].index(item)

                        df_nao_perecivel = pandas.DataFrame(self.prateleira["Não-Perecíveis"]).iloc[[index_nao_perecivel]]
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

                        df_pereciveis_code = pandas.DataFrame(self.prateleira["Perecíveis"]).iloc[[index_perecivel_code]]
                        print(df_pereciveis_code)

                    except ValueError:
                        print("Entrada inválida!")

                elif code in self.prateleira["Não-Perecíveis"]["Código"]:
                    try:
                        index_nao_perecivel_code = self.prateleira["Não-Perecíveis"]["Código"].index(code)

                        df_nao_pereciveis_code = pandas.DataFrame(self.prateleira["Não-Perecíveis"]).iloc[[index_nao_perecivel_code]]
                        print(df_nao_pereciveis_code)

                    except ValueError:
                        print("Entrada inválida!")
                else:
                    print("Produto não encontrado!")

    def excluir_produto(self, nome, codigo):
        """Exclusão de produto\n
        Método de exclusão de um produto da prateleira.
        Args:
                nome (str): Objeto que representa o item da prateleira
                categoria (str): Objeto que representa o tipo do item

        Returns: len(prateleira) - 1
        """

    def averiguar_produto(self, estragavel=None, deterioravel=None):
        """Método para averiguação da prateleira e do produto."""
        #Define o estado dos produtos perecíveis e não-perecíveis
        estragavel = self.prateleira["Perecíveis"]
        deterioravel = self.prateleira["Não-Perecíveis"]
        data_atual = datetime.today()

        #Exibe os produtos pereciveis e não-pereciveis
        estragavel_df = pandas.DataFrame(estragavel)
        deterioravel_df = pandas.DataFrame(deterioravel)
        print(estragavel_df, "\n", deterioravel_df)

        try:
            #Verifica se o produto está estragando ou vencido
            if estragavel:
                estragavel["Validade"] = pandas.to_datetime(estragavel["Validade"])
                prod_estragando = estragavel["Validade"] <= data_atual
                prod_vencido = estragavel["Validade"] > data_atual

                #Notifica caso algum produto esteja estragando
                if prod_estragando:
                    self.show_notificacao("ALERTA", "Atente-se à validade dos produtos!")

                #Notifica caso algum produto esteja vencido
                if prod_vencido:
                    self.show_notificacao("ALERTA", "Produto vencido!")

            #Verifica se o produto está deteriorando
            if deterioravel:
                deterioravel["Validade"] = pandas.to_datetime(deterioravel["Validade"])
                validade = datetime.now() - timedelta(days=365)
                prod_deteriorando = deterioravel["Validade"] > validade

                #Notifica caso algum produto esteja deteriorando
                if prod_deteriorando:
                    self.show_notificacao("ALERTA", "Produto deteriorando!")

        except AttributeError:
            print("Nenhum produto cadastrado!")

        return estragavel, deterioravel

def main(au=None, asys=None):
    """Início do programa.
    \n* *Criar instância de 'SuperMercado'.*
    \n* *Chamar o Menu.*

    Args:
        au (Usuário): Objeto que representa o Usuário.
        asys (Sistema): Objeto que representa o Sistema.\n

            \n>## Execução Esperada

                >>>>>>>>DIAGRAMA DE SEQUÊNCIA

                |```asys ->Inicia o programa ➡️ asys ->Cria instância de SuperMarket```⬇️

                |```asys ->Abre Menu ➡️ asys ->Espera escolha do usuário```⬇️

                |```aU ->Escolhe uma opção[] ➡️ asys ->Chama adicionar_produto()```⬇️

                |```aU ->Insere produto[] ➡️ asys ->Adiciona produto à prateleira```⬇️

                |```asys ->Chama ver_Prateleira() ➡️ asys ->Exibe produtos na prateleira```⬇️

                |```asys ->Chama excluir_produto() ➡️ aU ->Escolhe produto a excluir[]```⬇️

                |```asys ->Remove produto ➡️ asys ->Chama averiguar_produto()```⬇️

                |```asys ->Verifica estado dos produtos ➡️ asys ->Exibe mensagem```⬇️

                |```aU ->Recebe feedback[] ➡️ asys ->Retorna ao Menu```⬇️\n
                |```asys ->Finaliza o programa```
    """

    mercado = SuperMarket(itens_nao_pereciveis={}, itens_pereciveis={})
    mercado.menu()

    asys = 8
    au = 4

    interacoes = asys + au
    print(f"O total de interações entre o Sistema(asys) e o Usuário(au) foi de {interacoes}")

if __name__ == "main":
    main(au=0, asys=0)
