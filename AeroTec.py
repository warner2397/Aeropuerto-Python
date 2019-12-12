import random
import pickle
from datetime import datetime, timedelta
import tkinter as tk

"""global lists of each class"""
global listaUsu
global listPista
global listPuerta
global listAerolinea
global listTripu
global listAvion
global listAeropuerto
global listVuelos
global listHitorial
listHitorial = list()
#global condigo

class Administrador(object):  # """Admin class and its attributes"""
    def __init__(self, cedula, nombre, edad, email, contra, tipo):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.contra = contra
        self.tipo = tipo

class Pasajero(object):  # """Pasajero class and its attributes"""
    def __init__(self, idPasaporte, nombre, edad, email, contra, tipo):
        self.idPasaporte = idPasaporte
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.contra = contra
        self.tipo = tipo


class Pista(object):  # """Pista class and its attributes"""
    def __init__(self, numPista, estado):
        self.numPista = numPista
        self.estado = estado

    def getnumepist(self):
        return self.numPista


class Puerta(object):  # Puerta class and its attributes
    def __init__(self, numPuerta, estado):
        self.numPuerta = numPuerta
        self.estado = estado

    def getnumepuer(self):
        return self.numPuerta


class Aerolinea(object):  # Aerolinea class and its attributes
    def __init__(self, nomAero, annoFund, tipoAero, cantPaises):
        self.nomAero = nomAero
        self.annoFund = annoFund
        self.tipoAero = tipoAero
        self.cantPaises = cantPaises


class Tripulacion(object):  # Tripulacion class and its attributes
    def __init__(self, nombre, fecha, idAerolinea, puestoTrabajo, estado, indentificacion):
        self.nombre = nombre
        self.fecha = fecha
        self.idAerolinea = idAerolinea
        self.puestoTrabajo = puestoTrabajo
        self.estado = estado
        self.identificacion = indentificacion

    def getNombre(self):
        return self.nombre


class Avion(object):  # Avion class and its attributes
    def __init__(self, idAvion, modeloAvion, annoContruc, aerolineaPertenece, capacidadPasajeros, estado, contador):
        self.idAvion = idAvion
        self.modeloAvion = modeloAvion
        self.annoConstruc = annoContruc
        self.aerolineaPertenece = aerolineaPertenece
        self.capacidadPasajeros = capacidadPasajeros
        self.estado = estado
        self.contador = contador

    def getAvi(self):
        return self.idAvion


class Aeropuerto(object):  # Aeropuerto class and its attributes
    def __init__(self, idAero, nombreAero, ciudad, pais):
        self.idAero = idAero
        self.nombreAero = nombreAero
        self.ciudad = ciudad
        self.pais = pais

    def getAero(self):
        return self.nombreAero


class Vuelos:  # Vuelos class and its attributes
    p = Tripulacion

    def __init__(self, aerolinea, fechaSalida, fechaLlegada, horaSalida, horaLlegada, aeropuertoSalida,
                 aeropuertoLlegada, id, pista, puerta, avion, t1, t2, t3, t4, t5, precio, duracion):
        self.aerolinea = aerolinea
        self.fechaSalida = fechaSalida
        self.fechaLlegada = fechaLlegada
        self.horaSalida = horaSalida
        self.horaLlegada = horaLlegada
        self.aeropuertoSalida = aeropuertoSalida
        self.aeropuertoLlegada = aeropuertoLlegada
        self.id = id
        self.pista = pista
        self.puerta = puerta
        self.avion = avion
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.precio = precio
        self.duracion = duracion

    def __str__(self):
        return "%i - %s" % (self.precio, self.aeropuertoSalida)


class Historial:
    def __init__(self, horaSalida, aeroSalida, aeroLlegada, fechSalida, precio, duracion, tipo, escala1, escala2,
                 horaLlega, codigo):
        self.horaSalida = horaSalida
        self.aeroSalida = aeroSalida
        self.aeroLlegada = aeroLlegada
        self.fechSalida = fechSalida
        self.precio = precio
        self.duracion = duracion
        self.tipo = tipo
        self.escala1 = escala1
        self.escala2 = escala2
        self.horaLlega = horaLlega
        self.codigo = codigo

    def __str__(self):
        return "%i - %s" % (self.precio, self.aeroSalida)

archivoVuelos = open("losVuelos", "rb")
listVuelos = pickle.load(archivoVuelos)  # Cargar los vuelos para leer
archivoVuelos.close()


archivoTripu = open("losTripu", "rb")
listTripu = pickle.load(archivoTripu)  # Cargar los vuelos para leer
archivoTripu.close()

"""archivoUsuario = open("losUsuarios", "wb")
pickle.dump(listaUsu, archivoUsuario)
archivoUsuario.close()
del(archivoUsuario)"""

archivoUsuario = open("losUsuarios", "rb")
listaUsu = pickle.load(archivoUsuario)  # Cargar los vuelos para leer
archivoUsuario.close()

archivoAeropuerto = open("losAeropuertos", "rb")
listAeropuerto = pickle.load(archivoAeropuerto)  # Cargar los vuelos para leer
archivoAeropuerto.close()

archivoAerolinea = open("lasAerolineas", "rb")
listAerolinea = pickle.load(archivoAerolinea)  # Cargar los vuelos para leer
archivoAerolinea.close()

archivoPuertas = open("lasPuertas", "rb")
listPuerta = pickle.load(archivoPuertas)  # Cargar los vuelos para leer
archivoPuertas.close()

archivoPistas = open("lasPistas", "rb")
listPista = pickle.load(archivoPistas)  # Cargar los vuelos para leer
archivoPistas.close()

archivoAvion = open("losAviones", "rb")
listAvion = pickle.load(archivoAvion)  # Cargar los vuelos para leer
archivoAvion.close()


def crearAdmin():  # regist administrador

    print("\n-------------------------\n"
          " Registro de Administrador \n"
          "---------------------------\n")

    cedula = input("Ingrese su numero de cedula: ")
    nombre = input("Escriba su nombre: ")
    edad = input("Escriba su edad: ")
    email = input("Escriba su correo electronico: ")
    contra = input("Escriba su contraseña: ")
    tipo = True
    datos = None
    a = Administrador(cedula, nombre, edad, email, contra, tipo)

    for q in listaUsu:

        if hasattr(q, 'cedula'):  # validate if data is there
            datos = q.cedula

        if cedula == datos:
            print('usuario existente en el sistema!. Vuelva a ingresar los datos!')
            break

    else:

        listaUsu.append(a)
        while True:  # create another account or return to the menu
            n = (input("Usuario registrado!\n\n"
                       "[1].-Registrar otro usuario\n"
                       "[2].-Volver al login\n"
                       "Seleccione una opción: "))

            if n == "1":
                crearPasajero()
            elif n == "2":
                menu()


def crearPasajero():  # registration of pasajero

    print("\n---------------------\n"
          "Registro de Usuario\n"
          "---------------------\n")
    idPasaporte = input("Ingrese su numero de pasaporte: ")
    nombre = input("Escriba su nombre: ")
    edad = input("Escriba su edad: ")
    email = input("Escriba su correo electronico: ")
    contra = input("Escriba su clave: ")
    tipo = False
    datos = None
    p = Pasajero(idPasaporte, nombre, edad, email, contra, tipo)

    for q in listaUsu:
        if hasattr(q, 'idPasaporte'):  # validate if data is there
            datos = q.idPasaporte
        if idPasaporte == datos:
            print('El usuario ya existe en el sistema, vuelva a intentarlo')
            crearPasajero()

    else:
        listaUsu.append(p)
        compraVuelos = open(idPasaporte + ".txt", "w")
        compraVuelos.close()
        while True:  # create another account, or return to the menu
            n = (input("Usuario registrado!\n\n"
                       "[1].-Registrar otro usuario\n"
                       "[2].-Volver al login\n"
                       "Seleccione una opción: "))
            if n == "1":
                crearPasajero()
            elif n == "2":
                menu()


def menu():
    print('\n-*-*-*-*-*BIEVENIDOS AEROTEC-*-*-*-*-*-\n')
    while True:
        opcion = input(
            "1.-registrarse\n"
            "2.-Ingresar\n"
            'Digite la accion que desea realizar: ')

        if opcion == "1":
            tipoUsu()
        elif opcion == "2":
            iniSecion()


def tipoUsu():  # type of user that you want to enter

    while True:
        cualUsu = input("""Usuario que desea registrar\n
        [1]-Administrador\n
        [2]-Usuario\n
        Indique que desea regitrar: """)
        if cualUsu == "1":
            crearAdmin()
        elif cualUsu == "2":
            crearPasajero()


def iniSecion():  # Start of secion
    global usuario
    while True:
        usuario = (input("Usuario: "))
        contra = (input("Contraseña: "))

        for u in listaUsu:
            if hasattr(u, 'cedula'):  # validate what data is there
                datos = u.cedula
            else:
                datos = u.idPasaporte
            if usuario == datos and contra == u.contra:  # validator of the login
                if u.tipo == True:  # validate if it is admin or user
                    menuPrincipal()

                else:
                    menuUsuario()
        else:

            print('\ndatos incorrectos!\n'
                  'vuelva a ingresarlos.!\n')
            iniSecion()


def menuUsuario():  # menu del usuario
    print("\n<<<<BIENVENIDO>>>>\n")

    p = input('[1]-BUSQUEDA DE VUELOS\n'
              '[2]-BUSQUEDA VUELOS INTELIGENTE\n'
              "{3]-salir"
              '>>>')
    if p == "1":
        busqVuelos()
    elif p == "2":
        busqVuelos2()
    else:
        menu()


