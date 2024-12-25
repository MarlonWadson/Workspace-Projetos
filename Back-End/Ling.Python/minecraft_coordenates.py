"""Pegar Coordenadas do Minecraft."""
#---------Imports
import os
import time
import customtkinter as ctk
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base

#---------Declarações Globais
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

#Criando as tabelas no BD
Base.metadata.create_all(bind=db)

#Conectando com o BD
Session = sessionmaker(bind=db)
session = Session()