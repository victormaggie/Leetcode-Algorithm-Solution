SELECT
    IFNULL(
        ROUND(
            (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM reques_accepted) AS A)
            /
            (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM friend_request) AS B)
            ,2
        )
        ,0
    )

/*use less syntax method*/

SELECT  IFNULL(ROUND(COUNT(DISTINCT (r.sender_id, r.send_to_id)) / COUNT(DISTINCT (a.requester_id, a.accepter_id)), 2) , 0)
FROM 
    friend_request r
    , request_accepted a
