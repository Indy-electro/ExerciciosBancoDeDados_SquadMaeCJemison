import sqlite3

conexao = sqlite3.connect('biblioteca')
cursor = conexao.cursor()


#CONSULTA 2:  Encontrar todos os livros emprestados no momento.
emprestados = cursor.execute('SELECT livros.titulo, cadastro.nome, emprestimos.data_emprestimo, emprestimos.data_devolucao from emprestimos INNER JOIN livros ON emprestimos.id_livro = livros.id_livro INNER JOIN cadastro ON emprestimos.id_usuario = cadastro.id_usuario where FG_devolvido = 0')
for _livrosindisponiveis in emprestados:
    print('Titulo | Usuário com o Livro | Data do Empréstimo | Prazo para Devolução:')
    print(_livrosindisponiveis) 


conexao.commit()

conexao.close