def busqVuelos2():
    p = input("\n[1]-DIRECTO\n"
              "\n[2]-CON ESCALA\n"
              "\n[3]-VOLVER\n"
              ">>>")
    if p == "1":
        vuelosInteligentes()
    elif p == "2":
        vuelosInteligentesEscalas()
    menuUsuario()


def vuelosInteligentesEscalas():  # veo vuelos con un rango de fechas
    # listVuelos.sort(key=lambda Vuelos: Vuelos.precio)
    print("\nBUSQUEDA DE VUELOS INTELIGENTES CON ESCALAS\n")
    fecha = input('Ingrese la fecha vuelo, AAAA-MM-DD: ')
    date = datetime.strptime(fecha, "%Y-%m-%d")
    rango = int(input('Ingrese el rango de días para buscar el vuelo: '))
    fechSuma = date + timedelta(days=rango)
    fechResta = date - timedelta(days=rango)

    fechaComp1 = datetime.strftime(fechSuma, "%Y-%m-%d")
    fechaComp2 = datetime.strftime(fechResta, "%Y-%m-%d")

    aSalida = input('Ingrese el aeropuerto de salida ')
    aLlegada = input('Ingrese el aeropuerto de llegada: ')
    cont = 0
    codigo = 0

    for p in listVuelos:
        fechaComparar = p.fechaSalida
        if cont == 5:
            break
        if fechaComparar >= fechaComp2 and fechaComparar <= fechaComp1:
            if p.aeropuertoSalida == aSalida:

                for l in listVuelos:
                    if cont == 5:
                        break
                    if p.aeropuertoLlegada == l.aeropuertoSalida and p.fechaSalida == l.fechaLlegada and p.horaLlegada < l.horaSalida and l.aeropuertoSalida != p.aeropuertoSalida:

                        for q in listVuelos:
                            if l.aeropuertoLlegada == q.aeropuertoSalida and l.horaLlegada < q.horaSalida and l.aeropuertoSalida != p.aeropuertoSalida:
                                if q.aeropuertoLlegada == aLlegada and p.fechaLlegada == q.fechaLlegada:

                                    codigo += 1
                                    totalPrecio = (p.precio + l.precio + q.precio) / 4
                                    duracion = p.duracion + l.duracion + q.duracion + 3
                                    tipo = "Vuelo con escala"

                                    v = Historial(p.horaSalida, aSalida, aLlegada, p.fechaSalida, totalPrecio,
                                                  duracion, tipo, l.aeropuertoSalida, q.aeropuertoSalida, q.horaLlegada,
                                                  codigo)

                                    cont += 1
                                    listHitorial.append(v)

                                    if cont == 5:
                                        break

    listHitorial.sort(key=lambda Historial: Historial.precio)
    for k in listHitorial:
        print("\nCodigo: ", k.codigo,
              "\nTipo: ", k.tipo,
              "\n Fecha salida: ", k.fechSalida,
              "\nHora salida: ", k.horaSalida,
              "\nAero salida: ", k.aeroSalida,
              "\nAero Destino: ", k.aeroLlegada,
              "\nEscala1: ", k.escala1,
              "\nEscala2: ", k.escala2,
              "\nHora llegada: ", k.horaLlega,
              "\nDuracion: ", k.duracion,
              "\nPrecio: ", k.precio)

    compra = input("\n[1]-Comprar vuelo\n"  # usuario decide si comprar el Vuelo o no!
                   "[2]-volver\n"
                   ">>>")
    if compra == "1":
        while True:
            pasaporte = input('Ingrese su numero de pasaporte: ')
            if usuario == pasaporte:

                dr = int(input('Ingrese el codigo del vuelo: '))

                for i in listHitorial:
                    i.precio = str(i.precio)
                    i.duracion = str(i.duracion)

                compraVuelos = open(pasaporte + ".txt", "a")
                for l in listHitorial:
                    if dr == l.codigo:
                        text = pasaporte + "," + l.aeroSalida + "," + l.aeroLlegada + "," + \
                               l.fechSalida + "," + l.precio + "," + l.duracion + "," + l.tipo + \
                               "," + l.escala1 + "," + l.escala2 + "," + l.horaLlega + "\n"
                        compraVuelos.write(text)
                compraVuelos.close()
                listHitorial.clear()

                print('\nVuelo comprado!\n')
                compra = input('\nCOMPRAR OTRO VUELO\n'
                               '[1]-Comprar otro: \n'
                               '[2]-Volver al menu\n'
                               '>>>')
                if compra == 1:
                    vuelosInteligentesEscalas()
                else:
                    menuUsuario()
    else:
        menuUsuario()


def vuelosInteligentes():
    #
    cont = 0
    print("\nBUSQUEDA DE VUELOS INTELIGENTES\n")
    fecha = input('Ingrese la fecha vuelo, AAAA-MM-DD: ')
    date = datetime.strptime(fecha, "%Y-%m-%d")
    rango = int(input('Ingrese el rango de días para ver el vuelo: '))
    fechSuma = date + timedelta(days=rango)
    fechResta = date - timedelta(days=rango)

    fechaComp1 = datetime.strftime(fechSuma, "%Y-%m-%d")
    fechaComp2 = datetime.strftime(fechResta, "%Y-%m-%d")

    aSalida = input('Ingrese el aeropuerto de salida ')
    aLlegada = input('Ingrese el aeropuerto de llegada: ')

    for x in listVuelos:
        fechaComparar = x.fechaSalida
        if fechaComparar >= fechaComp2 and fechaComparar <= fechaComp1:
            if x.aeropuertoSalida == aSalida and x.aeropuertoLlegada == aLlegada:
                tipo = "Vuelos inteligentes"
                r = ""

                v = Historial(x.horaSalida, x.aeropuertoSalida, x.aeropuertoLlegada, fecha, x.precio,
                              x.duracion, tipo, r, x.fechaLlegada, x.horaLlegada, x.id)
                listHitorial.append(v)
                cont += 1
                if cont == 5:
                    break
    listHitorial.sort(key=lambda Historial: Historial.precio)
    for p in listHitorial:
        print("Vuelo", p.codigo, "Precio: ", p.precio)
    compra = input("[1]-Comprar vuelos\n"
                   "[2]-Volver\n"
                   ">>>")
    if compra == "1":

        while True:
            pasaporte = input('Ingrese su numero de pasaporte: ')
            if usuario == pasaporte:

                dr = int(input('Ingrese el codigo del vuelo: '))

                for i in listHitorial:
                    i.precio = str(i.precio)
                    i.duracion = str(i.duracion)

                compraVuelos = open(pasaporte + ".txt", "a")
                for l in listHitorial:
                    if dr == l.codigo:
                        text = pasaporte + "," + l.aeroSalida + "," + l.aeroLlegada + "," + \
                               l.fechSalida + "," + l.precio + "," + l.duracion + "," + l.tipo + \
                               "," + l.escala1 + "," + l.escala2 + "," + l.horaLlega + "\n"
                        compraVuelos.write(text)
                compraVuelos.close()
                listHitorial.clear()

                print('\nVuelo comprado!\n')
                compra = input('\nCOMPRAR OTRO VUELO\n'
                               '[1]-Comprar otro: \n'
                               '[2]-Volver al menu\n'
                               '>>>')
                if compra == 1:
                    vuelosInteligentes()
                else:
                    menuUsuario()
    else:
        menuUsuario()


def busqVuelos():
    hace = input("[1]-Rápido / Caro\n"
                 "[2]-Lento / Barato\n"
                 "[3}-Volver\n"
                 ">>>")
    if hace == "1":
        vueloDirecto()
    elif hace == "2":
        escalaVuelos()
    else:
        menuUsuario()


def escalaVuelos():  # Funcion de los vuelos con escalas
    print("<<<VUELOS CON ESCALAS>>>")
    aSalida = input('Ingrese el aeropuerto de origen: ')
    aLlegada = input('Ingrese el aeropuerto de destino: ')
    fechSalida = input("Ingrese la fecha de AAAA-MM-DD: ")
    cont = 0
    codigo = 0

    for p in listVuelos:
        if cont == 5:
            break
        if fechSalida == p.fechaSalida:
            if p.aeropuertoSalida == aSalida:

                for l in listVuelos:
                    # if cont == 5:
                    # break
                    if p.aeropuertoLlegada == l.aeropuertoSalida and p.fechaSalida == l.fechaLlegada and p.horaLlegada < l.horaSalida and l.aeropuertoSalida != p.aeropuertoSalida:

                        for q in listVuelos:
                            if l.aeropuertoLlegada == q.aeropuertoSalida and l.horaLlegada < q.horaSalida and l.aeropuertoSalida != p.aeropuertoSalida:
                                if q.aeropuertoLlegada == aLlegada and p.fechaLlegada == q.fechaLlegada:
                                    codigo += 1
                                    totalPrecio = (p.precio + l.precio + q.precio) / 4
                                    duracion = p.duracion + l.duracion + q.duracion + 3
                                    tipo = "Vuelo con escala"
                                    print("\nTipo de vuelo: ", tipo)
                                    print("Duracion total del vuelo: ", duracion, "horas", )
                                    print("Codigo del Vuelo:", codigo)
                                    print(p.id, p.aeropuertoSalida, p.aeropuertoLlegada, p.precio)
                                    print(l.id, l.aeropuertoSalida, l.aeropuertoLlegada, l.precio)
                                    print(q.id, q.aeropuertoSalida, q.aeropuertoLlegada, q.precio)
                                    print("Precio total del vuelo: ", totalPrecio)
                                    v = Historial(p.horaSalida, p.aeropuertoSalida, q.aeropuertoLlegada, p.fechaSalida,
                                                  totalPrecio,
                                                  duracion, tipo, l.aeropuertoSalida, q.aeropuertoSalida, q.horaLlegada,
                                                  codigo)

                                    listHitorial.append(v)
                                    aeSali = ""
                                    v = Historial(p.horaSalida, p.aeropuertoSalida, l.aeropuertoLlegada, l.fechaSalida,
                                                  totalPrecio,
                                                  duracion, tipo, l.aeropuertoSalida, aeSali, l.horaLlegada, codigo)
                                    cont += 1
                                    listHitorial.append(v)

    compra = input("\n[1]-Comprar vuelo\n"  # usuario decide si comprar el Vuelo o no!
                   "[2]-volver\n"
                   ">>>")
    if compra == "1":
        while True:
            pasaporte = input('Ingrese su numero de pasaporte: ')
            if usuario == pasaporte:

                dr = int(input('Ingrese el codigo del vuelo: '))

                for i in listHitorial:
                    i.precio = str(i.precio)
                    i.duracion = str(i.duracion)

                compraVuelos = open(pasaporte + ".txt", "a")
                for l in listHitorial:
                    if dr == l.codigo:
                        text = pasaporte + "," + l.aeroSalida + "," + l.aeroLlegada + "," + \
                               l.fechSalida + "," + l.precio + "," + l.duracion + "," + l.tipo + \
                               "," + l.escala1 + "," + l.escala2 + "," + l.horaLlega + "\n"
                        compraVuelos.write(text)
                compraVuelos.close()
                listHitorial.clear()

                print('\nVuelo comprado!\n')
                compra = input('\nCOMPRAR OTRO VUELO\n'
                               '[1]-Comprar otro: \n'
                               '[2]-Volver al menu\n'
                               '>>>')
                if compra == 1:
                    escalaVuelos()
                else:
                    menuUsuario()
    else:
        menuUsuario()


