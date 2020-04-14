CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT

BEGIN
    SET N = N - 1;
    RETURNS
        (SELECT Salary 
        FROM Employee
        GROUP BY Salary
        ORDER BY 1 DESC
        LIMIT 1
        OFFSET N
        );
END

