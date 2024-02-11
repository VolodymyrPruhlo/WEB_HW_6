SELECT t.name, t.surname, AVG(g.grade) AS average_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.subject_id
JOIN teachers t ON sub.teacher_id = t.teacher_id
WHERE t.name = 'John' AND t.surname = 'Doe' -- Приклад для викладача "John Doe"
GROUP BY t.teacher_id;
