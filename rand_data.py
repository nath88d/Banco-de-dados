import names
import random as rand
import psycopg2

num_de_pessoas = int(input("Insira o numero de pessoas para inserir no banco: "))
depart = [453, 654, 236, 735]
formado = [True, False]
URL = input("\nInsira a General String do banco CockroachDB: "); print()

conn = psycopg2.connect(URL)

def executa(comando):
    with conn.cursor() as cur:
        cur.execute(comando)
        conn.commit()

def gerar(query):
    executa(query)
    print(query)

#deleta dados
executa("\
        delete from professores where professores.nome_professor != '';\
        delete from alunos where nome_aluno != '';\
        delete from grupo_tcc where grupo_tcc.id_grupo != '-1';\
        delete from historico_professor where historico_professor.id_disciplina != '-1';\
        delete from disciplinas where disciplinas.nome_disciplina != '';\
        delete from matriz_curricular where semestre != '-1';\
        delete from cursos where cursos.nome_curso != '';\
        delete from departamentos where departamentos.nome_departamento != '';\
        ")
#departamento
gerar("\
    insert into departamentos values (453, 'Computacao', NULL);\
    insert into departamentos values (654, 'Engenharia', NULL);\
    insert into departamentos values (236, 'Administracao', NULL);\
    insert into departamentos values (735, 'Economia', NULL);\
    ")
#cursos
gerar("\
    insert into cursos values(0, 'Administração de Empresas');\
    insert into cursos values(1, 'Gestão de Recursos Humanos');\
    insert into cursos values(2, 'Engenharia Civil');\
    insert into cursos values(3, 'Engenharia Elétrica');\
    insert into cursos values(4, 'Ciência da Computação');\
    insert into cursos values(5, 'Engenharia de Software');\
    insert into cursos values(6, 'Economia');\
    insert into cursos values(7, 'Finanças');\
    ")
#disciplinas
gerar("\
    insert into disciplinas values (0, 'Comp. Sci.', 453, 4);\
    insert into disciplinas values (1, 'Finance', 654, 7);\
    insert into disciplinas values (2, 'Eng. eletrica', 236, 3);\
    insert into disciplinas values (3, 'Physics', 735, 4);\
    INSERT INTO disciplinas VALUES (4, 'Desenvolvimento Web', 453, 4);\
    INSERT INTO disciplinas VALUES (5, 'Mercado de Capitais', 654, 7);\
    INSERT INTO disciplinas VALUES (6, 'Eletromagnetismo', 236, 3);\
    INSERT INTO disciplinas VALUES (7, 'Astrofísica', 735, 4);\
    INSERT INTO disciplinas VALUES (8, 'Gestão de Recursos Humanos', 453, 0);\
    INSERT INTO disciplinas VALUES (9, 'Segurança da Informação', 654, 7);\
    INSERT INTO disciplinas VALUES (10, 'Gestão de Riscos', 236, 3);\
    INSERT INTO disciplinas VALUES (11, 'Energias Renováveis', 735, 4);\
    INSERT INTO disciplinas VALUES (12, 'Mecânica Quântica', 453, 4);\
    INSERT INTO disciplinas VALUES (13, 'Marketing Estratégico', 654, 7);\
    INSERT INTO disciplinas VALUES (14, 'Big Data Analytics', 236, 3);\
    INSERT INTO disciplinas VALUES (15, 'Derivativos Financeiros', 735, 7);\
    INSERT INTO disciplinas VALUES (16, 'Eletrônica de Potência', 453, 3);\
    INSERT INTO disciplinas VALUES (17, 'Física Nuclear', 654, 4);\
    INSERT INTO disciplinas VALUES (18, 'Empreendedorismo', 236, 0);\
    INSERT INTO disciplinas VALUES (19, 'Aprendizado de Máquina', 735, 4);\
    INSERT INTO disciplinas VALUES (20, 'Finanças Corporativas', 453, 7);\
    INSERT INTO disciplinas VALUES (21, 'Telecomunicações', 654, 5);\
    INSERT INTO disciplinas VALUES (22, 'Óptica Avançada', 236, 3);\
    INSERT INTO disciplinas VALUES (23, 'Gestão da Qualidade', 735, 0);\
    ")



with conn.cursor() as cur:
    num = 0
    for i in range(num_de_pessoas): # Insere professores
        q = "insert into professores values ("+ str(num) + ", '" + names.get_full_name() + "', '" + str(depart[(rand.randint(0,3))]) + "');" # 
        gerar(q)
        num += 1
    
    num = 0
    for i in range(num_de_pessoas): # Insere alunos
        q = "insert into alunos values ("+ str(num) + ", '" + names.get_full_name() + "', " + str(formado[(rand.randint(0,1))]) + ", NULL);"
        gerar(q)
        num += 1
    num = 0
    for i in range(num_de_pessoas): #Insere historico professor
        for h in range(1, 4):
            q = "insert into historico_professor values(%d, %d, %d, %d);"%(num, rand.randint(0,23), rand.randint(1,8), rand.randint(2000,2024))
            gerar(q)
        num += 1
    num = 0
    for i in range(round((0.2*num_de_pessoas))): #Insere grupo tcc
        q = "insert into Grupo_TCC values(%d, %d);"%(num, rand.randint(0,num_de_pessoas))
        gerar(q)
        num += 1
    num = 0
    for i in range(num_de_pessoas): #Insere historico aluno / Matriz curricular/ verificar nota e alterar formado
        nota = rand.uniform(0, 10)
        print(nota)
        curso = rand.randint(0,7)
        data_inicial = rand.randint(2000,2024)
        sem_inicial = rand.randint(1,8)
        gerar("insert into matriz_curricular values ('%d', '%d', '%d', '%d')"%(num, curso, data_inicial, 8))
        cur.execute("SELECT id_disciplina FROM disciplinas where id_curso = '%d'"%(curso))
        curso = cur.fetchall()
        semestre = 0
        for m in range(0, (len(curso)-rand.randint(0,4))):
            semestre += 1
            gerar("insert into historico_aluno values('%d', '%d', '%d', '%d', '%.2f')"%(num, m, semestre, data_inicial, nota))
            print(curso[m][0])
            data_inicial += 1
        if((nota >= 5)and(sem_inicial == 8)):
            q = "UPDATE alunos SET formado = 'True' where id_aluno = '%d';\
                 UPDATE alunos SET grupo_tcc = '%d' where id_aluno = '%d';\
                 "%(num, rand.randint(0,round((0.2*num_de_pessoas))), num)
            print("formado")
        else:
            q = "UPDATE alunos SET formado = 'False' where id_aluno = '%d';"%(num)
            print("nao formado")
        gerar(q)
        num += 1

executa("\
    UPDATE departamentos SET id_chefe_departamento = %d where id_departamento = '453';\
    UPDATE departamentos SET id_chefe_departamento = %d where id_departamento = 654;\
    UPDATE departamentos SET id_chefe_departamento = %d where id_departamento = 236;\
    UPDATE departamentos SET id_chefe_departamento = %d where id_departamento = 735;\
    "%(
        rand.randint(0,num_de_pessoas-1),
        rand.randint(0,num_de_pessoas-1),
        rand.randint(0,num_de_pessoas-1),
        rand.randint(0,num_de_pessoas-1)))
