#Crear la clase libro
class Libro:
    def __init__(self,id, titulo, genero, ISBN, editorial,autores):
        self.id=id
        self.titulo=titulo
        self.genero=genero
        self.ISBN=ISBN
        self.editorial=editorial
        self.autores=autores
        self.cantAutores=1
        for i in self.autores:
            if i == '&':
                self.cantAutores+=1
                
#crear Destructor de Clase Libro
    def __del__(self) :
        print("\tLibro eliminado")
        return None
#CREACION DE UNA LISTA Y UN OBJETO QUE LO CONSERVE EN EL CACHE
listaLibro :list= []
#CREACION DE UNA PALETA DE COLORES
amarillo='\033[33m'
rojo = '\033[31m'
verde = '\033[32m'
morado = '\033[35m'
celeste = '\033[36m'
blanco = '\033[37m'
reset = '\033[39m'