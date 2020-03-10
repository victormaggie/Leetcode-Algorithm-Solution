/*
SELECT 

    a.name
    
SELECT 
    s.name
FROM
    salesperson s
WHERE
    s.sales_id NOT IN
    (
        SELECT 
            o.sales_id
        FROM 
            orders o
        Left JOIN company c
        ON o.com_id = c.com_id
        WHERE 
            c.name = "RED"
    )
*/

SELECT 
    s.name
FROM 
    salesperson s
WHERE
    s.sales_id NOT IN
    (
        SELECT  
            o.sales_id
        FROM 
            orders o
                LEFT JOIN
            company c ON o.com_id = c.com_id 
        WHERE
            c.name = "RED"
    )