def vueloDirecto():  # Vuelo directo

    print("<<<VUELOS DIRECTOS>>>")
    aSalida = input('Ingrese el aeropuerto de origen: ')
    aLlegada = input('Ingrese el aeropuerto de destino: ')
    fechSalida = input("Ingrese la fecha del vuelo AAAA-MM-DD: ")

    for p in listVuelos:
        if p.aeropuertoSalida == aSalida and p.aeropuertoLlegada == aLlegada and fechSalida == p.fechaSalida:
            print("\nVuelo: ", p.id, "\nAeropuerto salida: ", p.aeropuertoSalida,
                  "\nAeropuerto Llegada: ", p.aeropuertoLlegada, "\nFecha de vuelo: ", p.fechaSalida,
                  "\nHora vuelo: ", p.horaSalida, "\nDuracion: ", p.duracion, "horas", "\nPrecio: ", p.precio, )
            tipo = "Vuelo directo"
            r = ""
            v = Historial(p.horaSalida, p.aeropuertoSalida, p.aeropuertoLlegada, fechSalida, p.precio,
                          p.duracion, tipo, r, p.fechaLlegada, p.horaLlegada, p.id)
            listHitorial.append(v)
        """else:
            print("No hay vuelos en esa fecha!",menuUsuario())"""

    compra = input("\n[1]-Comprar vuelo\n"  # usuario decide si comprar el Vuelo o no!
                   "[2]-volver\n"
                   ">>>")
    if compra == "1":

        while True:
            pasaporte = input('Ingrese su numero de pasaporte: ')

            if usuario == pasaporte:

                dr = input('Ingrese el codigo del vuelo: ')

                for i in listHitorial:
                    i.precio = str(i.precio)
                    i.duracion = str(i.duracion)

                for l in listHitorial:
                    if dr == l.codigo:
                        compraVuelos = open(pasaporte + ".txt", "a")
                        text = pasaporte + "," + l.aeroSalida + "," + l.aeroLlegada + "," + \
                               l.fechSalida + "," + l.precio + "," + l.duracion + "," + l.tipo + \
                               "," + l.escala2 + "," + l.horaLlega + "," + l.codigo + "\n"
                        compraVuelos.write(text)
                        compraVuelos.close()
                listHitorial.clear()

                print('\nVuelo comprado!\n')
                compra = input('\nCOMPRAR OTRO VUELO\n'
                               '[1]-Comprar otro: \n'
                               '[2]-Volver al menu\n'
                               '>>>')
                if compra == 1:
                    vueloDirecto()
                else:
                    menuUsuario()
    else:
        menuUsuario()


def menuPrincipal():  # administrator menu
    print("""\n*_*_*_*_*_*_MENU PRINCIPAL DE ADMINISTRADORES_*_*_*_*_*_*
    1.-Mantenimiento de pistas.
    2.-Mantenimiento de puertas de abordaje.
    3.-Mantenimiento de aerolineas.
    4.-Mantenimiento de tripulaciones.
    5.-Mantenimiento de aviones.
    6.-Mantenimiento de aeropuertos.
    7.-Mantenimiento de vuelos.
    8.-Salir.""")

    while True:
        mante = (input('Indique a cual mantenimiento desea ingresar: \n'))
        if mante == "1":
            mantePistas()
        elif mante == "2":
            mantePuertas()
        elif mante == "3":
            manteAerolineas()
        elif mante == "4":
            manteTripu()
        elif mante == "5":
            manteAvion()
        elif mante == "6":
            manteAeropuerto()
        elif mante == "7":
            manteVuelos()
        elif mante == "8":
            menu()
        else:
            print("Ingrese un valor valido entre las opciones.")
            menuPrincipal()


def mantePistas():  # runway maintenance menu
    print("""\n_____MANTENIMIENTO DE PISTAS_____\n
    [1]-Crear una pista
    [2]-Leer pista
    [3]-Editar pista
    [4]-Eliminar pista
    [5]-Volver menu principal""")
    while True:
        hacer = input('Ingrese la opcion que desea realizar: ')
        if hacer == "1":
            crearPista()
        elif hacer == "2":
            leerPista()
        elif hacer == "3":
            editarPista()
        elif hacer == "4":
            elimiPista()
        elif hacer == "5":
            menuPrincipal()


"------------------------------------------Mantenimiento de pistas---------------------------------------------"


def crearPista():  # crear pista
    print("\n+++NUEVA PISTA+++\n"
          "Lista de pistas")
    # Here you write the track you want to add
    for r in listPista:
        print("pista: ", r.numPista, "-" "estado: ", r.estado)

    numPista = (input("\nIngrese el numero de pista: "))

    for p in listPista:
        if numPista == p.numPista:
            print("La pista ya existe!", crearPista())
    else:
        for h in listPista:  # compare if the track exists

            while True:
                if numPista != h.numPista:
                    s = (input("Elija el estado de la pista!\n"
                               "*1-Disponible\n"
                               "*2-No disponible\n"
                               "*3-En mantenimiento\n"
                               ":"))

                    if s == "1":  # se cambia los estados de la pista a strings
                        estado = "Disponible"
                        print("\nPista creada!\n"
                              "pista", numPista, "-" " estado: ", estado)
                        l = Pista(numPista, estado)
                        listPista.append(l)

                    elif s == "2":
                        estado = "No disponible"
                        print("\nPista creada!\n"
                              "pista", numPista, "-" " estado: ", estado)
                        l = Pista(numPista, estado)
                        listPista.append(l)

                    elif s == "3":
                        estado = "En mantenimiento"
                        print("\nPista creada!\n"
                              "pista", numPista, "-" " estado: ", estado)
                        l = Pista(numPista, estado)
                        listPista.append(l)

                    elif s != "1" and "1" and "3":
                        print("Invalido, ingrese datos nuevamente.!")
                        crearPista()

                    otra = input("\n[1]- Crear otra pista\n"
                                 "Precione Cualquier tecla para volver al menu\n"
                                 ">>>")
                    if otra == "1":
                        crearPista()
                    else:
                        mantePistas()

                else:

                    print("La pista ya existe!\n"
                          "Vuelva a ingresar dados.\n")
                    crearPista()


def leerPista():  # The status of the track is read in this function
    print("\n*_*_*_*_*_*_[LEER PISTA]*_*_*_*_*_\n")
    for r in listPista:
        print("Pista: ", r.numPista)

    filtro = (input("Ingrese el numero de pista: "))

    # Recorrer la lista
    for a in listPista:  # what the user wants to see appears on the screen
        if filtro == a.numPista:

            print("Pista: ", a.numPista, " Estado: ", a.estado)

            print("\n[1].-Volver a leer\n[PRECIONE CUALQUIER TECLA NUMERICA].-Volver al menu")
            z = int(input('Que desea realizar :'))  # option to see the track or return to the menu

            if z == 1:
                leerPista()
            else:
                mantePistas()
    else:
        print("La pista no existe!, ingrese nuevamente")
        leerPista()


def editarPista():  # Edit the states of the track
    print("\n_-_-_-_-_EDITOR DE PISTAS_-_-_-_-_\n")

    for r in listPista:
        print("pista: ", r.numPista)

    pistEdit = (input("Indique pista a editar: "))

    for k in listPista:  # what the user wants to see appears on the screen
        if pistEdit == k.numPista:
            print("\nPista: ", k.numPista, " Estado: ", k.estado)

            s = int(input("\nElija el nuevo estado de la pista!\n"  # the user chooses the state
                          "*1-Disponible\n"
                          "*2-No disponible\n"
                          "*3-En mantenimiento\n"
                          ": "))
            if s == 1:  # the states of the tracks are updated
                k.estado = "Disponible"
                print("\nPista actualizada!\n"
                      "\npista", k.numPista, "-" " estado: ", k.estado, "\n")  # imprime the new state
            elif s == 2:
                k.estado = "No disponible"
                print("\nPista actualizada!\n"
                      "\npista", k.numPista, "-" " estado: ", k.estado, "\n")
            elif s == 3:
                k.estado = "En mantenimiento"
                print("\nPista actualizada!\n"
                      "\npista", k.numPista, "-" " estado: ", k.estado, "\n")
            mantePistas()
    else:
        print("La pista no existe!, ingrese nuevamente")
        editarPista()


