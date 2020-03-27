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

