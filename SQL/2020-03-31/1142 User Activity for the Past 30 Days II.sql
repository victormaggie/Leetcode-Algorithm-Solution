SELECT 
    IFNULL(ROUND(AVG(num), 2), 0.00) AS average_per_user
FROM
    (
        SELECT COUNT(DISTINCT session_id) AS num
        FROM Activity
        WHERE activity_date > adddate('2019-07-27', -30) AND activity_date < '2019-07-27'
        GROUP BY user_id
    ) AS t


SELECT  
    IFNULL(ROUND(COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id), 2), 0.00)
    AS average_sessions_per_user
FROM    Activity
WHERE activity_date > adddate('2019-07-27', -30) AND activity_date <= '2019-07-27'