def elimiPista():  # Delete Pistas
    print("\n---ELIMINAR PISTA---\n")
    for r in listPista:
        print("pista: ", r.numPista)

    elimi = (input("Ingrese la pista a elimiar: "))

    for p in listPista:
        # what the user wants to remove is displayed on the screen

        if elimi == p.numPista:
            listPista.remove(p)
            print("Pista eliminada!")
            mantePistas()
    else:
        print("La pista no existe!, ingrese nuevamente")
        elimiPista()


"-------------------------------------------Mantenimiento de puertas--------------------------------------------------"


def mantePuertas():  # Menu door maintenance
    print("""\n_____MANTENIMIENTO DE PUERTAS_____\n
        [1]-Crear una puerta
        [2]-Leer puerta
        [3]-Editar puerta
        [4]-Eliminar puerta
        [5]-Volver menu principal""")
    while True:
        hacer = int(input('Ingrese la opcion que desea realizar: '))
        if hacer == 1:
            crearPuerta()
        elif hacer == 2:
            leerPuerta()
        elif hacer == 3:
            editarPuerta()
        elif hacer == 4:
            elimiPuerta()
        elif hacer == 5:
            menuPrincipal()


def crearPuerta():
    print("\n+++NUEVA PUERTA+++\n"
          "Lista de puertas")  # Here you write the track you want to add

    for w in listPuerta:
        print("Puerta: ", w.numPuerta)

    for k in range(int(input("Cuantas puertas desea crear: "))):

        numPuerta = (input("Ingrese el numero de puerta: "))
        for p in listPuerta:
            if numPuerta == p.numPuerta:
                print("La puerta ya existe!", crearPuerta())
        else:
            t = (input("Elija el estado de la puerta!\n"
                       "*1-Disponible\n"
                       "*2-En uso\n"
                       ":"))

            if t == "1":  # the states of the pureta are changed to strings
                estado = "Disponible"
                print("\nPuerta creada!\n"
                      "Puerta", numPuerta, "-" " Estado: ", estado)
                j = Puerta(numPuerta, estado)
                listPuerta.append(j)

            elif t == "2":
                estado = "En uso"
                print("\nPuerta creada!\n"
                      "Puerta", numPuerta, "-" " Estado: ", estado)
                j = Puerta(numPuerta, estado)
                listPuerta.append(j)

    mantePuertas()


def leerPuerta():
    # In this function the status of the track is read

    print("\n*_*_*_*_*_*_[LEER PUERTAS]*_*_*_*_*_\n")
    for r in listPuerta:
        print("Puerta: ", r.numPuerta)

    filtro = (input("Ingrese el numero de puerta: "))

    # Recorrer la lista
    for a in listPuerta:
        # what the user wants to see appears on the screen

        if filtro == a.numPuerta:

            print("Puerta: ", a.numPuerta, " Estado: ", a.estado)

            print("\n[1].-Volver a leer\n[PRECIONE CUALQUIER TECLA NUMERICA].-Volver al menu")
            z = int(input('Que desea realizar :'))
            # option to see the track or return to the menu

            if z == 1:
                leerPuerta()
            else:
                mantePuertas()
    else:
        print("La puerta no existe!, ingrese nuevamente")
        leerPuerta()


def editarPuerta():
    # edit the states of the door

    print("\n_-_-_-_-_EDITOR DE PUERTAS_-_-_-_-_\n")

    for r in listPuerta:
        print("Puerta: ", r.numPuerta)

    pistEdit = int(input("Indique puerta a editar: "))

    for k in listPuerta:
        # what the user wants to see appears on the screen

        if pistEdit == k.numPuerta:

            print("\nPuerta: ", k.numPuerta, " Estado: ", k.estado)

            s = int(input("\nElija el nuevo estado de la puerta!\n"
                          # the user chooses the state
                          "*1-Disponible\n"
                          "*2-En uso\n"
                          ": "))

            if s == 1:
                # the states of the tracks are updated
                k.estado = "Disponible"
                print("\nPuerta actualizada!\n"
                      "\nPuerta", k.numPuerta, "-" " Estado: ", k.estado, "\n")  # imprime el nuevo estado

            elif s == 2:
                k.estado = "En uso"
                print("\nPuerta actualizada!\n"
                      "\nPuerta", k.numPuerta, "-" " Estado: ", k.estado, "\n")
            mantePuertas()
    else:
        print("La puerta no existe!, ingrese nuevamente")
        editarPuerta()


def elimiPuerta():
    # Remove Doors
    print("\n---ELIMINAR PUERTA---\n")
    for r in listPuerta:
        print("puerta: ", r.numPuerta)

    elimi = (input("Ingrese la puerta a elimiar: "))

    for p in listPuerta:
        # what the user wants to remove is displayed on the screen

        if elimi == p.numPuerta:
            listPuerta.remove(p)
            print("Puerta eliminada!")
            mantePuertas()
    else:
        print("La puerta no existe!, ingrese nuevamente")
        elimiPuerta()


"----------------------------------------------Mante Aerolineas---------------------------------------------------------"


def manteAerolineas():  # Menu Aerolineas maintenance
    print("""\n_____MANTENIMIENTO DE AEROLINEAS_____\n
           [1]-Crear Aerolinea
           [2]-Leer Aerolinea
           [3]-Editar Aerolinea
           [4]-Eliminar Aeroliea
           [5]-Volver menu principal""")

    while True:
        hacer = int(input('Ingrese la opcion que desea realizar: '))
        if hacer == 1:
            crearAerolinea()
        elif hacer == 2:
            leerAerolinea()
        elif hacer == 3:
            editarAerolinea()
        elif hacer == 4:
            elimiAerolinea()
        elif hacer == 5:
            menuPrincipal()


def crearAerolinea():
    print("\n+++NUEVA AEROLINEA+++\n"
          "\nLISTA AEROLINEAS\n")
    # Here you write the airline you want to add

    for w in listAerolinea:
        print("Nombre: ", w.nomAero, "-"" Año fundado: ", w.annoFund, "-"" Cantidad países: ", w.cantPaises,
              "-"" Tipo: ", w.tipoAero)

    nomAero = (input("Ingrese el nombre de la aerolinea: "))
    annoFund = int(input("Ingrese el año de fundación: "))
    cantPaises = int(input("Ingrese la cantidad de países en los que opera: "))

    while True:
        t = int(input("Elija el tipo de aerolinea!\n"
                      "*1-Local\n"
                      "*2-Internacional\n"
                      ":"))

        if t == 1:  # the airline's status is changed to strings
            tipoAero = "Local"
            print("\nAerolinea creada!\n"
                  "Aerolinea: ", nomAero, "-" " Año fundado: ", annoFund, "-"" Cantidad países: ", cantPaises,
                  "-"" Tipo: ", tipoAero)
            j = Aerolinea(nomAero, annoFund, tipoAero, cantPaises)
            listAerolinea.append(j)

        elif t == 2:

            tipoAero = "Internacional"
            print("\nAerolinea creada!\n"
                  "Aerolinea: ", nomAero, "-" " Año fundado: ", annoFund, "-"" Cantidad países: ", cantPaises,
                  "-"" Tipo: ", tipoAero)
            j = Aerolinea(nomAero, annoFund, tipoAero, cantPaises)
            listAerolinea.append(j)

        manteAerolineas()


def leerAerolinea():
    # In this function the data of the Airline is read

    print("\n*_*_*_*_*_*_[LEER AEROLINEAS]*_*_*_*_*_\n")
    for w in listAerolinea:
        print("Nombre: ", w.nomAero, )

    while True:
        try:  # validate that what is entered are only letters
            filtro = (input("Ingrese el nombre de la aerolinea a leer: "))

            # Recorrer la lista
            for a in listAerolinea:
                # what the user wants to see appears on the screen

                if filtro == a.nomAero:

                    print("Aerolinea: ", a.nomAero, "-" " Año fundado: ", a.annoFund, "-"" Cantidad países: ",
                          a.cantPaises, "-"" Tipo: ", a.tipoAero)

                    while True:
                        try:
                            print("\n[1].-Volver a leer\n[PRECIONE CUALQUIER TECLA NUMERICA].-Volver al menu")
                            z = int(input('Que desea realizar :'))  # option to see the track or return to the menu

                            if z == 1:
                                leerAerolinea()
                            else:
                                manteAerolineas()

                        except ValueError:
                            print("Solo numeros!")
            else:
                print("La aerolinea no existe!, ingrese nuevamente")
                leerAerolinea()

        except ValueError:
            print("Solo letras")


