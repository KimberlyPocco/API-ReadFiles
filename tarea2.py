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
#SUBMENU DE LISTAR POR FORMA
def subMenuForma():
    resultado=requests.get(f'https://pokeapi.co/api/v2/pokemon-shape/')
    detalleSolicitud : dict =resultado.json()
    resultado= [forma ['name'] for forma in detalleSolicitud['results'] ]
    return resultado