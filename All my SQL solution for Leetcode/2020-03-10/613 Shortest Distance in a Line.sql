SELECT
    MIN(ABS(p1.x - p2.x)) AS shortest

FROM 
    point p1
JOIN
    point p2
ON
    /* Generage the permutation of the table*/
    p1.x != p2.x

/*
SELECT 
    MIN(ABS(p1.x - p2.x)) AS shortest
FROM
    point p1
JOIN
    point p2
ON 
    p1.x <> p2.x
*/