def editarAerolinea():
    # edit the airline's status

    print("\n_-_-_-_-_EDITOR DE AEROLINEAS_-_-_-_-_\n")

    for r in listAerolinea:
        print("Aerolinea: ", r.nomAero)
    while True:
        try:
            pistEdit = (input("Ingrese aerolinea a editar: "))

            for k in listAerolinea:  # the airline you want to see is shown on the screen

                if pistEdit == k.nomAero:

                    print("Aerolinea: ", k.nomAero, "-" " Año fundado: ", k.annoFund,
                          "-"" Cantidad países: ", k.cantPaises, "-"" Tipo: ", k.tipoAero)

                    k.cantPaises = int(input("Ingrese la nueva cantidad de países: "))
                    while True:
                        try:
                            t = int(input("Elija el tipo de aerolinea!\n"
                                          "*1-Local\n"
                                          "*2-Internacional\n"
                                          ":"))

                            if t == 1:  # the type of airline is chosen
                                k.tipoAero = "Local"
                                print("\nAerolinea editada!\n"
                                      "Aerolinea: ", k.nomAero, "-" " Año fundado: ", k.annoFund,
                                      "-"" Cantidad países: ", k.cantPaises, "-"" Tipo: ", k.tipoAero)
                                listAerolinea.append(k)

                            elif t == 2:

                                k.tipoAero = "Internacional"
                                print("\nAerolinea editada!\n"
                                      "Aerolinea: ", k.nomAero, "-" " Año fundado: ", k.annoFund,
                                      "-"" Cantidad países: ", k.cantPaises, "-"" Tipo: ", k.tipoAero)
                                listAerolinea.append(k)

                            manteAerolineas()

                        except ValueError:
                            print("Solo numeros")

            else:
                print("La Aeroliea no existe!, ingrese nuevamente")
                editarAerolinea()
        except ValueError:
            print("Solo letras")


def elimiAerolinea():
    # Remove airline
    print("\n---ELIMINAR AEROLINEA---\n")
    for r in listAerolinea:
        print("Aerolinea: ", r.nomAero)

    elimi = (input("Ingrese la aerolinea a elimiar: "))

    for p in listAerolinea:
        # what the user wants to remove is displayed on the screen

        if elimi == p.nomAero:
            listAerolinea.remove(p)
            print("Aerolinea eliminada!")
            manteAerolineas()
    else:
        print("La aerolinea no existe!, ingrese nuevamente")
        elimiAerolinea()


"-----------------------------------------------Mante tripulacion------------------------------------------------------"


def manteTripu():
    # menu crew maintenance
    print("""\n_____MANTENIMIENTO DE AEROLINEAS_____\n
               [1]-Crear Tripulante
               [2]-Leer Tripulante
               [3]-Editar Tripulante
               [4]-Eliminar Tripulante
               [5]-Volver menu principal""")

    while True:
        hacer = int(input('Ingrese la opcion que desea realizar: '))

        if hacer == 1:
            crearTripulante()
        elif hacer == 2:
            leerTripulante()
        elif hacer == 3:
            editarTripulante()
        elif hacer == 4:
            elimiTripulante()
        elif hacer == 5:
            menuPrincipal()


def crearTripulante():
    print("\n+++NUEVO TRIPULANTE+++\n")
    # Here you write the crew member you want to add

    identificacion = input("Ingrese el numero de identificacion: ")
    for x in listTripu:
        if identificacion == x.identificacion:
            print("Error!. esa identificacion ya existe")
            crearTripulante()
    else:
        nombre = (input("Ingrese el nombre y apellido del tripulante: "))
        fecha = (input("Ingrese el año de nacimiento, AAAA-MM-DD: "))
        while True:  # # Here you write the crew member who isThe airline you work for wants to add
            for k in listAerolinea:  # imprime el id de aerolineas
                print("Aerolinea: ", k.nomAero)
            idAerolinea = (input("Ingrese aerolinea para la que trabaja: "))
            for p in listAerolinea:  # The for is to compare, and see if the id that is entered exists

                if idAerolinea == p.nomAero:
                    # I compare the imput with the for list

                    while True:
                        # indicar cual será el puesto
                        puesto = input("\n[1]-Piloto"
                                       "\n[2]-Servicio al cliente"
                                       "\nIndique cual es el puesto: ")
                        if puesto == "1":
                            puestoTrabajo = "Piloto"

                            while True:
                                esta = input("\n[1]-Disponible"
                                             "\n[2]-En servicio"
                                             "\nIndique el estado: ")
                                if esta == "1":
                                    estado = True
                                    j = Tripulacion(nombre, fecha, idAerolinea, puestoTrabajo, estado, identificacion)
                                    listTripu.append(j)
                                    print("Tripulante creado!")

                                elif esta == "2":
                                    estado = False
                                    j = Tripulacion(nombre, fecha, idAerolinea, puestoTrabajo, estado, identificacion)
                                    listTripu.append(j)
                                    print("Tripulante creado!")
                                manteTripu()

                        elif puesto == "2":
                            puestoTrabajo = "Servicio al cliente"

                            while True:
                                esto = input("\n[1]-Disponible"
                                             "\n[2]-En servicio"
                                             "\nIndique el estado: ")
                                if esto == "1":
                                    estado = True
                                    j = Tripulacion(nombre, fecha, idAerolinea, puestoTrabajo, estado, identificacion)
                                    listTripu.append(j)
                                    print("Tripulante creado!")

                                elif esto == "2":
                                    estado = False
                                    j = Tripulacion(nombre, fecha, idAerolinea, puestoTrabajo, estado, identificacion)
                                    listTripu.append(j)
                                    print("Tripulante creado!")
                                manteTripu()

            else:
                print("La aerolinea que ingresó no existe!")


def leerTripulante():
    # read crew

    print("\n******LEER TRIPULACION*******\n")
    for h in listTripu:
        print("Nombre:", h.nombre, "\nId: ", h.identificacion)

    identifi = input("Ingrese la identificación del tripulante: ")
    for u in listTripu:
        if identifi == u.identificacion:
            if u.estado == True:

                print("\nNombre: ", u.nombre, "\n Fecha nacimiento: ", u.fecha, "\n Aerolinea: ", u.idAerolinea,
                      "\n Identificacion: ", u.identificacion, "\n Puesto", u.puestoTrabajo, "\n estado: Disponible")
                manteTripu()
            else:
                print("\nNombre: ", u.nombre, "\n Fecha nacimiento: ", u.fecha, "\n Aerolinea: ", u.idAerolinea,
                      "\n Identificacion: ", u.identificacion, "\n Puesto:", u.puestoTrabajo, "\n Estado: En servicio")
                manteTripu()
    else:
        print("El tripulante no existe!.")
        leerTripulante()


def editarTripulante():
    # edit crew member
    print("\n______EDITOR DE TRIPULACION_____\n")
    tripu = input("ingrese identificación de tripulante: ")
    for x in listTripu:
        if tripu == x.identificacion:
            if x.estado == True:
                print("Nombre: ", x.nombre, " Fecha nacimiento: ", x.fecha, " Aerolinea: ", x.idAerolinea,
                      " Identificacion: ", x.identificacion, " Puesto: Piloto")
            else:
                print("Nombre: ", x.nombre, " Fecha nacimiento: ", x.fecha, " Aerolinea: ", x.idAerolinea,
                      " Identificacion: ", x.identificacion, " Puesto: Servicio al cliente")

            while True:
                # The airline you work for

                for k in listAerolinea:
                    # print the airline id
                    print("Aerolinea: ", k.nomAero)

                x.idAerolinea = (input("Ingrese aerolinea: "))

                for p in listAerolinea:
                    # The for is to compare, and see if the id that is entered exists

                    if x.idAerolinea == p.nomAero:
                        # I compare the imput with the for list

                        while True:
                            # indicate what the position will be
                            x.puesto = (input("\n[1]-Piloto"
                                              "\n[2]-Servicio al cliente"
                                              "\nIndique cual es el puesto: "))
                            if x.puesto == "1":
                                x.puesto = "Piloto"

                                while True:
                                    esta = (input("\n[1]-Disponible"
                                                  "\n[2]-En servicio"
                                                  "\nIndique el estado: "))
                                    if esta == "1":
                                        x.estado = True
                                        listTripu.append(x)
                                        print("Tripulante actualizado!")

                                    elif esta == "2":
                                        x.estado = False
                                        listTripu.append(x)
                                        print("Tripulante actualizado!")
                                    manteTripu()


                            elif x.puesto == "2":
                                x.puesto = "Servicio al cliente"

                                while True:
                                    esto = (input("\n[1]-Disponible"
                                                  "\n[2]-En servicio"
                                                  "\nIndique el estado: "))
                                    if esto == "1":
                                        x.estado = True
                                        listTripu.append(x)
                                        print("Tripulante actualizado!")

                                    elif esto == "2":
                                        x.estado = False
                                        listTripu.append(x)
                                        print("Tripulante actualizado!")
                                    manteTripu()
                else:
                    print("\nLa aerolinea no existe!\n")

    else:
        print("El tripulante no existe!")
        editarTripulante()


def elimiTripulante():
    # Remove Crewmember
    print("\n---ELIMINAR TRIPULANTE---\n")

    elimi = (input("Ingrese identificación de tripulante a elimiar: "))

    for p in listTripu:
        # what the user wants to remove is displayed on the screen

        if elimi == p.identificacion:
            print("\nTripulante: ", p.nombre)

            listTripu.remove(p)
            print("Eliminado!")
            manteTripu()
    else:
        print("El tripulante no existe!, ingrese nuevamente")
        elimiTripulante()


"---------------------------------------------------Mante Avion--------------------------------------------------------"


def manteAvion():
    # maintenance aircraft
    print("""\n_____MANTENIMIENTO DE AVION_____\n
           [1]-Crear Avion
           [2]-Leer Avion
           [3]-Editar Avion
           [4]-Eliminar Avion
           [5]-Volver menu principal""")

    while True:
        hacer = int(input('Ingrese la opcion que desea realizar: '))

        if hacer == 1:
            crearAvion()

        elif hacer == 2:
            leerAvion()

        elif hacer == 3:
            editarAvion()

        elif hacer == 4:
            elimiAvion()

        elif hacer == 5:
            menuPrincipal()


