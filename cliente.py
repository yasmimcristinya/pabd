#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome_empresa, endereco, telefone):
    db.cur.execute("""
                   INSERT into empresa (nome_empresa, endereco, telefone)
                   VALUES ('%s','%s','%s')
                   """ % (nome_empresa, endereco, telefone))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM empresa
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

#função para excluir dados
def excluir(id):
  db.cur.execute("""
                DELETE FROM empresa where id_funcionario= '%s'
  """ % (id))
  db.con.commit()