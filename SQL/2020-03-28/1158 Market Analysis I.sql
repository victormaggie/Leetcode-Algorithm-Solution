SELECT
    u.user_id AS buyer_id,
    join_date,
    CASE
        WHEN t.item_id IS NULL THEN 0
        ELSE COUNT(*)
    END AS orders_in_2019

FROM 
    Users u 
    LEFT JOIN 
    (SELECT * FROM Orders WHERE order_date BETWEEN '2019-01-01' AND '2019-12-31') t 
    ON u.user_id = t.buyer_id 

GROUP BY u.user_id 


/*COALESCE*/
/*YEAR(2019)*/
/*IFNULL function*/


SELECT
    u.user_id AS buyer_id,
    join_date,
    coalesce(orders_in_2019, 0) AS orders_in_2019 

FROM 
    Users u 
    LEFT JOIN 
    (SELECT buyer_id, count(order_date) AS orders_in_2019 FROM Orders WHERE order_date BETWEEN '2019-01-01' AND '2019-12-31' GROUP BY buyer_id) t 
    ON u.user_id = t.buyer_id 