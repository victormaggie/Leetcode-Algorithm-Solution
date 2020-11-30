SELECT 
    America,
    Asia,
    Europe

FROM 
/*use MySql assignment argument for the calculation*/
    (SELECT @am := 0, @as := 0, @eu :=0) t,
    (
        SELECT 
            @am := @am + 1 AS amid,
            name AS America
        FROM  
            student
        WHERE
            continent = 'America'
        ORDER BY America
    ) t1

    LEFT JOIN

    (
        SELECT
            @as := @as + 1 AS asid,
            name AS Asia
        FROM
            student
        WHERE
            continent = 'Asia'
        ORDER BY Asia
    ) t2

    ON amid = asid

    LEFT JOIN
    (
        SELECT
            @eu := @eu + 1 AS euid,
            name AS Europe
        FROM 
            student
        WHERE   
            continent = 'Europe'
        ORDER BY Europe
    ) t3

    ON euid = amid



/* Another solution for the calculation*/

SELECT  MIN(America) AS America,
        MIN(Asia) AS Asia,
        MIN(Europe) AS Europe
FROM
(
    SELECT  
        CASE
            WHEN continent = 'America' THEN @am := @am + 1
            WHEN continent = 'Asia'    THEN @as := @as + 1
            WHEN continent = 'Europe'  THEN @eu := @eu + 1
        END AS rowline,

        CASE WHEN continent = 'America' THEN name END AS America,
        CASE WHEN continent = 'Asia'    THEN name END AS Asia,
        CASE WHEN continent = 'Europe'  THEN name END AS Europe 
    FROM
        student,
        (SELECT @am := 0, @as := 0, @eu := 0) temp
ORDER by name
) t

GROUP BY rowline
