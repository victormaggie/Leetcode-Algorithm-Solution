SELECT
    seller_id
FROM Sales
GROUP BY seller_id
HAVING SUM(price) = (SELECT SUM(price) AS sum_price
                    FROM Sales
                    GROUP BY seller_id
                    ORDER BY sum_price DESC
                    LIMIT 1)
;