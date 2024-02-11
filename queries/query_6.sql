SELECT s.student_id, s.name, s.surname
FROM students s
JOIN `groups` g ON s.group_id = g.group_id
WHERE g.group_name = 'A'; -- Приклад для групи "A"
