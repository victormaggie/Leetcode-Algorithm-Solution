-- 12-24-2019

-- Solution 1
SELECT
    MAX(Salary) as 'SecondHighestSalary'

FROM Employee
WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee)
;

-- Solution 2
SELECT
    MAX(Salary) as 'SecondHighestSalary'
FROM Employee
WHERE Salary < (SELECT MAX(Salary) From Employee))
;

-- Solution 3 using sub-query and limit

SELECT
( SELECT DISTINCT
    Salary
FROM Employee
ORDER BY Salary DESC
Limit 1 OFFSET 1
) AS 'SecondHighestSalary';

-- Solution 4 using IFNULL and LIMIT
SELECT
    IFNULL(
        (SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
            LIMIT 1 OFFSET 1),
        NULL
    ) AS 'SecondHighestSalary';


