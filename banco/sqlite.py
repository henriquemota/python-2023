import os
import sqlite3 as conector

dirname = os.path.dirname(__file__)
url = os.path.join(dirname, 'data', 'mydb.db')

def criar_banco():
  try:
    conexao = conector.connect(url)
    cursor = conexao.cursor()

    sql = (
        'create table if not exists pessoas ('
        'id int primary key,'
        'nome varchar(100)'
        ');'
    )

    cursor.execute(sql)
  except conector.DatabaseError as err:
    print('erro de banco de dados')
  except conector.Error as err:
    print('erro')
  finally:
    cursor.close()
    conexao.close()
