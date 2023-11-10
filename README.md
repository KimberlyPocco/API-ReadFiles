# ReadFiles

## Caso Practico 01:

Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, editorial y autor(es). Considerar que un libro puede tener varios autores.

Se solicita escribir un programa en Python que permita registrar libros. Debe utilizar: colecciones (listas, tuplas, etc), funciones y clases de Python.

Dicho programa debe tener un menu (a interactuar en la línea de comando) para:

* Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
* Opción 2: Listar libros.
* Opción 3: Agregar libro.
* Opción 4: Eliminar libro.
* Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
* Opción 6: Ordenar libros por título.
* Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.
* Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.
* Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
* Opción 10: Guardar libros en archivo de disco duro (.txt o csv).
### Nota: listar libros involucra: título, género, ISBN, editorial y autor(es)

## Caso Practico 02:
Con la PokeAPI: https://pokeapi.co/docs/v2 utilizar la API v2 y el paquete requests de Python

Escribir un programa que tenga las siguientes opciones:

* Opción 1: Listar pokemons por generación. Se ingresa alguna generación (1, 2, 3, ..) y se listan todos los pokemon respectivos.
* Opción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) y se listan todos los pokemons respectivos.
* Opción 3: Listar pokemons por habilidad. Se deben sugerir opciones a ingresar para interactuar.
* Opción 4: Listar pokemons por habitat. Se deben sugerir opciones a ingresar para interactuar.
* Opción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar para interactuar.
### Nota: listar pokemons involucra: nombre, habilidad y URL de la imagen
##  Libreria Usada en el proyecto

Las solicitudes están disponibles en PyPI:

```consola
$ python -m solicitudes de instalación de pip
```

Las solicitudes admiten oficialmente Python 3.7+.

##  Funciones admitidas y prácticas recomendadas

Requests está listo para las demandas de crear aplicaciones sólidas y confiables que hablan HTTP, para las necesidades de hoy.

- Keep-Alive y agrupación de conexiones
- Dominios y URL internacionales
- Sesiones con persistencia de cookies
- Verificación TLS/SSL estilo navegador
- Autenticación básica y implícita
- Cookies similares a `dict` familiares
- Descompresión y decodificación automática de contenido
- Cargas de archivos de varias partes
- Soporte de proxy SOCKS
- Tiempos de espera de conexión
- Descargas de transmisión
- Reconocimiento automático de `.netrc`
- Solicitudes HTTP fragmentadas

##  Referencia de la API y guía del usuario disponibles en [ Leer los documentos ](https://requests.readthedocs.io)

