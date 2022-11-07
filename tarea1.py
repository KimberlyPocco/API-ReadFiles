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
    def __del__(self):
        print("\tLibro eliminado")
        return None

#Crear el método mostrar libro
    def mostrarLibro(self):
        print("{0:3} {1:30} {2:15} {3:15} {4:25} {5}".format(self.id, self.titulo,self.genero,self.ISBN,self.editorial,self.autores), end="")

