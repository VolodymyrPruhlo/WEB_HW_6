SELECT s.name AS student_name, s.surname AS student_surname, t.name AS teacher_name, t.surname AS teacher_surname, sub.subject_name
FROM grades g
JOIN students s ON g.student_id = s.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
JOIN teachers t ON sub.teacher_id = t.teacher_id
WHERE s.student_id = 1 AND t.teacher_id = 2; -- Приклад для студента з ID 1 і викладача з ID 2
