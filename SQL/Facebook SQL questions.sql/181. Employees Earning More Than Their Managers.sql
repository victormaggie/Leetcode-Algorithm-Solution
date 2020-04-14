SELECT 
    e1.Name AS Employee
FROM Employee e1
JOIN Employee e2
ON e1.Employee = e2.Employee
WHERE e1.salary > e2.salary

/*Solution 2*/

SELECT  a.name AS 'Employee'
FROM    Employee e1,
        Employee e2
WHERE e1.ManagerId = e2.Id AND e1.salary > e2.salary
;