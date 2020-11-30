SELECT 
    month, 
    country, 
    SUM(IF(state='approved', 1, 0)) AS approved_count,
    SUM(IF(state='approved', amount, 0)) AS approved_amount, 
    SUM(IF(state='back', 1, 0)) AS chargeback_count, 
    SUM(IF(state='back', amount, 0)) AS chargeback_amount
FROM
(
    SELECT 
        LEFT(chargebacks.trans_date, 7) AS month, 
        country, 
        "back" AS state, 
        amount
    FROM chargebacks
    JOIN transactions 
    ON chargebacks.trans_id = transactions.id
    UNION ALL
    SELECT LEFT(trans_date, 7) AS month, country, state, amount
    FROM transactions
    WHERE state = "approved"
) s
GROUP BY month, country


