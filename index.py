from tkinter import*
from tkinter import ttk,Tk
from tkinter import messagebox
import pymongo

MONGO_HOST = "localhost"
MONGO_PORT = "27017"
MONGO_Tiempo_Fuera= 1000

MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/"

MONGO_BASEDATOS="clavistel"
MONGO_COLECCION="planesContratados"
cliente=pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_Tiempo_Fuera)

MibaseDatos= cliente[MONGO_BASEDATOS]
MiColeccion=MibaseDatos[MONGO_COLECCION]

while True:
    print("Registro de clientes con productos Clavistel")
    print("Menu")
    print("1. Crear documento de cliente nuevo")
    print("2. Leer documentos de clientes")
    print("3. Actualizar documento de cliente")
    print("4. Eliminar documento de cliente")
    print("5. Salir")

    opcion= int(input("Elige una opción: "))

#Funciones
    #Crear documento
    if opcion==1:
        rut = int(input("Rut sin digito verificador: "))
        nombre= input("Nombre: ")
        direccion= input("Dirección: ")
        opcion = int(input("Producto contratado: \n1. Plan de internet\n2. Plan de telefonía\n3. Plan de televisión\n4. Plan de internet + telefonía\n5. Plan de internet + televisión\n6. Plan de telefonía + televisión\n7. Plan de internet + telefonía + televisión\nElige una opción: "))
        if opcion==1:
            productoContratado = "Plan de internet"
        elif opcion==2:
            productoContratado = "Plan de telefonía"
        elif opcion==3:
            productoContratado = "Plan de televisión"
        elif opcion==4:
            productoContratado = "Plan de internet + telefonía"
        elif opcion==5:
            productoContratado = "Plan de internet + televisión"
        elif opcion==6:
            productoContratado = "Plan de telefonía + televisión"
        elif opcion==7:
            productoContratado = "Plan de internet + telefonía + televisión"
        nuevo_documento={
        "rut": rut,
        "nombre": nombre,
        "direccion": direccion,
        "productoContratado": productoContratado
        }
        MiColeccion.insert_one(nuevo_documento)

    elif opcion==2:
        #Leer documentos
        print("Documentos en la coleccion planesContratados: ")
        documentos= MiColeccion.find()
        for documento in MiColeccion.find():
            print(documento)

    elif opcion==3:
        #Actualizar documento
        rut = int(input("Rut sin digito verificador del cliente a actualizar: "))
        nuevo_nombre= input("Nuevo nombre: ")
        nueva_direccion= input("Nueva dirección: ")
        opcion = int(input("Nuevo producto contratado: \n1. Plan de internet\n2. Plan de telefonía\n3. Plan de televisión\n4. Plan de internet + telefonía\n5. Plan de internet + televisión\n6. Plan de telefonía + televisión\n7. Plan de internet + telefonía + televisión\nElige una opción: "))
        if opcion==1:
            productoContratado = "Plan de internet"
        elif opcion==2:
            productoContratado = "Plan de telefonía"
        elif opcion==3:
            productoContratado = "Plan de televisión"
        elif opcion==4:
            productoContratado = "Plan de internet + telefonía"
        elif opcion==5:
            productoContratado = "Plan de internet + televisión"
        elif opcion==6:
            productoContratado = "Plan de telefonía + televisión"
        elif opcion==7:
            productoContratado = "Plan de internet + telefonía + televisión"
        MiColeccion.update_one({"rut": rut}, {"$set": {"nombre": nuevo_nombre, "direccion": nueva_direccion, "productoContratado": nuevo_productoContratado}})
        print("Documento actualizado")

    elif opcion==4:
        #Eliminar documento
        rut = int(input("Rut sin digito verificador del cliente a eliminar: "))
        MiColeccion.delete_one({"rut": rut})
        print("Documento eliminado")

    elif opcion==5:
        break