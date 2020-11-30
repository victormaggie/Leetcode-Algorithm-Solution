SELECT 
    t.Id1 AS Id,
    COUNT(*) AS num
FROM
    (SELECT requester_id AS Id1, accepter_id AS Id2 FROM request_accepted
    UNION
    SELECT accepter_id AS Id1, requester_id AS Id2 FROM request_accepted) t

GROUP BY t.Id1
ORDER BY COUNT(*) DESC
LIMIT 1


