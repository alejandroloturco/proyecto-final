from datetime import datetime
import mysql.connector
import json
import os
import pymongo
import random
from bson import json_util
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pydicom
import nltk
from spellchecker import SpellChecker
import spacy

nlp = spacy.load('en_core_web_sm')

spell = SpellChecker()

def es_valida(palabra):
    
    if spell.correction(palabra) != palabra:
        return False

    if not palabra.lower().startswith('p'):
        return False

    doc = nlp(palabra)
    token = doc[0]

    if token.pos_ == 'NOUN':
        return False
    if token.pos_ == 'VERB' and token.tag_ != 'VB':
        return False

    if token.tag_ not in ['VB', 'JJ', 'RB']: 
        return False

    return True

palabras = ["poder", "parando", "paciente", "parto", "pienso", "pulir", "pintar"]

palabras_validas = [palabra for palabra in palabras if es_valida(palabra)]

print("Palabras válidas:", palabras_validas)



def crear_BDSQL():
    cnx = mysql.connector.connect(
        user='root',
        password='',
        host='localhost'
    )
    cursorSQL = cnx.cursor()
    cursorSQL.execute('CREATE DATABASE IF NOT EXISTS alzcare;')
    cursorSQL.execute("CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY '1234';")
    cursorSQL.execute("GRANT ALL PRIVILEGES ON alzcare.* TO 'admin'@'localhost';")
    cursorSQL.close()
    cnx.close()
def conectar_SQL():
    SERVIDOR = 'localhost'
    USUARIO = 'admin'
    CONTRASEÑA = '1234'
    DB  = 'alzcare'
    cnx = mysql.connector.connect(user=USUARIO,password=CONTRASEÑA,host=SERVIDOR,database=DB)
    cursorSQL = cnx.cursor()
    return cursorSQL,cnx
def desconectar_SQL(cnx,cursor):
    cnx.commit()
    cursor.close()
    cnx.close()
def crear_tablasSQL():
    cursorSQL, cnx = conectar_SQL()
    cursorSQL.execute("USE alzcare;")
    cursorSQL.execute("CREATE TABLE IF NOT EXISTS cuidador (ID INT UNSIGNED PRIMARY KEY,Nombre VARCHAR(225) NOT NULL,Apellido VARCHAR(225) NOT NULL,Telefono VARCHAR(225) NOT NULL,Cedula VARCHAR(225) NOT NULL,Formacion VARCHAR(225) NOT NULL,Usuario VARCHAR(225) NOT NULL,Contraseña VARCHAR(225) NOT NULL)")
    cursorSQL.execute("CREATE TABLE IF NOT EXISTS paciente (ID INT UNSIGNED PRIMARY KEY,ID_Cuidador INT UNSIGNED NOT NULL,Nombre VARCHAR(225) NOT NULL,Apellido VARCHAR(225) NOT NULL,Nacimiento VARCHAR(225) NOT NULL,Procedencia VARCHAR(225) NOT NULL,Fase VARCHAR(225) NOT NULL,Escolaridad VARCHAR(225) NOT NULL,Mano_dominante VARCHAR(225) NOT NULL,FOREIGN KEY (ID_Cuidador) REFERENCES cuidador(ID) ON UPDATE CASCADE ON DELETE CASCADE)")
    cursorSQL.execute("CREATE TABLE IF NOT EXISTS registro (ID INT UNSIGNED PRIMARY KEY,ID_Paciente INT UNSIGNED NOT NULL,Fecha_Registro VARCHAR(225) NOT NULL,Pregunta_1 INT NOT NULL,Pregunta_2 INT NOT NULL,Pregunta_3 INT NOT NULL,Pregunta_4 INT NOT NULL,Pregunta_5 INT NOT NULL,Pregunta_6 INT NOT NULL,Pregunta_7 INT NOT NULL,Pregunta_8 INT NOT NULL,Pregunta_9 INT NOT NULL,Pregunta_10 INT NOT NULL,Pregunta_11 INT NOT NULL,Pregunta_12 INT NOT NULL,Pregunta_13 INT NOT NULL,Pregunta_14 INT NOT NULL,Pregunta_15 INT NOT NULL,Pregunta_16 INT NOT NULL,Pregunta_17 INT NOT NULL,FOREIGN KEY (ID_Paciente) REFERENCES paciente(ID) ON UPDATE CASCADE ON DELETE CASCADE)")
    desconectar_SQL(cnx,cursorSQL)
class Cuidador:

    def __init__(self, ID, Nombre, Apellido, Telefono, Cedula, Formacion, Usuario, Contraseña):
        self.ID = ID
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Telefono = Telefono
        self.Cedula = Cedula
        self.Formacion = Formacion
        self.Usuario = Usuario
        self.Contraseña = Contraseña

