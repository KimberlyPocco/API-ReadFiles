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

#Crear una variable listaLibro para levantar temporalmente a memoria la lista de objetos
listaLibro :list= []
#crear variable de formato colores
amarillo='\033[33m'
rojo = '\033[31m'
verde = '\033[32m'
morado = '\033[35m'
celeste = '\033[36m'
blanco = '\033[37m'
reset = '\033[39m'

#Crear la funcion menu
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


while True:
    menu()
    op=int(input(rojo+"INGRESE UNA OPCIÓN DEL MENÚ: "+reset))
    #OPCION 1
    if op==1:
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        print(blanco+"OPCIÓN 1: LEER ARCHIVO")
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        nombreArchivo = input(amarillo+"\tIngrese el nombre del archivo .csv o .txt: "+reset)
        try:
            archivo = open(nombreArchivo,'r')
            print(verde+"\tSe leyo correctamente el libro: ",archivo.name) #validar apertura archivo
            listaLinea:list = []
            for i in archivo:
                linea = i.split(",")
                if linea[0] != "id":
                    a = Libro(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5])
                    listaLibro.append(a)
            archivo.close()
        except:
            print(rojo+"\tNombre de archivo no encontrado en disco duro. No existe el archivo: "+reset,nombreArchivo )
    #OPCION 2
    elif op==2:
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        print("LISTAR LIBRO")
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        
        print(celeste+"{0:3} {1:30} {2:15} {3:15} {4:25} {5}".format('ID', 'TITULO', 'GENERO','ISBN','EDITORIAL','AUTOR'+reset))
        for libro in listaLibro:
            libro.mostrarLibro()
    
    elif op==3:
    #OPCION 3
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        print("REGISTRAR LIBRO") 
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        flagWhile = True
        while flagWhile:
            id = input(amarillo+"\tIngrese el id del libro: "+ reset)
            for j in range(len(listaLibro)):
                if listaLibro[j].id == id:
                    print(rojo+"\tEl ID de ese libro ya existe. Por favor ingrese otro Id"+reset)
                    break
            if j+1 == len(listaLibro) and listaLibro[j].id != id:
                flagWhile = False
        titulo= (input(amarillo+"\tIngrese el título del libro: "+ reset))
        genero= (input(amarillo+"\tIngrese el género del libro: "+ reset))
        isbn= input(amarillo+"\tIngrese el ISBN del libro: ")
        editorial= input(amarillo+"\tIngrese la editorial del libro: "+ reset)
        autores= input(amarillo+"\tIngrese nombre de los autores(es): "+ reset)
        autores = autores + "\n"
        a = Libro(id,titulo,genero,isbn,editorial,autores)
        listaLibro.append(a)
        print(verde+"\tLibro agregado exitosamente"+reset)
    #OPCION 4
    elif op == 4:
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        print("ELIMINAR LIBRO")
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        flagWhile = True
        while flagWhile:
            id = (input(amarillo+"\tIngrese el id del libro a eliminar: "+reset))
            for j in range(len(listaLibro)):
                if listaLibro[j].id == id:
                    flagWhile = False
                    break
            if j+1 == len(listaLibro) and flagWhile:
                print(rojo+"\tNo se encontró el Id del libro a eliminar"+reset)

        if flagWhile == False:
            a = listaLibro.pop(j)
            del a
    #OPCION 5
    elif op == 5:
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        print("BUSCAR LIBRO")
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        print(blanco+"Opción 1: Búsqueda por ISBN"+reset)
        print(blanco+"Opción 2: Búsqueda por título "+reset)
        print(blanco+"----------------------------------------------------------------------------------------------------------------------"+reset)
        opBusqueda=int(input(morado+"Ingrese el número de su opción de búsqueda del libro: "+reset))
        flagBusqueda = False
        if opBusqueda==1:
            parametroBusqueda=input(amarillo+"\tIngrese el ISBN: "+reset)
            for libro in listaLibro:
                if libro.ISBN==parametroBusqueda:
                    libro.mostrarLibro()
                    flagBusqueda = True
            if flagBusqueda == False:
                print(rojo+"\tNo se existe un libro con el ISBN ingresado."+reset)
        elif opBusqueda==2:
            parametroBusqueda=input(amarillo+"\tIngrese el título: "+reset)
            for libro in listaLibro:
                if libro.titulo==parametroBusqueda:
                    libro.mostrarLibro()
                    flagBusqueda = True
            if flagBusqueda == False:
                print(rojo+"\tNo se existe un libro con ese título ingresado"+reset)
        else:
            print(rojo+"\tEl número de la opción ingresada no es correcta"+reset)
    #OPCIÓN 6 
    elif op == 6:
        print(blanco+"-------------------------------------------------------------------------------------")
        print("ORDENAR LIBRO POR TÍTULO")
        print(blanco+"-------------------------------------------------------------------------------------")
        listaLibro = sorted(listaLibro, key=lambda libro : libro.titulo)
        print(celeste+"{0:3} {1:30} {2:15} {3:15} {4:25} {5}".format('ID', 'TITULO', 'GENERO','ISBN','EDITORIAL','AUTOR'+reset))
        for libro in listaLibro:
            libro.mostrarLibro()
        
        print(verde+"\nSe ordenó exitosamente los libros por título"+reset)
    #OPCIÓN 7
    elif op == 7:
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        print("BUSCAR LIBRO")
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        print(blanco+"Opción 1: Búsqueda por autor"+reset)
        print(blanco+"Opción 2: Búsqueda por editorial "+reset)
        print(blanco+"Opción 3: Búsqueda por género "+reset)
        print(blanco+"----------------------------------------------------------------------------------------------------------------------"+reset)
        opBusqueda=int(input(morado+"Ingrese su opción de búsqueda: "+reset))

        flagBusqueda = False
        if opBusqueda==1:
            parametroBusqueda=input(amarillo+"\tIngrese el autor: "+reset)
            parametroBusqueda = parametroBusqueda + "\n"
            for libro in listaLibro:
                if libro.autores==parametroBusqueda:
                    libro.mostrarLibro()
                    flagBusqueda = True
            if flagBusqueda == False:
                print(rojo+"\tNo hay libros con ese autor"+reset)
        elif opBusqueda==2:
            parametroBusqueda=input(amarillo+"\tIngrese la editorial: "+reset)
            for libro in listaLibro:
                if libro.editorial==parametroBusqueda:
                    libro.mostrarLibro()
                    flagBusqueda = True
            if flagBusqueda == False:
                print(rojo+"\tNo hay libros de esa editorial")
        elif opBusqueda==3:
            parametroBusqueda=str(input(amarillo+"\tIngrese el género: "+reset))
            for libro in listaLibro:
                if libro.genero==parametroBusqueda:
                    libro.mostrarLibro()
                    flagBusqueda = True
            if flagBusqueda == False:
                print(rojo+"\tNo hay libros de ese género")
        else:
            print(rojo+"La opción ingresada no es correcta")
    #OPCION 8
    elif op == 8:
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        print("BUSCAR LIBRO POR CANTIDAD DE AUTORES")
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        numAutores=int(input(blanco+"Ingrese el número de autores del libro: "+reset))
        flagBusqueda = False
        print(celeste+"MOSTRAR CANTIDAD DE LIBROS CON ", numAutores," AUTOR(ES)"+ reset)
        print(celeste+"----------------------------------------------------------------------------------------------------------------------"+reset)
        for libro in listaLibro:
            if libro.cantAutores == numAutores:
                libro.mostrarLibro()
                flagBusqueda = True
        print(celeste+"----------------------------------------------------------------------------------------------------------------------"+reset)
        if flagBusqueda == False:
            print(rojo+"No existen libro(s) con ",numAutores, "autor(es)"+reset)
    #OPCION 9
    elif op == 9:
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        print("EDITAR LIBRO")
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        flagWhile = True
        while flagWhile:
            id = (input(morado+"Ingrese el id del libro a editar: "+reset))
            for j in range(len(listaLibro)):
                if listaLibro[j].id == id:
                    flagWhile = False
                    break
            if j+1 == len(listaLibro) and flagWhile:
                print(rojo+"No se encontró el Id del libro a editar"+reset)
        #Editar campos a editar (título, género, ISBN, editorial y autores)
        while True:
            print(amarillo+"\t¿Desea editar el título? No: 0 o Sí: 1"+reset)
            opcion=int(input("\tIngrese la opcion: "))
            if opcion == 0 or opcion == 1:
                break
            else: 
                print("\tOpción NO válida. Ingrese 1 o 0")
        if opcion == 1:
            titulo= (input("\tIngrese el titulo del libro: "))
            listaLibro[j].titulo = titulo
        
        while True:
            print(amarillo+"\t¿Desea editar el género? No: 0 o Sí: 1"+reset)
            opcion=int(input("\tIngrese la opcion: "))
            if opcion == 0 or opcion == 1:
                break
            else:
                print(rojo+"\tOpción NO válida. Ingrese 1 o 0"+reset)
        if opcion == 1:
            genero= (input("\tIngrese el genero del libro: "))
            listaLibro[j].genero = genero

        while True:
            print(amarillo+"\t¿Desea editar el ISBN? No: 0 o Sí: 1"+reset)
            opcion=int(input("\tIngrese la opcion: "))
            if opcion == 0 or opcion == 1:
                break
            else:
                print(rojo+"\tOpción NO válida. Ingrese 1 o 0"+reset)
        if opcion == 1:
            isbn= input("\tIngrese el ISBN del libro: ")
            listaLibro[j].ISBN = isbn

        while True:
            print(amarillo+"\t¿Desea editar el editorial? No: 0 o Sí: 1"+reset)
            opcion=int(input("\tIngrese la opcion: "))
            if opcion == 0 or opcion == 1:
                break
            else:
                print(rojo+"\tOpción NO válida. Ingrese 1 o 0"+reset)
        if opcion == 1:
            editorial= input("\tIngrese la editorial del libro: ")
            listaLibro[j].editorial = editorial

        while True:
            print(amarillo+"\t¿Desea editar el autor(es)? No: 0 o Sí: 1"+reset)
            opcion=int(input("\tIngrese la opcion: "))
            if opcion == 0 or opcion == 1:
                break
            else:
                print(rojo+"\tOpción NO válida. Ingrese 1 o 0"+reset)
        if opcion == 1:
            autores = input("\tIngrese nombre de los autores(es): ")
            autores = autores + "\n"
            listaLibro[j].autores = autores

        print(verde+"\tLibro editado exitosamente"+reset)

    elif op == 10:
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        print("GUARDAR LIBROS")
        print(blanco+"----------------------------------------------------------------------------------------------------------------------")
        nombArchGuardar = input(morado+"\tIngrese el nombre del archivo a guardar .csv o .txt: "+reset)
        fileGuardar = open(nombArchGuardar,'w')
        for libro in listaLibro:
            lineaGuardar = libro.id+","+libro.titulo+","+libro.genero+","+libro.ISBN+","+libro.editorial+","+libro.autores
            fileGuardar.write(lineaGuardar)
        fileGuardar.close()
        print(verde+"\tLibros guardados exitosamente en el archivo ",nombArchGuardar+reset)
    elif op == 11:
        break
