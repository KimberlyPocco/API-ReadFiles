#importamos libreria Requests
import requests
#Creacion de una paleta de colores
amarillo='\033[33m'
rojo = '\033[31m'
verde = '\033[32m'
morado = '\033[35m'
celeste = '\033[36m'
blanco = '\033[37m'
reset = '\033[39m'

#LISTAR POR GENERACION
def listarPokemonGeneration(generation):
    try: 
        resultado= requests.get(f'https://pokeapi.co/api/v2/generation/{generation}')
        detalleSolicitud : dict= resultado.json()
        resultado ={'nombre' :  [ nombres ['name'] for nombres in detalleSolicitud['pokemon_species']],
                    'habilidad': [ detalleSolicitud['abilities']],
                    'url' : [url ['url'] for url in detalleSolicitud['pokemon_species']]}
        return resultado
    except :
        print(rojo+"NO EXISTE LA GENERACIÓN INGRESADA"+reset)

#LISTAR POR FORMA
def listarPokemonForma(shape):
    try:
        resultado=requests.get(f'https://pokeapi.co/api/v2/pokemon-shape/{shape}')
        detalleSolicitud: dict =resultado.json()
        resultado={'nombre' : [nombres ['name'] for nombres in detalleSolicitud['pokemon_species']],
                 'habilidad' : [],
                 'url': [nombres ['url'] for nombres in detalleSolicitud['pokemon_species']]}
        return resultado
    except :
            print(rojo+"NO EXITEN POKEMONES CON LA FORMA INGRESADA"+reset)

#SUBMENU DE LISTAR POR FORMA
def subMenuForma():
    resultado=requests.get(f'https://pokeapi.co/api/v2/pokemon-shape/')
    detalleSolicitud : dict =resultado.json()
    resultado= [forma ['name'] for forma in detalleSolicitud['results'] ]
    return resultado
#LISTAR POR HABILIDAD
def listarPokemonHabilidad(ability):
    try:
        resultado = requests.get(f'https://pokeapi.co/api/v2/ability/{ability}')
        detalleSolicitud: dict =resultado.json()
        resultado= {'nombre': [nombre ['pokemon']['name'] for nombre in detalleSolicitud['pokemon']],
                    'habilidad': [detalleSolicitud['name']],
                    'url': [url ['pokemon']['url'] for url in detalleSolicitud['pokemon']]}
        return resultado
    except :
        print(rojo+"NO EXISTE EL NOMBRE DE LA HABILIDAD INGRESADA"+reset)

#SUBMENU LISTA HABILIDAD
def subMenuHabilidad():
    try:
        resultado=requests.get(f'https://pokeapi.co/api/v2/ability/')
        detalleSolicitud =resultado.json()
        resultado= [forma ['name'] for forma in detalleSolicitud['results'] ]
        return resultado
    except:
        print(rojo+"NO EXISTE LA HABILIDAD INGRESADA"+reset)
#LISTAR POR HABITAT
def listarPokemonHabitat(habitat):
    try:
        resultado = requests.get(f'https://pokeapi.co/api/v2/pokemon-habitat/{habitat}')
        detalleSolicitud: dict =resultado.json()
        resultado= {'nombre': [ habitad ['name'] for habitad in detalleSolicitud['pokemon_species']],
                    'habilidad': [],
                    'url': [url ['url'] for url in detalleSolicitud['pokemon_species']]}
        return resultado
    except:
        print(rojo+"NO EXISTE LA HABITAD INGRESADA"+reset)

#SUBMENU DE HABITAD
def subMenuHabitad():
    resultado=requests.get(f'https://pokeapi.co/api/v2/pokemon-habitat/')
    detalleSolicitud : dict =resultado.json()
    resultado= [habitad ['name'] for habitad in detalleSolicitud['results'] ]
    return resultado

#LISTAR POR TIPO
def listarPokemonPorTipo(tipo):
    try:
        resultado= requests.get(f'https://pokeapi.co/api/v2/type/{tipo}')
        detalleSolicitud: dict =resultado.json()
        resultado={'nombre' : [tipo ['pokemon']['name'] for tipo in detalleSolicitud['pokemon']],
                    'habilidad': [],
                    'url': [url ['pokemon']['url'] for url in detalleSolicitud['pokemon']]}
        return resultado
    except:
        print(rojo+"NO EXISTE EL TIPO INGRESADO"+reset)

