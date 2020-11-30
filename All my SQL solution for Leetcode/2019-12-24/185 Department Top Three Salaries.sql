SELECT
    d1.name AS 'Department',
    e1.name AS 'Employee',
    e1.Salary
FROM
    Employee e1
JOIN
    Department d1
ON
    e1.DepartmentId = d1.Id 
WHERE
    3 > (
        SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary AND e1.DepartmentId = e2.DepartmentId
    )
;

