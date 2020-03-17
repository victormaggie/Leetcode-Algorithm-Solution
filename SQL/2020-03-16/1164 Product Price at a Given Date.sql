
SELECT
    DISTINCT a.product_id,
    IFNULL(temp.new_price, 10) AS price
FROM
    Products a 

LEFT JOIN
    (
        SELECT *
        FROM Products
        WHERE (product_id, change_date) IN 
            (
                SELECT product_id,
                    MAX(change_date)
                FROM Products
                WHERE change_date <= "2019-08-16"
                GROUP BY product_id
            )
    ) AS temp

ON a.product_id = temp.product_id


