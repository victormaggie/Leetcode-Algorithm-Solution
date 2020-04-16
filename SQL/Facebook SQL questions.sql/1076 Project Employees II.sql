SELECT
    project_id
FROM Project p 
LEFT JOIN Employee e  
GROUP BY project_id 
HAVING COUNT(DISTINCT e.employee_id) = 
    (
        SELECT
            COUNT(e.employee_id)
        FROM Project p 
        LEFT JOIN employee_id e 
        ON p.employee_id = e.employee_id
        GROUP BY project_id 
        ORDER BY COUNT(DISTINCT e.employee_id) DESC
        LIMIT 1
    )



/*Solutio 2 
This is a bit tricky answer to some extend
*/

SELECT 
    project_id 
FROM project 
GROUP BY project_id
HAVING count(project_id) = 
(
    SELECT COUNT(project_id) as cnt 
    FROM project 
    GROUP BY project_id 
    ORDER BY count(project_id) DESC
    LIMIT 1
)