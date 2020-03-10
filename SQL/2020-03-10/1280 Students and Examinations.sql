SELECT a.student_id,a.student_name,a.subject_name,IFNULL(b.attended_exams,0) AS attended_exams FROM
(
    (SELECT student_id,student_name,subject_name FROM students ,subjects ) a
    
LEFT JOIN
    
    (SELECT student_id,subject_name,COUNT(subject_name) AS attended_exams FROM examinations GROUP BY student_id,subject_name)b
    
ON
    a.student_id = b.student_id AND a.subject_name = b.subject_name
) 
ORDER BY a.student_id,a.subject_name

