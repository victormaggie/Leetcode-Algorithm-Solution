
SELECT
    e1.DepartmentId AS DepartmentId,
    e1.Name AS Employee,
    e1.Salary AS Salary

FROM   Employee e1 
JOIN Department d 
ON e1.DepartmentId = d.Id 
WHERE 3 > (
    SELECT COUNT(*)
    FROM Employee e2 
    WHERE e2.Salary > e1.Salary AND e2.DepartmentId = e1.DepartmentId
)