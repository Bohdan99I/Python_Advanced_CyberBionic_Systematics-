SELECT 
    s.id_student,
    s.firstname,
    s.lastname,
    ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON g.student_id = s.id_student
WHERE s.id_student = 1
GROUP BY s.id_student, s.firstname, s.lastname;