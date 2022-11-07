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