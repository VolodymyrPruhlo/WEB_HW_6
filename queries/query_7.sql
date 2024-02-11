SELECT s.student_id, s.name, s.surname, g.grade
FROM grades g
JOIN students s ON g.student_id = s.student_id
JOIN `groups` gr ON s.group_id = gr.group_id
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE gr.group_name = 'A' AND sub.subject_name = 'Math'; -- Приклад для групи "A" і предмета "Math"
