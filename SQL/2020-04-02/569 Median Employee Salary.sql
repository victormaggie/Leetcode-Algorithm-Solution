SELECT 
    Id,
    Company,
    Salary
FROM
    (
        SELECT e.Id, 
                e.Company AS Company,
                e.Salary AS Salary,
                IF(@prev = e.Company, @Rank := @Rank + 1, @Rank := 1) AS ranking,
                @prev := e.Company
        FROM Employee e,
            (SELECT @Rank := 0, @prev := 0) t
        ORDER BY Salary, Company, Id
    ) Rank 

    INNER JOIN
    (
        SELECT COUNT(*) countnum, Company AS name FROM Employee GROUP BY Company
    ) companycount

    ON Rank.Company = companycount.name

WHERE 
    ranking = FLOOR((countnum + 1)/2)
    OR
    ranking = FLOOR((countnum + 2)/2)
