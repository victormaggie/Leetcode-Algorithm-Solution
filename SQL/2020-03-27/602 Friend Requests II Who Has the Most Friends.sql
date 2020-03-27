/* UNION WILL NOT ALLOW DUPLICATES
    UNION ALL WILL ALLOW DUPICATES
*/

SELECT id1 AS id,
    COUNT(*) AS num
FROM 
    (
        SELECT requester_id AS id1, accepter_id AS id2 FROM request_accepted
        UNION
        SELECT accepter_id AS id1, requester_id AS id2 FROM request_accepted
    ) a 

GROUP BY a.id1
ORDER BY COUNT(*) DESC
LIMIT 1
