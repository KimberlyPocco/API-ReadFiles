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
def menu():
    print(blanco+"\n************************************************************************************************************************")
    print(morado+"                            BIENVENIDO AL MENÚ DE LA CLASE LIBRO")
    print(blanco+"************************************************************************************************************************")
    print(amarillo+"Opción 1: Leer archivo de disco duro (.txt o csv)")  
    print("Opción 2: Listar libros")  
    print("Opción 3: Agregar libro")   
    print("Opción 4: Eliminar libro")  
    print("Opción 5: Buscar libro por ISBN o por título")  
    print("Opción 6: Ordenar libros por título")  
    print("Opción 7: Buscar libros por autor, editorial o género")  
    print("Opción 8: Buscar libros por número de autores")  
    print("Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores)")  
    print("Opción 10: Guardar libros en archivo de disco duro (.txt o csv)")  
    print("Opción 11: SALIR")
    print(blanco+"*************************************************************************************************************************")