#SUBMENU TIPO
def subMenuTipo():
    resultado=requests.get(f'https://pokeapi.co/api/v2/type/')
    detalleSolicitud : dict =resultado.json()
    resultado= [tipo ['name'] for tipo in detalleSolicitud['results'] ]
    return resultado

def menu():
    while True :
        print(blanco+"*****************************************************************************************")
        print(morado+"                            BIENVENIDO AL MENÚ  POKEMÓN                                  ")
        print(blanco+"*****************************************************************************************")
        print(amarillo+"Opción 1: Listar pokemones por generación")  
        print("Opción 2: Listar pokemones por forma")  
        print("Opción 3: Listar pokemones por habilidad")  
        print("Opción 4: Listar pokemones por habitad") 
        print("Opción 5: Listar pokemones por tipo")
        print("Opción 6: Salir")  
        print(blanco+"*****************************************************************************************"+reset) 
        op =int (input(rojo+"INGRESE EL NUMERO DE LA OPCIÓN A ELEGIR:  "+reset))
       
        #OPCION 1
        if op==1:
            gen=input(verde+"Ingrese la generacion del pokemon deseado: "+reset)
            if listarPokemonGeneration(gen)!=None:
                print(listarPokemonGeneration(gen))
            else:
                print("Solo existen 8 generaciones de pokemonnes!")

        #OPCION 2
        elif op==2:
            print(blanco+"-------------------------------------------------------------------------------------------"+reset) 
            print("SUB MENU FORMAS DE POKEMÓNES: Ingrese el nombre o nro. de una formas mostradas")
            print(blanco+"-------------------------------------------------------------------------------------------"+celeste) 
            menuForma= subMenuForma()
            cont=0
            for i in  menuForma:
                print("{:>2})".format(cont+1),i)
                cont+=1
            print(blanco+"-------------------------------------------------------------------------------------------"+reset) 
            forma=input(verde+"Ingrese su opción para listar pokemones por forma: "+reset)
            
            if listarPokemonForma(forma)!=None:
               print(listarPokemonForma(forma))
            
        #OPCION 3
        elif op==3:
            print(blanco+"-------------------------------------------------------------------------------------------"+reset) 
            print("SUB MENU HABILIDADES DE POKEMÓNES: Ingrese el nombre o nro. de las habilidades mostradas")
            print(blanco+"-------------------------------------------------------------------------------------------"+celeste) 
            menuHabilidad= subMenuHabilidad()
            cont=0
            for i in  menuHabilidad:
                print("{:>2})".format(cont+1),i)
                cont+=1
            print(blanco+"-------------------------------------------------------------------------------------------"+reset)
            habilidad=input(verde+"Ingrese el nombre de la habilidad: "+reset)

            if listarPokemonHabilidad(habilidad)!=None: 
               print(listarPokemonHabilidad(habilidad))

        #OPCION 4
        elif op==4:
            print(blanco+"-------------------------------------------------------------------------------------------"+reset) 
            print("SUB MENU HABITAD DE POKEMÓNES: Ingrese el nombre o nro. de las habitats mostradas")
            print(blanco+"-------------------------------------------------------------------------------------------"+celeste) 
            menuHabitad= subMenuHabitad()
            cont=0
            for i in  menuHabitad:
                print("{:>2})".format(cont+1),i)
                cont+=1
            print(blanco+"-------------------------------------------------------------------------------------------"+reset)
            habitad=input(verde+"Ingrese su opción para listar pokemones por habitad: "+reset)

            if listarPokemonHabitat(habitad)!=None: 
                print(listarPokemonHabitat(habitad))
            

        #OPCION 5
        elif op==5:
            print(blanco+"-------------------------------------------------------------------------------------------"+reset) 
            print("SUB MENU TIPO DE POKEMÓNES: Ingrese el nombre o nro. de los tipos mostrados")
            print(blanco+"-------------------------------------------------------------------------------------------"+celeste) 
            menuTipo= subMenuTipo()
            cont=0
            for i in  menuTipo:
                print("{:>2})".format(cont+1),i)
                cont+=1
            print(blanco+"-------------------------------------------------------------------------------------------"+reset)

            tipo=input(verde+"Ingresesu opción para listar pokemones por tipo: "+reset)

            if listarPokemonPorTipo(tipo)!=None: 
                print(listarPokemonPorTipo(tipo))
        #OPCION 6
        elif op==6:
            break
        else:
                print(rojo+"DEBERA INGRESAR SOLO LAS OPCIONES MOSTRADAS DEL 1-6\nREGRESE AL MENÚ "+reset)
                  
menu()
