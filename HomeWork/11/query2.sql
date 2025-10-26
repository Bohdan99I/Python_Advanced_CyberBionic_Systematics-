SELECT s.id_student, s.firstname, s.lastname, g.name AS group_name, g.facultet
FROM students s
JOIN groups g ON s.group_id = g.id
WHERE g.name = 'CS-101';
