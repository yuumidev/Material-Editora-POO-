class Material:
    def __init__(self, titulo, autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora
    
    def exibir_informacoes(self):
        print(f'Título: {self.titulo}')
        print(f'Autor/Editora: {self.autor_ou_editora}')

class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora
        self.genero = genero

    def exibir_informacoes(self):
        print('Informações Livro')
        super().exibir_informacoes()
        print(f'Gênero: {self.genero}')

class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao):
        super().__init__(titulo, autor_ou_editora)
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora
        self.edicao = edicao

    def exibir_informacoes(self):
        print('Informações Revista')
        super().exibir_informacoes()
        print(f'Edição: {self.edicao}')


livroum = Livro('Corte de Rosas e Espinhos','Sarah J. Mass','Fantasia')
livroum.exibir_informacoes()
print('--------------------------------')
revistaum = Revista('Forbes','Forbes Media','Maio 2024')
revistaum.exibir_informacoes()