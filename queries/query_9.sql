SELECT s.name, s.surname, sub.subject_name
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE s.student_id = 1 -- Приклад для студента з ID 1
GROUP BY sub.subject_id;
