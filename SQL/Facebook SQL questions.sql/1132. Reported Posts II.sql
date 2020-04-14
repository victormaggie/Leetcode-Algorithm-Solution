SELECT 
    ROUND(IFNULL(SUM(daily_num) / COUNT(date), 0), 2) average_daily_percent
FROM
    (
        SELECT  a.action_date date,
                100 * COUNT(DISTINCT r.post_id) / COUNT(DISTINCT a.post_id) 
        FROM    Actions a 
        LEFT JOIN Removals r 
        ON a.post_id = r.post_id 
        WHERE extra = 'spam'
        GROUP BY 1
    ) t

    