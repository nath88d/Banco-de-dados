-- Deleta FRs e todas as tabelas
-- ALTER TABLE historico_professor drop id_professor;
-- drop table historico_professor;
-- drop table historico_aluno;
-- drop table disciplinas;
-- drop table matriz_curricular;
-- drop table cursos;
-- ALTER TABLE departamentos DROP ID_chefe_departamento;
-- ALTER TABLE grupo_tcc DROP ID_professor_orientador;
-- drop table professores;
-- drop table departamentos;
-- drop table alunos;
-- drop table grupo_tcc;


CREATE TABLE Professores (
    ID_professor INT PRIMARY KEY,
    Nome_professor VARCHAR(100)
);

CREATE TABLE Grupo_TCC (
    ID_grupo INT PRIMARY KEY,
    ID_professor_orientador INT,
    FOREIGN KEY (ID_professor_orientador) REFERENCES Professores(ID_professor) ON DELETE SET NULL
);

CREATE TABLE Alunos (
    ID_aluno INT PRIMARY KEY,
    Nome_aluno VARCHAR(100),
    formado boolean,
    grupo_tcc INT,
    FOREIGN KEY (grupo_tcc) REFERENCES Grupo_TCC(ID_grupo) ON DELETE SET NULL
);


CREATE TABLE Departamentos (
    ID_departamento INT PRIMARY KEY,
    Nome_departamento VARCHAR(100),
    ID_chefe_departamento INT,
    FOREIGN KEY (ID_chefe_departamento) REFERENCES Professores(ID_professor) ON DELETE SET NULL
);


CREATE TABLE Cursos (
    ID_curso INT PRIMARY KEY,
    Nome_curso VARCHAR(100)
);

CREATE TABLE Disciplinas (
    ID_disciplina INT PRIMARY KEY,
    Nome_disciplina VARCHAR(100),
    ID_departamento INT,
    ID_curso INT,
    FOREIGN KEY (ID_departamento) REFERENCES Departamentos(ID_departamento) ON DELETE SET NULL,
    FOREIGN KEY (ID_curso) REFERENCES Cursos(ID_curso)
);


CREATE TABLE Matriz_Curricular (
    id_aluno INT,
    FOREIGN KEY (id_aluno) REFERENCES Alunos(ID_aluno) ON DELETE SET NULL,
    ID_curso INT,
    FOREIGN KEY (ID_Curso) REFERENCES Cursos(ID_curso) ON DELETE SET NULL,
    ano INT,
    semestre INT
);

CREATE TABLE Historico_Aluno (
    id_aluno INT,
    ID_disciplina INT,
    Semestre INT,
    Ano INT,
    Nota_final DECIMAL(4,2),
    FOREIGN KEY (ID_disciplina) REFERENCES Disciplinas(ID_disciplina) ON DELETE SET NULL,
    FOREIGN KEY (id_aluno) REFERENCES alunos(ID_aluno) ON DELETE SET NULL
);


CREATE TABLE Historico_Professor (
    ID_professor INT,
    ID_disciplina INT,
    Semestre INT,
    Ano INT,
    FOREIGN KEY (ID_professor) REFERENCES Professores(ID_professor) ON DELETE SET NULL,
    FOREIGN KEY (ID_disciplina) REFERENCES Disciplinas(ID_disciplina) ON DELETE SET NULL
);


ALTER TABLE Professores
ADD departamento INT,
ADD FOREIGN KEY (departamento) REFERENCES Departamentos(ID_departamento) ON DELETE SET NULL;

