
/* This is for the calculation of 

COUNT (*) 
WHEN THERE IS A NULL 
HOW TO DO IT

*/

SELECT
    dept_name,
    CASE
        WHEN s.dept_id IS NULL THEN 0
        ELSE COUNT(*)
    END AS student_number

    /*
    here only need COUNT(student_id) Then can avoid use the conditional case
    */

FROM
    department d
LEFT JOIN student s 
ON d.dept_id = s.dept_id
GROUP BY d.dept_name 
ORDER BY student_number DESC, d.dept_name 


/*Be aware of that :

sometimes need to count, then choose to count the specific number

*/