def crearAvion():
    print("\n+++NUEVO AVION+++\n"
          "Lista de aviones")
    # Here you write the track you want to add

    for w in listAvion:  # imprimo la lista de los aviones
        print("Id avion: ", w.idAvion)

    idAvion = (input("Ingrese el id del avion: "))

    for n in listAvion:
        # I loop the list to verify that id does not exist

        if idAvion == n.idAvion:
            print("EL id ya existe")
            crearAvion()

    else:
        contador = 0
        modeloAvion = input("Ingrese el modelo del avion: ")
        while True:
            for t in listAvion:  # verifica si el modelo ya existe

                if modeloAvion == t.modeloAvion:
                    print("El modelo que ingresó ya existe")
                    crearAvion()
            else:
                annoContruc = input("Ingrese el año de construccion (AAAA): ")

                while True:  # La aerolinea pertenece
                    for k in listAerolinea:  # imprime el id de aerolineas

                        print("Aerolinea: ", k.nomAero)

                    aerolineaPertenece = (input("Ingrese aerolinea para la que trabaja: "))

                    for p in listAerolinea:  # Para comprobar si la aerolinea existe

                        if aerolineaPertenece == p.nomAero:  # Comparo el imput con la lista del for
                            capacidadPasajeros = input("Ingrese la capacidad de pasajeros:")

                            while True:
                                s = int(input("Elija el estado del avion!\n"
                                              "*1-Disponible\n"
                                              "*2-En uso\n"
                                              ":"))

                                if s == 1:  # se elige los estados del avion
                                    estado = "Disponible"
                                    print("\nAvion creado!\n")
                                    j = Avion(idAvion, modeloAvion, annoContruc, aerolineaPertenece, capacidadPasajeros,
                                              estado, contador)
                                    listAvion.append(j)
                                    manteAvion()

                                elif s == 2:
                                    estado = "En uso"
                                    print("\nAvion creado!\n")
                                    j = Avion(idAvion, modeloAvion, annoContruc, aerolineaPertenece, capacidadPasajeros,
                                              estado, contador)
                                    listAvion.append(j)
                                    manteAvion()

                    else:
                        print("La aerolinea que ingresó no existe!")


def leerAvion():
    print("\n++++LEER AVION++++\n")
    for o in listAvion:
        print("Avion :", o.idAvion)

    filtro = input("Ingrese el id del avion:")
    for l in listAvion:
        if filtro == l.idAvion:
            print("Id avion: ", l.idAvion, " Modelo: ", l.modeloAvion, " Año: ", l.annoConstruc,
                  " Aerolinea: ", l.aerolineaPertenece, " Capacidad: ", l.capacidadPasajeros, " Estado :", l.estado)
            manteAvion()
    else:
        print("El id no existe!")
        leerAvion()


def editarAvion():  # edid plane

    print("\n_-_-_-EDITAR AVION_-_-_-_\n")
    for o in listAvion:
        print("ID AVION: ", o.idAvion)

    avion = input("Ingrese id de avion a editar: ")
    for p in listAvion:
        if avion == p.idAvion:
            p.modeloAvion = input("Ingrese el nuevo modelo del avion: ")
            p.capacidadPasajeros = input("Ingrese nueva capacidad avion: ")

            while True:
                s = (input("Elija el estado del avion!\n"
                           "*1-Disponible\n"
                           "*2-En uso\n"
                           ":"))

                if s == "1":  # se elige los estados del avion
                    p.estado = "Disponible"
                    print("\nAvion actualizado!\n")
                    manteAvion()

                elif s == "2":
                    p.estado = "En uso"
                    print("\nAvion actualizado!\n")
                    manteAvion()
    else:
        print("El id no existe")
        editarAvion()


def elimiAvion():  # Eliminar Pistas
    print("\n---ELIMINAR AVION---\n")

    for r in listAvion:
        print("ID Avion: ", r.idAvion)

    elimi = (input("Ingrese id del avion a elimiar: "))

    for p in listAvion:  # se muestra en pantalla lo que el usuario desea eliminar

        if elimi == p.idAvion:
            print("\nAvion: ", p.idAvion)

            listAvion.remove(p)
            print("Eliminado!")
            manteAvion()
    else:
        print("El avion no existe!, ingrese nuevamente")
        elimiAvion()


def manteAeropuerto():
    print("""\n_____MANTENIMIENTO DE AEROPUERTO_____\n
               [1]-Crear Aeropuerto
               [2]-Leer Aeropuerto
               [3]-Editar Aeropuerto
               [4]-Eliminar Aeropuerto
               [5]-Volver menu principal""")

    while True:
        hacer = int(input('Ingrese la opcion que desea realizar: '))

        if hacer == 1:
            crearAeropuerto()

        elif hacer == 2:
            leerAeropuerto()

        elif hacer == 3:
            editarAeropuerto()

        elif hacer == 4:
            elimiAeropuerto()

        elif hacer == 5:
            menuPrincipal()


def crearAeropuerto():  # Crear Aeropuerto

    print("\n<<<<<<<<Crear Aeropuerto>>>>>>>>\n")

    for p in listAeropuerto:
        print("ID Aeropuerto ", p.idAero)

    idAero = input("Ingrese ID del aerolinea: ")
    for i in listAeropuerto:
        if idAero == i.idAero:
            print("El id ya existe!")
            crearAeropuerto()

    else:

        nombreAero = input("Ingrese nombre del Aeropuerto: ")
        ciudad = input("Ingrese la ciudad: ")
        pais = input(("Ingrese el país: "))
        print("Aeropuerto creado!")
        k = Aeropuerto(idAero, nombreAero, ciudad, pais)
        listAeropuerto.append(k)
        manteAeropuerto()


def leerAeropuerto():
    print("\n***LEER AEROPUERTO***\n")
    for p in listAeropuerto:
        print("ID Aeropuerto: ", p.idAero)

    filtro = input("Ingrese id de aeropuerto a buscar: ")

    for k in listAeropuerto:
        if filtro == k.idAero:
            print("ID: ", k.idAero, "Nombre ", k.nombreAero, "Ciudad: ", k.ciudad, "País: ", k.pais)
            manteAeropuerto()

    print("El aeropuerto no existe!")
    leerAeropuerto()


def editarAeropuerto():
    print("\n<<<<<<EDITAR AEROPUERTO>>>>>>>\n")
    for p in listAeropuerto:
        print("ID Aeropuerto:", p.idAero)

    filtro = input("Ingrese id a editar: ")
    for h in listAeropuerto:
        if filtro == h.idAero:
            h.nombreAero = input("Ingrese nombre aeropuerto: ")
            h.ciudad = input("Ingrese ciudad: ")
            h.pais = input("Ingrese pais: ")
            print("\nAeropuerto actualizado!\n")
            manteAeropuerto()
    else:
        print("\nEl id no existe!\n")
        editarAeropuerto()


def elimiAeropuerto():  # Eliminar Pistas
    print("\n---ELIMINAR AEROPUERTO---\n")

    for r in listAeropuerto:
        print("ID Aeropuerto ", r.idAero)

    elimi = (input("Ingrese id del aeropuerto a elimiar: "))

    for p in listAeropuerto:  # se muestra en pantalla lo que el usuario desea eliminar
        if elimi == p.idAero:
            print("\nAeropuerto ", p.idAero)
            listAeropuerto.remove(p)
            print("Eliminado!")
            manteAeropuerto()
    else:
        print("El aeropuerto no existe!, ingrese nuevamente")
        elimiAeropuerto()


def manteVuelos():
    print("""\n_____MANTENIMIENTO DE VUELOS_____\n
                 [1]-Crear Vuelo
                 [2]-Leer Vuelo
                 [3]-Editar Vuelo
                 [4]-Eliminar Vuelo
                 [5]-Reportes
                 [6]-Volver menu principal""")
    while True:
        hacer = input('Ingrese la opcion a realizar del mantenimiento: ')

        if hacer == "1":
            AgregarVuelo()
        elif hacer == "2":
            mostrarVuelo()
        elif hacer == "3":
            editarVuelo()
        elif hacer == "4":
            eliminarVuelo()
        elif hacer == "5":
            menuReportes()
        elif hacer == "6":
            menuPrincipal()


