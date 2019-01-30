class Book(object):
    def __init__(self):
        self.id_book = None
        self.title = None
        self.sub_title = None
        self.author = []
        self.category = []
        self.publication_date = None
        self.description = None

    def create_book(self, _id):
        self.id_book = _id
        self.title = input("Ingrese el Titulo de libro: ")
        self.sub_title = input("Ingrese el Sub Titulo de libro: ")
        self.author = []
        x = int(input("Ingrese la catidad de autores: "))
        for i in range(0, x):
            self.author.append(input("Ingrese el nombre del autor:"))
        self.category = []
        y = int(input("Ingrese la catidad de categorias: "))
        for i in range(0, y):
            self.category.append(input("Ingrese la categoria: "))
        self.publication_date = input("Ingrese la fecha de publicacion: ")
        self.editor = input("Ingrese la Editorial:")
        self.description = input("Ingrese la Descripcion: ")

    def read_book(self):
        print(
            f'ID Libro: {self.id_book}',
            f'Titulo: {self.title}',
            f'Subtitulo: {self.sub_title}',
            f'Autor: {self.author}',
            f'Categoria: {self.category}',
            f'Fecha de Publicación: {self.publication_date}',
            f'Descripcion:{self.description}'
              )
