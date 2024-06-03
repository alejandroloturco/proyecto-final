from datetime import datetime
import mysql.connector
import json
import os
import random
from bson import json_util
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pydicom
import nltk
from spellchecker import SpellChecker
import spacy
import sys

def vaidacion_p(palabra):
    nlp = spacy.load('en_core_web_sm')
    spell = SpellChecker()    
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
    cursorSQL.execute("CREATE TABLE IF NOT EXISTS paciente (ID INT UNSIGNED PRIMARY KEY,ID_Cuidador INT UNSIGNED NOT NULL,Nombre VARCHAR(225) NOT NULL,Apellido VARCHAR(225) NOT NULL,Telefono VARCHAR(225) NOT NULL,Cedula VARCHAR(225) NOT NULL,Nacimiento VARCHAR(225) NOT NULL,Procedencia VARCHAR(225) NOT NULL,Fase VARCHAR(225) NOT NULL,Escolaridad VARCHAR(225) NOT NULL,Mano_dominante VARCHAR(225) NOT NULL,FOREIGN KEY (ID_Cuidador) REFERENCES cuidador(ID) ON UPDATE CASCADE ON DELETE CASCADE)")
    cursorSQL.execute("CREATE TABLE IF NOT EXISTS seguimiento (ID INT UNSIGNED PRIMARY KEY,ID_Paciente INT UNSIGNED NOT NULL,Fecha_Registro VARCHAR(225) NOT NULL,Pregunta_1 INT NOT NULL,Pregunta_2 INT NOT NULL,Pregunta_3 INT NOT NULL,Pregunta_4 INT NOT NULL,Pregunta_5 INT NOT NULL,Pregunta_6 INT NOT NULL,Pregunta_7 INT NOT NULL,Pregunta_8 INT NOT NULL,Pregunta_9 INT NOT NULL,Pregunta_10 INT NOT NULL,FOREIGN KEY (ID_Paciente) REFERENCES paciente(ID) ON UPDATE CASCADE ON DELETE CASCADE)")
    desconectar_SQL(cnx,cursorSQL)
    
def obtener_dataSQL():
    cursorSQL, cnx = conectar_SQL()
    listcui = []
    listpac = []
    listreg = []
    cuidador = "SELECT * FROM  cuidador"
    pacientes = "SELECT * FROM  paciente"
    seguimiento = "SELECT * FROM seguimiento"
    cursorSQL.execute(cuidador)
    resultado = cursorSQL.fetchall()    
    for i in resultado:
        diccui = {}
        diccui = {
            "ID": (i[0]),
            "Nombre": (i[1]),
            "Apellido": (i[2]),
            "Telefono": (i[3]),
            "Cedula": (i[4]),
            "Formacion": (i[5]),
            "Usuario": (i[6]),
            "Contraseña": (i[7])
            }
        listcui.append(diccui)       
    cursorSQL.execute(pacientes)
    resultado = cursorSQL.fetchall()
    for i in resultado:
            dicpac = {}
            dicpac = {
                "ID": (i[0]),
                "ID_Cuidador": (i[1]),
                "Nombre": (i[2]),
                "Apellido": (i[3]),
                "Telefono": (i[4]),
                "Cedula": (i[5]),
                "Nacimiento": (i[6]),
                "Procedencia": (i[7]),                                             
                "Fase": (i[8]),
                "Escolaridad": (i[9]),
                "Mano_Dominante": (i[10])
                }
            listpac.append(dicpac) 
    cursorSQL.execute(seguimiento)
    resultado = cursorSQL.fetchall()
    for i in resultado:
            dichm = {}
            dichm = {
                "ID": (i[0]),
                "ID_Paciente": (i[1]),
                "Fecha_Registro": (i[2]),
                "Pregunta_1": (i[3]),
                "Pregunta_2": (i[4]),
                "Pregunta_3": (i[5]),
                "Pregunta_4": (i[6]),
                "Pregunta_5": (i[7]),
                "Pregunta_6": (i[8]),
                "Pregunta_7": (i[9]),
                "Pregunta_8": (i[10]),
                "Pregunta_9": (i[11]),
                "Pregunta_10": (i[12]),
                "Pregunta_11": (i[13]),
                "Pregunta_12": (i[14]),
                "Pregunta_13": (i[15]),
                "Pregunta_14": (i[16]),
                "Pregunta_15": (i[17]),
                "Pregunta_16": (i[18]),
                "Pregunta_17": (i[19])             
                }
            listreg.append(dichm) 
    desconectar_SQL(cnx,cursorSQL)
    return listcui, listpac, listreg
    
def imagenes():
    path = 'C:/Users/Usuario/Downloads/Proyecto/Proyecto/imagenes'
    imagenes = os.listdir(path)
    return imagenes

class Cuidador:
    def __init__(self,listcui):
        self._listcui = listcui
            
    def SetNombre(self,n):
        self._nombre = n
    def SetCedula(self,n):
        self._cedula = n
    def SetNumero(self,n):
        self._numero = n
    def SetEmail(self,n):
        self._email = n
    def SetOcupacion(self,n):
        self._ocupacion = n
    
    def GetNombre(self):
        return self._nombre
    def GetNumero(self):
        return self._numero 
    def GetEmail(self):
        return self._email 
    def GetOcupacion(self):
        return self._ocupacion 
    
    def validar_usuario(self, usuario, contrasena):
        for i in range(len(self._listcui)):
                if self._listcui[i]["Usuario"] == usuario and self.cuidador.listcui[i]["Contraseña"] == contrasena:
                    return True
        return False
  
class Paciente(Cuidador):
    def __init__(self, listpac):
        self._listpac = listpac
    
    def SetEdad(self,n):
        self._edad = n
    def SetResidencia(self,r):
        self._residencia = r
    def SetNacimiento(self,n):
        self._nacimiento = n
    def SetFase(self,f):
        self._fase = f
    def SetEstudio(self,e):
        self._estudio = e
    def SetDominancia(self,d):
        self._dominancia = d
    def SetTiempoalz(self,t):
        self._tiempoalz = t
    
    def GetEdad(self):
        return self._edad
    def GetResidencia(self):
        return self._residencia 
    def GetNacimiento(self):
        return self._nacimiento 
    def GetFase(self):
        return self._fase 
    def GetEstudio(self):
        return self._estudio
    def GetDominancia(self):
        return self._dominancia 
    def GetTiempoalz(self):
        return self._tiempoalz


class Seguimiento:
    def __init__(self, listreg):
        self._listreg = listreg


        
        