def AgregarVuelo():  # aqui se crea un vuelos # new flighs
    print("\n>>>>>AGREGAR VUELOS<<<<<\n")
    print("Aerolineas existentes:")
    for x in listAerolinea:
        print("Nombre: ", x.nomAero)

    aerolinea = input("Ingrese una de las Aerolineas: ")

    for k in listAerolinea:
        if aerolinea == k.nomAero:
            id = (input("Ingrese un id para el vuelo: "))
            for n in listVuelos:
                if id == n.id:
                    print("El id ya está en uso!. Ingrese datos nueveamente!")
                    AgregarVuelo()
            else:
                print("Ingrese la fecha de salida")
                fechaSalida = input('Fecha Salida: AAAA-MM-DD: ')
                horaSalida = input('Hora salida: HH:MM:')
                fechaLlegada = input('\nFecha llegada: AAAA-MM-DD: ')

                for x in listVuelos:
                    if aerolinea == x.aerolinea:
                        if fechaSalida == x.fechaSalida and horaSalida == x.horaSalida:
                            print("La tripulacion para esa hora está en uso!, no se puede crear el vuelo.")
                            manteVuelos()
                else:

                    horaLlegada = input('Hora llegada: HH:MM:')
                    duracion = int(input('Ingrese la duración del vuelo: '))
                    precio = int(input('Ingrese el precio del vuelo: '))

                    for y in listAeropuerto:
                        print("Aeropuerto: ", y.nombreAero)

                    while True:
                        aeropuertoSalida = input("Ingrese el aeropuerto de salida :")

                        for r in listAeropuerto:
                            if aeropuertoSalida == r.nombreAero:
                                for a in listAeropuerto:
                                    print("Aeropuerto: ", a.nombreAero)

                                while True:
                                    aeropuertoLlegada = input("Ingrese el aeropuerto de llegada : ")

                                    for t in listAeropuerto:
                                        if aeropuertoLlegada == t.nombreAero:  # Contadores para random
                                            cont = 0
                                            cont1 = 0
                                            contP = 0
                                            contP1 = 0
                                            contS = 0
                                            contS1 = 0
                                            contS2 = 0
                                            contPista = 0
                                            contPuerta = 0
                                            contAvion = 0
                                            pista = None
                                            puerta = None
                                            avion = None
                                            t1 = None
                                            t2 = None
                                            t3 = None
                                            t4 = None
                                            t5 = None
                                            escal = None
                                            escala1 = None
                                            escala2 = None
                                            while contPista < 1:
                                                pista = random.choice(listPista)

                                                if pista.estado == 'Disponible':
                                                    pista.estado = 'En uso'
                                                    contPista = contPista + 1

                                            while contPuerta < 1:
                                                puerta = random.choice(listPuerta)

                                                if puerta.estado == 'Disponible':
                                                    puerta.estado = 'En uso'
                                                    contPuerta = contPuerta + 1

                                            while contAvion < 1:
                                                avion = random.choice(listAvion)

                                                if avion.aerolineaPertenece == aerolinea:
                                                    avion.estado = 'En uso'
                                                    avion.contador += 1
                                                    contAvion = contAvion + 1

                                            while contP1 < 1:
                                                t1 = random.choice(listTripu)

                                                if t1.puestoTrabajo == 'Piloto' and t1.idAerolinea == aerolinea:
                                                    t1.estado = False
                                                    contP1 += 1

                                            while contP < 1:
                                                t2 = random.choice(listTripu)

                                                if t2.puestoTrabajo == 'Piloto' and t2.idAerolinea == aerolinea and t2.nombre != t1.nombre:  # This funtion is for not repeat tripulant
                                                    t2.estado = False
                                                    contP += 1

                                            while contS < 1:
                                                t3 = random.choice(listTripu)

                                                if t3.puestoTrabajo == 'Servicio al cliente' and t3.idAerolinea == aerolinea:
                                                    t3.estado = False
                                                    contS += 1

                                            while contS1 < 1:
                                                t4 = random.choice(listTripu)

                                                if t4.puestoTrabajo == 'Servicio al cliente' and t4.idAerolinea == aerolinea and t4.nombre != t3.nombre:
                                                    t4.estado = False
                                                    contS1 += 1

                                            while contS2 < 1:
                                                t5 = random.choice(listTripu)

                                                if t5.puestoTrabajo == 'Servicio al cliente' and t5.idAerolinea == aerolinea and t5.nombre != t4.nombre:
                                                    t5.estado = False
                                                    contS2 += 1

                                            v = Vuelos(aerolinea, fechaSalida, fechaLlegada, horaSalida, horaLlegada,
                                                       aeropuertoSalida, aeropuertoLlegada, id, pista, puerta, avion,
                                                       t1, t2, t3, t4, t5, precio, duracion)
                                            listVuelos.append(v)

                                            print("Vuelo creado!")

                                            archivoVuelos = open("losVuelos", "wb")
                                            pickle.dump(listVuelos, archivoVuelos)
                                            archivoVuelos.close()

                                            manteVuelos()
                                    else:
                                        print("El aeropuerto no existe")
                        else:
                            print("El aeropuerto no existe!")
    else:
        print("El Aerolinea no existe!")
        AgregarVuelo()


def mostrarVuelo():  # see flighs

    print("\n***LEER VUELOS***\n")
    for p in listVuelos:
        print(p.id)

    id = input("Ingrese el id del vuelo a ver: ")
    while True:
        for x in listVuelos:
            if id == x.id:
                print("numero vuelo: ", x.id, "\n", "aerolinea: ", x.aerolinea, "\n", "aeropuerdo salida: ",
                      x.aeropuertoSalida, "\n", "aeropuerto llegada: ", x.aeropuertoLlegada, "\n",
                      "hora salida: ", x.horaSalida, "\n", "fecha salida: ", x.fechaSalida, "\n", "pista: ",
                      x.pista.getnumepist(), "\n", "puerta: ", x.puerta.getnumepuer(),
                      "\nAvion: ", x.avion.getAvi(), "\n", "pilotos: ", x.t1.getNombre(), "-", x.t2.getNombre(), "\n",
                      "servicio al cliente: ", x.t3.getNombre(), "-", x.t4.getNombre(), "-", x.t5.getNombre())
                manteVuelos()

        else:
            print("El vuelo ingresado no existe")
            mostrarVuelo()


def eliminarVuelo():  # Delete flighs
    print("\n---ELIMINAR VUELO---\n")

    for x in listVuelos:
        print("Vuelo: ", x.id)

    elimi = (input("Ingrese id del vuelo a eliminar: "))

    for p in listVuelos:  # se muestra en pantalla lo que el usuario desea eliminar
        if elimi == p.id:
            print("\nVuelo ", p.id)
            listVuelos.remove(p)
            print("Eliminado!")
            archivoVuelos = open("losVuelos", "wb")
            pickle.dump(listVuelos, archivoVuelos)
            archivoVuelos.close()
            manteVuelos()
    else:
        print("El vuelo no existe!, ingrese nuevamente")
        eliminarVuelo()


def editarVuelo():
    print("<<<<<<EDITOR DE VUELOS>>>>>>")  # Edid flighs
    print("\nLISTA VUELOS:")
    for x in listVuelos:
        print("Vuelo: ", x.id)

    edid = input("Ingrese ID de Vuelo a editar: ")
    for c in listVuelos:

        if edid == c.id:
            for p in listAerolinea:
                print(p.nomAero)
            id = edid
            aerolinea = input("Ingrese una de las Aerolineas: ")

            for k in listAerolinea:
                if aerolinea == k.nomAero:
                    print("Ingrese la fecha de salida")
                    fechaSalida = input('Fecha Salida: AAAA-MM-DD: ')
                    print("\nIngrese la fecha de llegada")
                    fechaLlegada = input('Fecha Llegada: AAAA-MM-DD: ')
                    horaSalida = input('Hora salida, HH:MM:')

                    for x in listVuelos:
                        if aerolinea == x.aerolinea:
                            if fechaSalida == x.fechaSalida and horaSalida == x.horaSalida:
                                print("La tripulacion para esa hora está en uso!, no se puede crear el vuelo.")
                                manteVuelos()

                    else:
                        horaLlegada = input('Hora llegada, HH:MM: ')
                        duracion = int(input("Ingrese la duracion del vuelo: "))
                        precio = int(input('Ingrese el precio del vuelo: '))

                        for y in listAeropuerto:
                            print("Aeropuerto: ", y.nombreAero)

                        while True:
                            aeropuertoSalida = input("Ingrese el aeropuerto de salida :")
                            for r in listAeropuerto:
                                if aeropuertoSalida == r.nombreAero:
                                    for a in listAeropuerto:
                                        print("Aeropuerto: ", a.nombreAero)

                                    while True:
                                        aeropuertoLlegada = input("Ingrese el aeropuerto de llegada : ")

                                        for t in listAeropuerto:
                                            if aeropuertoLlegada == t.nombreAero:
                                                cont = 0  # Contadores para random
                                                cont1 = 0
                                                contP = 0
                                                contP1 = 0
                                                contS = 0
                                                contS1 = 0
                                                contS2 = 0
                                                contPista = 0
                                                contPuerta = 0
                                                contAvion = 0
                                                pista = None
                                                puerta = None
                                                avion = None
                                                t1 = None
                                                t2 = None
                                                t3 = None
                                                t4 = None
                                                t5 = None
                                                escal = None
                                                escala1 = None
                                                escala2 = None
                                                while contPista < 1:
                                                    pista = random.choice(listPista)  # random for pista

                                                    if pista.estado == 'Disponible':
                                                        pista.estado = 'En uso'
                                                        contPista = contPista + 1

                                                while contPuerta < 1:
                                                    puerta = random.choice(listPuerta)  # random for puerta

                                                    if puerta.estado == 'Disponible':
                                                        puerta.estado = 'En uso'
                                                        contPuerta = contPuerta + 1

                                                while contAvion < 1:
                                                    avion = random.choice(listAvion)  # random for avion

                                                    if avion.aerolineaPertenece == aerolinea:
                                                        avion.estado = 'En uso'
                                                        avion.contador += 1
                                                        contAvion = contAvion + 1

                                                while contP1 < 1:  # here is the random for tripulands
                                                    t1 = random.choice(listTripu)

                                                    if t1.puestoTrabajo == 'Piloto' and t1.estado == True:
                                                        t1.estado = False
                                                        contP1 += 1

                                                while contP < 1:
                                                    t2 = random.choice(listTripu)

                                                    if t2.puestoTrabajo == 'Piloto' and t2.estado == True:
                                                        t2.estado = False
                                                        contP += 1

                                                while contS < 1:
                                                    t3 = random.choice(listTripu)

                                                    if t3.puestoTrabajo == 'Servicio al cliente' and t3.estado == True:
                                                        t3.estado = False
                                                        contS += 1

                                                while contS1 < 1:
                                                    t4 = random.choice(listTripu)

                                                    if t4.puestoTrabajo == 'Servicio al cliente' and t4.estado == True:
                                                        t4.estado = False
                                                        contS1 += 1

                                                while contS2 < 1:
                                                    t5 = random.choice(listTripu)

                                                    if t5.puestoTrabajo == 'Servicio al cliente' and t5.estado == True:
                                                        t5.estado = False
                                                        contS2 += 1

                                                v = Vuelos(aerolinea, fechaSalida, fechaLlegada, horaSalida,
                                                           aeropuertoSalida, horaLlegada, aeropuertoLlegada, id, pista,
                                                           puerta, avion, t1, t2, t3, t4, t5, precio, duracion)
                                                listVuelos.remove(c)
                                                listVuelos.append(v)

                                                archivoVuelos = open("losVuelos", "wb")
                                                pickle.dump(listVuelos, archivoVuelos)
                                                archivoVuelos.close()

                                                print("Vuelo editado!")
                                                manteVuelos()
                                        else:
                                            print("El aeropuerto no existe")
                            else:
                                print("El aeropuerto no existe!")
            else:
                print("La Aerolinea no existe!")
                editarVuelo()
    else:
        print("El vuelo no existe!!")
        editarVuelo()

