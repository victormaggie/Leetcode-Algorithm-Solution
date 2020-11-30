SELECT L1.log_id AS START_ID, min(L2.log_id) AS END_ID
FROM
    (SELECT log_id FROM Logs WHERE log_id-1 NOT IN (SELECT log_id FROM Logs)) L1,
    (SELECT log_id FROM Logs WHERE log_id+1 NONT IN (SELECT log_id FROM Logs)) L2

WHERE L1.log_id <= L2.log_id
GROUP BY L1.log_id


/*

HOW TO CALCULATE THE SECUQUENTIAL DATA!!
*/