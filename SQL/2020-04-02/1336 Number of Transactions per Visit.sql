SELECT CAST(v5.transactions_count AS UNSIGNED INT) AS transactions_count, COALESCE(v4.visits_count,0) AS visits_count
FROM 
    (
    SELECT (@counter := @counter + 1) AS transactions_count
    FROM Transactions, (SELECT @counter := -1) c1
    /*check here*/
    WHERE @counter + 1 <= (SELECT COUNT(*) FROM Transactions GROUP BY user_id, transaction_date ORDER BY COUNT(*) DESC LIMIT 1)
    UNION SELECT(0)
    ) v5
LEFT JOIN
    (
    SELECT v3.transactions_count, COUNT(v3.user_id) AS visits_count
        FROM
        (
            SELECT v2.user_id, v2.visit_date, SUM(v2.transact_flag) AS transactions_count
                FROM
                    (
                        SELECT v1.user_id, v1.visit_date, CASE WHEN t1.transaction_date IS NULL THEN 0 ELSE 1 END AS transact_flag
                        FROM Visits v1
                        LEFT JOIN Transactions t1
                        ON v1.user_id = t1.user_id AND v1.visit_date = t1.transaction_date
                    ) v2
                GROUP BY v2.user_id, v2.visit_date
        ) v3
    GROUP BY v3.transactions_count
    ) v4
ON v5.transactions_count = v4.transactions_count;