def menuReportes():
    global ventana
    ventana = tk.Tk()

    ventana.geometry("580x500+0+0")
    ventana.title("MENU REPORTES")
    e1 = tk.Label(ventana,text="AEROTEC REPORTES",fg="black")
    e1.pack(padx=5,pady=15,ipadx=5,ipady=15)
    image = tk.PhotoImage(file="avion2.gif")
    image = image.subsample(1,1)
    label = tk.Label(image= image)
    label.place(x=0, y=0, relwidth=1.0, relheight=1.0)
    e3 = tk.Label(ventana, text="MENU REPORTES", fg="black")
    e3.pack(padx=5, pady=5, ipadx=5, ipady=5)
    #label.pack()
    boton = tk.Button(ventana, text="Vuelos por fechas", fg="black", command=rangoFechas)
    boton.pack(padx=5, pady=5, ipadx=5, ipady=5)
    boton3 = tk.Button(ventana, text="Vuelos por aerolineaa", fg="black", command=aerolineasVuelo)
    boton3.pack(padx=5, pady=5, ipadx=5, ipady=5)
    boton4 = tk.Button(ventana, text="Aviones con mas vuelos", fg="black",  command=rankingVuelo)
    boton4.pack(padx=5, pady=5, ipadx=5, ipady=5)
    boton5 = tk.Button(ventana, text="Info de tripulantes", fg="black", command=infoTripu)
    boton5.pack(padx=5, pady=5, ipadx=5, ipady=5)

    ventana.mainloop()






def rangoFechas(): #ventana de buscador por fechas
    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry('580x500+0+0')
    win.config(bg="blue")
    e3=tk.Label(win,text="BUSCAR VUELOS POR FECHAS",fg="black")
    e3.pack(padx=5, pady=5, ipadx=5, ipady=5)
    e2 = tk.Label(win, text="Fecha inicio\n AAAA-MM-DD ", fg="black")
    e2.pack(padx=5, pady=5, ipadx=5, ipady=5)
    fecha = tk.StringVar(ventana) #De la entrada de texto 1
    fecha1 = tk.StringVar(ventana) #De la entrada de texto 2

    entrada1=tk.Entry(win, textvariable=fecha1)
    entrada1.pack(padx=2,pady=2,ipadx=5,ipady=5)

    e4 = tk.Label(win, text="Fecha Final\n AAAA-MM-DD ", fg="black")
    e4.pack(padx=5, pady=5, ipadx=5, ipady=5)

    entrada2 = tk.Entry(win, textvariable=fecha)
    entrada2.pack(padx=5, pady=5, ipadx=5, ipady=5)

    boton2 = tk.Button(win, text='Buscar',
    command=lambda: validarFechas(entrada1, entrada2))  # boton de buscador de vuelos por aerolinea
    boton2.pack(side=tk.TOP)

    boton2 = tk.Button(win, text='volver', command=cerrarVentana)
    boton2.pack(padx=5, pady=20, ipadx=5, ipady=20)

def aerolineasVuelo():
    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry('580x500+0+0')
    win.config(bg="blue")
    e3 = tk.Label(win, text="Buscador de vuelos por aerolinea", fg="black")
    e3.pack(padx=5, pady=5, ipadx=5, ipady=5)
    e2 = tk.Label(win, text="Ingrese la aerolinea ", fg="black")
    e2.pack(padx=5, pady=5, ipadx=5, ipady=5)
    aero = tk.StringVar(ventana)
    entrada1 = tk.Entry(win, textvariable=aero)
    entrada1.pack(padx=2, pady=2, ipadx=5, ipady=5)

    boton2 = tk.Button(win, text='Buscar',
    command=lambda: validarAer(entrada1))  # boton de buscador de vuelos por aerolinea
    boton2.pack(side=tk.TOP)

    boton2 = tk.Button(win, text='volver', command=cerrarVentana)
    boton2.pack(padx=5, pady=20, ipadx=5, ipady=20)


def rankingVuelo():#Aviones con más vuelos

    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry('580x500+0+0')
    win.config(bg="blue")
    e3 = tk.Label(win, text="AVIONES CON MAS VUELOS", fg="black")
    e3.pack(padx=5, pady=25, ipadx=5, ipady=25)

    listbox = tk.Listbox(win, width=30, height=10, borderwidth=15)

    for lista in listAvion:

        if (lista.contador > 1):
            listbox.insert(tk.END, 'AVION: ' + lista.idAvion, "TOTAL VUELOS :" + str(lista.contador), "")
            listbox.pack()

    boton2 = tk.Button(win, text='volver', command=cerrarVentana)
    boton2.pack(padx=5, pady=20, ipadx=5, ipady=20)
    win.mainloop()

def infoTripu(): #Ver tripulantes por aerolinea

    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry('580x500+0+0')
    win.config(bg="blue")
    e3 = tk.Label(win, text="TRIPULANTES POR AEROLINEA", fg="black")
    e3.pack(padx=5, pady=5, ipadx=5, ipady=5)
    e2 = tk.Label(win, text="Ingrese la aerolinea ", fg="black")
    e2.pack(padx=5, pady=5, ipadx=5, ipady=5)
    aero = tk.StringVar(ventana)
    entrada1 = tk.Entry(win, textvariable=aero)
    entrada1.pack(padx=2, pady=2, ipadx=5, ipady=5 )

    boton2 = tk.Button(win, text='Buscar', command=lambda: validarAerolinea(entrada1))  # boton de buscador de vuelos por aerolinea
    boton2.pack(side=tk.TOP)

    boton2 = tk.Button(win, text='volver', command=cerrarVentana)
    boton2.pack(padx=5, pady=20, ipadx=5, ipady=20)

def cerrarVentana():
    ventana.destroy()
    menuReportes()


def validarFechas(fecha1,fecha2): #Validador de vuelos por fechas
    fech1 = fecha1.get()
    fech2 = fecha2.get()

    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry('580x500+0+0')
    win.config(bg="green")
    e3 = tk.Label(win, text="VUELOS POR AEROLINEA", fg="black")
    e3.pack(padx=5, pady=35, ipadx=5, ipady=35)

    listbox = tk.Listbox(win, width=50, height=20, borderwidth=15)

    for x in listVuelos:
        fechaComparar = x.fechaSalida
        if (fechaComparar >= fech1 and fechaComparar <= fech2):
            listbox.insert(tk.END, 'VUELO: ' + x.id, 'FECHA DE VUELO: ' + x.fechaSalida,
            "AERO SALIDA: " + x.aeropuertoSalida,"AERO LLEGADA: " + x.aeropuertoLlegada,"")
            listbox.pack(padx=100, pady=50)

    boton2 = tk.Button(win, text='volver', command=cerrarVentana)
    boton2.pack(padx=5, pady=20, ipadx=5, ipady=20)
    win.mainloop()

def validarAer(aerolineaid): # Validador de busqueda de vuelos por aerolinea
    aerolinea = aerolineaid.get()

    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry('580x500+0+0')
    win.config(bg="green")
    e3 = tk.Label(win, text="VUELOS POR AEORLINEA", fg="black")
    e3.pack(padx=5, pady=25, ipadx=5, ipady=25)

    listbox = tk.Listbox(win, width=50, height=20, borderwidth=15)

    for lista in listVuelos:

        if (aerolinea == lista.aerolinea):
            listbox.insert(tk.END, 'VUELO: ' + lista.id, "FECHA DE VUELO :" + lista.fechaSalida,
            "AERO SALIDA: " + lista.aeropuertoSalida,"AERO LLEGADA: " + lista.aeropuertoLlegada,"")
            listbox.pack(padx=100, pady=100)

    boton2 = tk.Button(win, text='volver', command=cerrarVentana)
    boton2.pack(padx=5, pady=20, ipadx=5, ipady=20)
    win.mainloop()


def validarAerolinea(aerolineaid):

    aerolinea = aerolineaid.get()

    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry('580x500+0+0')
    win.config(bg="green")
    e3 = tk.Label(win, text="TRIPULANTES POR AEROLINEA", fg="black")
    e3.pack(padx=5, pady=25, ipadx=5, ipady=25)

    listbox = tk.Listbox(win, width=50, height=20, borderwidth=15)

    for lista in listTripu :
         if(aerolinea==lista.idAerolinea):

           listbox.insert(tk.END, 'NOMBRE: ' +  lista.nombre,"PUESTO :" + lista.puestoTrabajo,"FECHA DE NACIMIENTO: " + lista.fecha,"")
           listbox.pack(padx=100, pady=100)


    boton2 = tk.Button(win, text='volver', command=cerrarVentana)
    boton2.pack(padx=5, pady=20, ipadx=5, ipady=20)
    win.mainloop()

menu()
