SELECT 
    customer_number
FROM
    order o
GROUP BY o.customer_number
ORDER BY count(*) DESC
LIMIT 1

