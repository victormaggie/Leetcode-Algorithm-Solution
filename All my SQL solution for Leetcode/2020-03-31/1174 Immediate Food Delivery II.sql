SELECT
    ROUND(100 * SUM(IF(order_date = customer_pref_delivery_date, 1, 0)) / COUNT(*) , 2) AS immediate_percentage

FROM
    (
        SELECT customer_id,
            min(order_date) order_date,
            /* This is dangerous here if customer_pref_delivery_date is behind the first one*/
            min(customer_pref_delivery_date) customer_pref_delivery_date,
        FROM   
            Delivery 
        GROUP BY customer_id
    ) t




SELECT 
    ROUND(100 * SUM(IF(order_date = customer_pref_delivery_date, 1, 0)) / COUNT(*) , 2) AS immediate_percentage
FROM   
    Delivery
WHERE
    (customer_id, order_date)
IN 
    (SELECT
        customer_id, min(order_date) as min_date
    FROM
        Delivery
    GROUP BY
        customer_id 
    )