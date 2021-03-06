import tkinter as tk
from tkinter import ttk
import datetime as dt
import pyodbc

dados_conexao = (
	"Driver={SQL Server};"
	"Server=DESKTOP-D2V70T0\sqlexpress;"
	"Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

comando = "SELECT id_venda FROM Vendas"
cursor.execute(comando)
lastID = cursor.fetchall()[-1][0]

listaTipos =['Galão', "Caixa", "Saco Pequeno", "Saco Grande", 'Unidade', "mL"]

def inserirCodigo():
	cursor.execute(comando)
	lastID = cursor.fetchall()[-1][0]

	nomeProduto = entryDescript.get()
	tipo = comboboxSelecionarTipo.get()
	quantidade = int(entryQauntidade.get())
	cliente = entryCliente.get()
	preco = float(entryPreco.get())
	data_criacao = dt.datetime.now()
	data_criacao = data_criacao.strftime("%d/%m/%y")
	codigo = lastID + 1
	inserirRow = """INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
	VALUES
		(?,?,?,?,?,?)"""
	cursor.execute(inserirRow,(codigo, cliente, nomeProduto, data_criacao, preco,quantidade))
	cursor.commit()


window = tk.Tk()
window.title("Cadastro")

labelCliente =tk.Label(text="Nome do Cliente")
labelCliente.grid(row=1,column=0, padx=0, pady=10, sticky='nswe', columnspan=2)
entryCliente = tk.Entry()
entryCliente.grid(row=1,column=2, padx=10, pady=10, sticky='nswe', columnspan=7)

label_descricao = tk.Label(text='Descrição do Item')
label_descricao.grid(row=3,column=0, padx=0, pady=10, sticky='nswe', columnspan=2)
entryDescript = tk.Entry()
entryDescript.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=8)

labelTipo = tk.Label(text='Tipo da Unidade do Material')
labelTipo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
comboboxSelecionarTipo = ttk.Combobox(values=listaTipos)
comboboxSelecionarTipo.grid(row=5, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

labelQuantidade = tk.Label(text='Quantidade da Unidade do Material')
labelQuantidade.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
entryQauntidade = tk.Entry()
entryQauntidade.grid(row=6, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

labelPreco = tk.Label(text="Preço R$")
labelPreco.grid(row=7, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
entryPreco = tk.Entry()
entryPreco.grid(row=7, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

criarCodigo = tk.Button(text="Criar Código", command=inserirCodigo)
criarCodigo.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=10)

window.mainloop()
