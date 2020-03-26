/*
    1. get the cumulative sum weigt using Join with condition  q1.turn >= q2.turn and Group by q1.turn
    2. CHECK CHECK

*/


SELECT q1.person_name
FROM Queue q1
INNER JOIN Queue q2
ON q1.turn >= q2.turn
GROUP BY q1.turn
/* Here use q2 as the weight calculation*/
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1


/*Less join solution*/ --> find the previous number, using q1.turn >= q2.turn

SELECT 
    q1.person_name
FROM 
    Queue q1, 
    Queue q2
WHERE 
    q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1


/*variable*/

SELECT
    person_name
FROM
    (SELECT
        q.person_name,
        @cum_weight:= @cum_weight + q.weight cum_weight
        FROM
        Queue q JOIN (SELECT @cum_weight:= 0) t1
    ORDER BY
        q.turn) t2
WHERE
    cum_weight <= 1000
ORDER BY
    cum_weight DESC
LIMIT 1;


/* Two way to calculate the cumulative sum

1. use the two table inner join 
2. choice from two table 
3. use the function @cum_weight := @cum_weight + q.weight cum_weight

*/