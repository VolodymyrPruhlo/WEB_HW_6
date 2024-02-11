SELECT s.student_id, s.name, s.surname, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE sub.subject_name = 'Math' -- Приклад для предмета "Math"
GROUP BY s.student_id
ORDER BY average_grade DESC
LIMIT 1;
