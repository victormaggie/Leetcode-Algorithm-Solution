/* Look again for this new subquery*/

SELECT 
    student_id,
    MIN(course_id) AS course_id,
    grade

FROM 
    Enrollments
WHERE
    (student_id, grade) in
    (
        SELECT student_id, MAX(grade) AS grade
        FROM Enrollments
        GROUP BY student_id
    )

GROUP BY student_id
ORDER BY student_id

