SELECT 
    customer_id
FROM customer c 
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUTN(*) FROM product)

