/*subquery for this questions*/

SELECT 
    MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee)

/*If there is no second value
This might lead to the bug
We need to solve this function by analyze the null
*/
SELECT 
    IFNULL(
        (SELECT DISTINCT Salary AS SecondHighestSalary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1)
        ,NULL
    ) AS SecondHighestSalary

