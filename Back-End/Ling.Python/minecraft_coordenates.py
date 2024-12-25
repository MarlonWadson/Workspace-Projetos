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