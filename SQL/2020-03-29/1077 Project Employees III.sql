/*
MAX is aggregating, will only return 1 number

LOOK !!! 
*/

SELECT
    p.project_id,
    e.employee_id
FROM 
    Project p 
LEFT JOIN Employee e 
ON p.employee_id = e.employee_id 
WHERE 
    (p.project_id, e.experience_years) in 
    (SELECT p.project_id, max(e.experience_years) FROM project p JOIN employee e ON e.employee_id = p.employee_id GROUP BY project_id)

