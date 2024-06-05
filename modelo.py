from datetime import datetime
import mysql.connector
import json
import os
import random
from bson import json_util
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
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
    cursorSQL.execute("CREATE TABLE IF NOT EXISTS paciente (ID INT UNSIGNED PRIMARY KEY,ID_Cuidador INT UNSIGNED NOT NULL,Nombre VARCHAR(225) NOT NULL,Apellido VARCHAR(225) NOT NULL,Edad VARCHAR(225) NOT NULL,Telefono VARCHAR(225) NOT NULL,Cedula VARCHAR(225) NOT NULL,Nacimiento VARCHAR(225) NOT NULL,Procedencia VARCHAR(225) NOT NULL,Fase VARCHAR(225) NOT NULL,Escolaridad VARCHAR(225) NOT NULL,Mano_dominante VARCHAR(225) NOT NULL,Tiempo_Alz VARCHAR(225) NOT NULL,FOREIGN KEY (ID_Cuidador) REFERENCES cuidador(ID) ON UPDATE CASCADE ON DELETE CASCADE)")
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
                "Edad": (i[4]),
                "Telefono": (i[5]),
                "Cedula": (i[6]),
                "Nacimiento": (i[7]),
                "Procedencia": (i[8]),                                             
                "Fase": (i[9]),
                "Escolaridad": (i[10]),
                "Mano_Dominante": (i[11])
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
                "Pregunta_10": (i[12])         
                }
            listreg.append(dichm) 
    desconectar_SQL(cnx,cursorSQL)
    return listcui, listpac, listreg

def añadir_cuidador(nombre,apellido,telefono,cedula,formacion,usuario,contraseña, listcui):
    '''Se ingresa un cuidador a la base de datos'''
    try:            
        cursorSQL, cnxSQL = conectar_SQL()
        listdatareg = []
        listus = ()        
        listus = (len(listcui),nombre,apellido,telefono,cedula,formacion,usuario,contraseña)
        listdatareg.append(listus)
        cursorSQL.executemany("""INSERT INTO cuidador (ID, Nombre, Apellido, Telefono, Cedula, Formacion, Usuario, Contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", listdatareg)
        desconectar_SQL(cnxSQL,cursorSQL)
        return True
    except: 
        print("Dato ingresado no valido")

def añadir_paciente(id_cuidador,nombre,apellido,edad,telefono,cedula,nacimiento,procedencia,fase,escolaridad,mano_dominante,tiempo_alz, listpac):
    '''Se ingresa un paciente a la base de datos'''
    #try:            
    cursorSQL, cnxSQL = conectar_SQL()
    listdatareg = []
    listus = ()        
    listus = (len(listpac),id_cuidador,nombre,apellido,edad,telefono,cedula,nacimiento,procedencia,fase,escolaridad,mano_dominante,tiempo_alz)
    listdatareg.append(listus)
    cursorSQL.executemany("""INSERT INTO paciente (ID, ID_Cuidador, Nombre, Apellido, Edad, Telefono, Cedula, Nacimiento, Procedencia, Fase, Escolaridad, Mano_dominante, Tiempo_Alz) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", listdatareg)
    desconectar_SQL(cnxSQL,cursorSQL)
    return True
    #except: 
    #    print("Dato ingresado no valido")

def añadir_respuestas(id,fecha,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10):    
    '''Se ingresan las respuestas de las 10 preguntas en fio'''
    try:            
        cursorSQL, cnxSQL = conectar_SQL()
        listdatareg = []
        listus = ()        
        listus = (id,fecha,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)
        listdatareg.append(listus)
        cursorSQL.executemany("""INSERT INTO seguimiento (ID_Paciente, Fecha_Registro, Pregunta_1, Pregunta_2, Pregunta_3, Pregunta_4, Pregunta_5, Pregunta_6, Pregunta_7, Pregunta_8, Pregunta_9, Pregunta_10) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", listdatareg)
        desconectar_SQL(cnxSQL,cursorSQL)
        return True
    except: 
        print("Dato ingresado no valido")
    
    
class Cuidador:
    def __init__(self,listcui):
        self._listcui = listcui

    def get_listcui(self):
        return self._listcui
    
    def validar_usuario(self, usuario, contrasena):
        for i in range(len(self._listcui)):
                if self._listcui[i]["Usuario"] == usuario and self._listcui[i]["Contraseña"] == contrasena:
                    return True
        return False

    def registro_cuidador(self, nombre, apellido, telefono, cedula, formacion, usuario, contraseña):
        self._listcui.append({"ID": len(self._listcui)+1, "Nombre": nombre, "Apellido": apellido, "Telefono": telefono, "Cedula": cedula, "Formacion": formacion, "Usuario": usuario, "Contraseña": contraseña})
        if añadir_cuidador(nombre,apellido,telefono,cedula,formacion,usuario,contraseña, self._listcui):
            return True
        else:
            return False
  
class Paciente(Cuidador):
    def __init__(self, listpac):
        self._listpac = listpac

    def get_listpac(self):
        return self._listpac
    
    def registro_paciente(self, nombre, apellido, edad, telefono, cedula, residencia, nacimiento, fase, estudio, dominancia, tiempoalz, listcui):
        ID_cuidador = listcui[-1]["ID"]
        self._listpac.append({"ID": len(self._listpac)+1, "ID_Cuidador": ID_cuidador , "Nombre": nombre, "Apellido": apellido, "Edad": edad, "Telefono": telefono, "Cedula": cedula, "Nacimiento": nacimiento, "Procedencia": residencia, "Fase": fase, "Escolaridad": estudio, "Mano_Dominante": dominancia, "Tiempo_Alz": tiempoalz})
        if añadir_paciente(ID_cuidador,nombre,apellido,edad,telefono,cedula,nacimiento,residencia,fase,estudio,dominancia,tiempoalz, self._listpac):
            return True
        else:
            return False
        
class Seguimiento:
    def __init__(self, listreg):
        self._listreg = listreg
    
    def get_listreg(self):
        return self._listreg
    
    def registro_seguimiento(self, id, fecha, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        self._listreg.append({"ID": len(self._listreg)+1, "ID_Paciente": id, "Fecha_Registro": fecha, "Pregunta_1": p1, "Pregunta_2": p2, "Pregunta_3": p3, "Pregunta_4": p4, "Pregunta_5": p5, "Pregunta_6": p6, "Pregunta_7": p7, "Pregunta_8": p8, "Pregunta_9": p9, "Pregunta_10": p10})
        añadir_respuestas(id,fecha,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)

