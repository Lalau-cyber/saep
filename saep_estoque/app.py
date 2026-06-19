import tkinter as tk
from tkinter import messagebox
from  banco import cadastrar_produto

janela = tk.Tk()
janela.title("SAEP Estoque Fácil")
janela.geometry("500x400")

titulo = tk.Label(
    janela,
    text="SAEP Estoque Fácil",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=10)

tk.Label(janela, text="Nome do produto:").pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()

tk.Label(janela, text="Categoria:").pack()
entrada_categoria = tk.Entry(janela, width=40)
entrada_categoria.pack()

tk.Label(janela, text="Qunatidade:").pack()
entrada_quantidade = tk.Entry(janela, width=40)
entrada_quantidade.pack()

tk.Label(janela, text="Preço:").pack()
entrada_preco = tk.Entry(janela, width=40)
entrada_preco.pack()

def salvar():
    nome = entrada_nome.get()
    categoria = entrada_categoria.get()
    quantidade = entrada_quantidade.get()
    preco = entrada_preco.get()

    if nome == "" or categoria == "" or quantidade == "" or preco == "":
        messagebox.showwarning("Atenção",
         "Preencha todos os campos ")
        return

    cadastrar_produto(nome, categoria, int(quantidade), float(preco))

    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")

    entrada_nome.delete(0, tk.END)
    entrada_categoria.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)

botao_salvar = tk.Button(
    janela,
    text="Cadastrar Produto",
    command=salvar,
    width=25
)

botao_salvar.pack(pady=20)
janela.mainloop()




# CREATE DATABASE SAEP_ESTOQUE;

# USE SAEP_ESTOQUE;

# CREATE TABLE PRODUTOS(
# ID INT AUTO_INCREMENT PRIMARY KEY,
# NOME VARCHAR(100) NOT NULL,
# CATEGORIA VARCHAR(100) NOT NULL,
# QUANTIDADE INT NOT NULL,
# PRECO DECIMAL(10,2) NOT NULL
# );


# ALTER TABLE PRODUTOS MODIFY COLUMN PRECO INT NOT NULL;
# select * from produtos