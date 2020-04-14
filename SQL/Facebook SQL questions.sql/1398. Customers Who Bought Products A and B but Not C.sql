SELECT
    customer_id,
    customer_name AS customer_name
FROM
    customers
WHERE
    customer_id IN
    (
        SELECT customer_id FROM Orders WHERE product_name = 'A'
    )
    AND
    customer_id IN
    (
        SELECT customer_id FROM Orders WHERE product_name = 'B'
    )
    customer_id NOT IN
    (
        SELECT customer_id FROM Orders WHERE product_name = 'C'
    )

    