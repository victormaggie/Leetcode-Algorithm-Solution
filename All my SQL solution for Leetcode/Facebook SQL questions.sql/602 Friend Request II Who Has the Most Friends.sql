
SELECT 
    fid 1 AS id,
    COUNT(*) AS num

FROM
    (SELECT requester_id AS fid1, accepter_id AS fid2 FROM request_accepted
    UNION
    SELECT accepter_id AS fid1, requester_id AS fid2 FROM request_accepted
    ) t
GROUP BY t.fid1

/*This is for the calculation of the maximum one*/
ORDER BY COUNT(*) DESC
LIMIT 1


