-- solution 1 using group by

SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;

-- solution 2 using temporary table

SELECT Email FROM
(
    SELECT Email, count(Email) as num
    FROM Person
    GROUP BY Email
) AS statistic
WHERE num > 1;