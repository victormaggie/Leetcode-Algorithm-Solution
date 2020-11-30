SELECT
    t.sub_id AS post_id,
    COUNT(DISTINCT s.sub_id) AS number_of_comments

FROM
    (SELECT sub_id FROM Submissions WHERE parent_id IS NULL) t
    LEFT JOIN
    Submissions s
    ON t.sub_id = s.parent_id

GROUP BY 1
ORDER BY 1

