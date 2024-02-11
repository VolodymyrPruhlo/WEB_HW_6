SELECT gr.group_name, AVG(g.grade) AS average_grade
FROM grades g
JOIN students s ON g.student_id = s.student_id
JOIN `groups` gr ON s.group_id = gr.group_id
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE sub.subject_name = 'Math' -- Приклад для предмета "Math"
GROUP BY gr.group_id;
