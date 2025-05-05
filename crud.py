class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

        def __str__(self):
            return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"
        livros = []

        def criar_livro():
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            isbn = input("Digite o ISBN do livro: ")
            novo_livro = Livro(titulo, autor, isbn)
            livros.append(novo-livro)
            print("Livro adicionado com sucesso!")

        def ler_livros():
            if not livros:
                print("Não há livros cadastrados.")
                return
            print("\n--- Lista de liros ---")
            for livro in livros:
                print(livro)
                print("------------------\n")

        def ler_livros_por_isbn(isbn_busca):
            for livro in livros:
                if livro.isbn == isbn_busca:
                    print(livro)
                    return
                print(f"Livro com ISBN '{isbn_busca}' não encontrado.")
        
        def atualizar_livro():
            isbn_busca = input("Digite o ISBN do livro que você deseja atualizar: ")
            for livro in livros:
                if livro.isbn == isbn_busca:
                    print("Livro encontrado. Digite os novos dados:")
                    livro.titulo = input(f"Novo título ({livro.titulo}): ") 
                    livro.autor = input(f"Novo autor ({livro.autor}): ")
                    livro.isbn = input(f"Novo ISBN ({livro.isbn}): ")
                    print("Livro atualizado com secesso!")
                    return
                print(f"Livro com ISBN '{isbn_bsuca}' não encontrado.")

        def deletar_livro():
            isbn_busca = input("Digite o ISBNdo livro que você deseja deletar: ")
            for i, livro in enumerate(livros):
                if livro.isbn == isbn_busca:
                    del livros[i]
                    print("Livro deletado com sucesso!")
                    return
                print(f"Livro com ISBN '{isbn_busca}' não encontrado.")

        def exibir_menu():
            print("\n--- Menu CRUD de Livros ---")
            print("1. Adcionar Livro (Create)")
            print("2. Listar Livros (Read)")
            print("3. Buscar Livro por IBSN (Read)")
            print("4. Atualizar Livro (Update)")
            print("5. Deletar Livro (Delete)")
            print("6. Sair")
            opcao = input("Escolha uma opção: ")
            return opcao
        
        def main():
            while True:
                opcao = exibir_menu()
                if opcao == '1':
                    criar_livro()
                elif opcao == '2':
                    ler_livros()
                elif opcao == '3':
                    isbn_busca = input("Digite o ISBN do livro que você procura: ")
                    ler_livros_por_isbn(isbn_busca)
                elif opcao == '4':
                    atualizar_livro()
                elif opcao == '5':
                    deletar_livro()
                elif opcao == '6':
                    print("Saindodo programa.")
                    break
                else: 
                    print("Opção inválida. Tente novamente. ")

        if __name__=="__main__":
            main()            