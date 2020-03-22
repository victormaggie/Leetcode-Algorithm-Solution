/* using subquery method
    1. select time between oct 1. 2020 and oct 3. 2020
    2. group by data
    3. calculate the ratio use AVG() function
*/

SELECT 
    Request_at AS Day,
    ROUND(AVG(T.Status = 'cancelled_by_client' OR T.Status = 'cancelled_by_driver' ), 2) AS 'Cancellation Rate'

FROM 
    (
        SELECT
            *
        FROM    
            Trips
        INNER JOIN
            Users
        ON Trips.Client_Id = Users.Users_Id
        WHERE Trips.Request_at BETWEEN '2013-10-01' AND '2013-10-02' AND User.Banned = 'No'
    ) AS Trips

GROUP BY T.Request_at


/* 
    Solution 2 for this problem
*/

SELECT 
    T.Request_at,
    ROUND((COUNT(IF(T.Status != 'completed', TRUE, NULL) / COUNT(*))), 2) AS 'Cancellation Rate'

FROM 
    Trips T
WHERE
    T.Client_Id in 
        (
            SELECT  
                Users_Id 
            FROM 
                Users
            WHERE
                Banned = 'No'
        )
    
    AND
    T.Driver_Id in
    (
        SELECT 
            Users_Id
        FROM
            Users
        WHERE
            Banned = 'No'
    )

    AND 
    T.Request_at between '2013-10-01' AND '2013-10-03'

GROUP BY T.Request_at

