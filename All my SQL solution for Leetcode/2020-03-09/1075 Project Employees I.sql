SELECT p.project_id,
    ROUND(AVG(experience_years), 2) AS average_years

FROM Project p 
JOIN Employee e 
ON p.employee_id = e.employee_id
GROUP BY p.project_id 

/*Time consuming for this questions*/

SELECT p.project_id,
    ROUND(AVG(experience_years), 2) AS average_years

FROM Project p,
    Employee e 
WHERE p.employee_id = e.employee_id 
GROUP BY 1 

