SELECT 
    IFNULL(
        ROUND (
                COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id)
            ,0)
        ,0) AS average_sessions_per_user
    
FROM
    activity_date
WHERE DATEDIFF('2019-07-27', activity_date) < 30

/*
WHERE activity_date <= '2019-07-27' AND activity_date > ADDDATE('2019-07-27', -30)
*/

