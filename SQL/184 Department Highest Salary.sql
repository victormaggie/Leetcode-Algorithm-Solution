
-- 24-12-2019

SELECT 
    Department.name AS 'Department',
    Employee.name   AS 'Employee',
    Salary
FROM 
    Employee
JOIN
    Department
ON
    Employee.DepartmentId = Department.Id 
WHERE
    (Employee.DepartmentId, Salary) IN
    (
        SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    )

;

-- Here left join cannot work???