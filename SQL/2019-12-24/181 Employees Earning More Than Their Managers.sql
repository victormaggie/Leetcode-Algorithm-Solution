SELECT
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE
    -- combine the foreign key here
    a. ManagerId = b.Id AND a.Salary > b.Salary
;
