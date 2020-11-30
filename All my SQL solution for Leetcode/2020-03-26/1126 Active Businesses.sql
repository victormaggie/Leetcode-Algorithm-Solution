/*
1. calculate the AVG occurences
2. Left join the table, WHERE occurence > AVG, GROUP BY business_id, COUNT(*) > 1
*/

SELECT
    e.business_id
FROM Events e 
LEFT JOIN 
    (
    SELECT
        event_type,
        AVG(occurences) AS num
    FROM
        Events
    GROUP BY event_type
    ) AS t

ON e.event_type = t.event_type
WHERE e.occurences > t.num
GROUP BY e.business_id
HAVING COUNT(*) > 1
;
