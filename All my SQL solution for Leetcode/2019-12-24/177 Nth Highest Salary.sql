-- 24- 12 - 2019
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT

BEGIN
    SET N = N - 1;
    RETURN
    (
        SELECT
        Salary
        FROM Employee
        -- GROUP BY to filter out the duplicate one ----> be aware of the group by !!! 
        GROUP BY Salary
        -- ORDER BY DESC  because of Nth highest
        ORDER BY Salary DESC
        LIMIT 1 OFFSET N
    );

END