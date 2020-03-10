
SELECT 
    q.query_name,
    ROUND(AVG(q.rating / q.position) ,2) AS quality,
    ROUND(AVG(q.rating < 3) * 100, 2) AS poor_query_percentage
FROM 
    Queries q
GROUP BY q.query_name