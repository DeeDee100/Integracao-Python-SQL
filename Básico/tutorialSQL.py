import pyodbc

dados_conexao = (
	"Driver={SQL Server};"
	"Server=DESKTOP-D2V70T0\sqlexpress;"
	"Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexao bem-sucedida")

cursor = conexao.cursor()

comando = """INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    (2, 'Dee', 'IPHON', '15/02/2021', 8000, 1)"""

cursor.execute(comando)
cursor.commit()