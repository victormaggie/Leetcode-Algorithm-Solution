SELECT 
    MAX(m.num) AS num
FROM
    my_numbers m
WHERE
    m.num NOT IN (
        SELECT
            num
        FROM
            my_numbers
        GROUP BY num
        HAVING COUNT(*) > 1
    )

/* ANOTHER SOLUTION FOR THIS QUESTIONS*/

SELECT
    MAX(num) AS num

SELECT
    MAX(num) AS num
    
FROM
    (
        SELECT
            num
        FROM
            my_numbers
        GROUP BY num
        HAVING COUNT(num) = 1
    ) AS t