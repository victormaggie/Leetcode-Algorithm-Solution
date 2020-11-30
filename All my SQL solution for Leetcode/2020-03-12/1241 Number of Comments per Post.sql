SELECT
    post_id,
    COUNT(DISTINCT post_id, sub_id) AS number_of_comments
FROM
(
    SELECT  
        DISTINCT sub_id as post_id
    FROM
        submissions
    WHERE
        parent_id is NULL
) t1

LEFT JOIN Submissions s 
ON t1.post_id = s.parent_id
GROUP BY post_id
