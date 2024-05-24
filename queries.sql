-- Tópico 1: historico do aluno
SELECT
    h.ID_disciplina,
    d.Nome_disciplina,
    h.Semestre,
    h.Ano,
    h.Nota_final
FROM
    Historico_Aluno h
JOIN
    Disciplinas d ON h.ID_disciplina = d.ID_disciplina
WHERE
    h.ID_aluno = 2;


-- Tópico 2: historico do prof
SELECT D.Nome_disciplina, H.Semestre, H.Ano
FROM Historico_Professor H
INNER JOIN Disciplinas D ON H.ID_disciplina = D.ID_disciplina
WHERE H.ID_professor = '1';


-- Tópico 3: alunos formados em determinado semestre/ano
SELECT
    a.ID_aluno,
    a.Nome_aluno
FROM
    Alunos a
JOIN
    Matriz_Curricular mc ON a.ID_aluno = mc.ID_aluno
WHERE
    mc.Semestre = '8'
    AND mc.Ano = 2016
    AND a.Formado = TRUE
GROUP BY
    a.ID_aluno, a.Nome_aluno;


-- Tópico 4: lista de professores chefes de departamento
SELECT P.Nome_professor, D.Nome_departamento
FROM Professores P
INNER JOIN Departamentos D ON P.ID_professor = D.ID_chefe_departamento;


-- Tópico 5: alunos que formam grupo de tcc com o nome do orientador
SELECT
    a.ID_aluno,
    a.Nome_aluno,
    g.ID_grupo,
    p.ID_professor,
    p.Nome_professor
FROM
    Alunos a
JOIN
    Grupo_TCC g ON a.grupo_tcc = g.ID_grupo
JOIN
    Professores p ON g.ID_professor_orientador = p.ID_professor
ORDER BY
    g.ID_grupo, a.ID_aluno;





