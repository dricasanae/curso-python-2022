
def menu():
    print('''
      AGENDA DE CONTATOS \n
        Menu de Opções:
    (1) Inserir contato
    (2) Atualizar contato
    (3) Mostrar agenda
    (4) Buscar contato (CPF)
    (5) Buscar contato (email)
    (6) Buscar contato (nome)
    (7) Buscar contato (curso)
    (8) Quantidade de contatos
    (9) Deletar contato (CPF)
    (10) Deletar contato (email)
    (11) Salvar e sair
    ''')
    opcao = int(input("Digite a opção desejada: "))
    return opcao