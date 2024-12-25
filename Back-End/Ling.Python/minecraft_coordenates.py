"""Programa para guardar Coordenadas do Minecraft."""
import os
import time
import customtkinter as ctk
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base

AUTHOR = "Marlon"

db_path = os.path.join(os.path.dirname(__file__), "Coordenadas_Mine.db")
db = create_engine(f"sqlite:///{db_path}") #Criando o arquivo do BD
Base = declarative_base()

class Coordenadas(Base):
    """Classe de Coordenadas."""
    __tablename__ = "Coordenadas"
    server = Column('Servidor', String, primary_key=True)
    local = Column("Local", String)
    coor_x = Column("X", String)
    coor_y = Column("Y", String)
    coor_z = Column("Z", String)

    def __init__(self, server, local, coor_x, coor_y, coor_z) -> None:
        """Inicializa os atributos da classe.

        Args:
            server (string): Nome do servidor.
            local (string): Nome do local.
            coor_x (string): Coordenada X.
            coor_y (string): Coordenada Y.
            coor_z (string): Coordenada Z.
        """
        self.server = server
        self.local = local
        self.coor_x = coor_x
        self.coor_y = coor_y
        self.coor_z = coor_z

Base.metadata.create_all(bind=db)

Session = sessionmaker(bind=db)
session = Session()

def pegar_coordenadas(server, nome, coor_x, coor_y, coor_z) -> str:
    """Função para pegar as coordenadas do Minecraft."""
    coordenada = Coordenadas(server=server, local=nome, coor_x=coor_x, coor_y=coor_y, coor_z=coor_z)
    session.add(coordenada)
    session.commit()

    return f"Coordenadas de {nome} foram salvas com sucesso no servidor {server}!"

def main():
    """Início do programa."""
    while True:
        if AUTHOR == "" or AUTHOR is None:
            print("\nPor favor, defina o autor do programa na linha 2.\n")

        else:
            print(f"OBRIGADO PELA PREFERÊNCIA, {AUTHOR}!")
            print("Se deseja mudar o autor, vá para a linha 9.")
            time.sleep(3)
            print("\nIniciando o programa...\n")
            time.sleep(3)
            break

    janela = ctk.CTk()
    janela.title("Coletor de Coordenadas")
    janela.geometry("600x400")

    header = ctk.CTkLabel(janela, text="Coleta de Dados", font=("Times New Roman", 20))
    header.pack(pady=10)

    dados = ctk.CTkLabel(janela, text="")
    dados.pack(pady=10)

    server_entry = ctk.CTkEntry(janela, placeholder_text="Servidor")
    server_entry.pack(pady=5)

    local_entry = ctk.CTkEntry(janela, placeholder_text="Nome da coordenada")
    local_entry.pack(pady=5)

    coor_x_entry = ctk.CTkEntry(janela, placeholder_text="Coordenada X")
    coor_x_entry.pack(pady=5)

    coor_y_entry = ctk.CTkEntry(janela, placeholder_text="Coordenada Y")
    coor_y_entry.pack(pady=5)

if __name__ == "__main__":
    main()
