SELECT
    query_name,
    ROUND(AVG(rating/position), 2) AS quality,
    ROUND(100 * SUM(IF(rating)) / COUNT(*), 2) AS poor_query_percentage

FROM Queries
GROUP BY query_name
