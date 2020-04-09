SELECT
    IFNULL(
        ROUND(
            COUNT(DISTINCT a.requester_id, a.accepter_id) / COUNT(DISTINCT r.sender_id, r.send_to_id)
            ,2)
        ,0) AS accept_rate

FROM friend_request r,
    request_accepted a 


/*solution 2: for the questions*/

SELECT 
    ROUND(
            IFNULL(
                (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM request_accepted) t) /
                (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM friend_request) r)
                ,0)
        ,2) AS accept_rate

