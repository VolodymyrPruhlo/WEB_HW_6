SELECT t.name, t.surname, sub.subject_name
FROM teachers t
JOIN subjects sub ON t.teacher_id = sub.teacher_id
WHERE t.name = 'John' AND t.surname = 'Doe'; -- Приклад для викладача "John Doe"
