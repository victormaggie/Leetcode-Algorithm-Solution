SELECT
    DISTINCT login_date,
    COUNT(*) user_count
FROM
    /*get every user's first login date, then take a subset
    1. use min(activity_date) as the smallest selection
    2. date_add('2019-06-30', INTERVAL - 90 day) 
    3. adddate('2019-06-30', -90)
    */
    (
        SELECT user_id, min(activity_date) login_date
        FROM traffic
        WHERE activity = 'login'
        GROUP BY user_id) a 
    WHERE login_date BETWEEN date_add('2019-06-30', INTERVAL - 90 day) AND '2019-06-30'

GROUP BY login_date



