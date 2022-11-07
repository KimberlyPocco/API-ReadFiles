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

