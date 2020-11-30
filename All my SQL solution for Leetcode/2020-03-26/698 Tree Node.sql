SELECT DISTINCT a.id
    CASE
        WHEN a.id IS NULL THEN 'Root'
        when b.id IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END
    AS Type

FROM tree a 
LEFT JOIN tree b 
ON a.id = b_p_id
ORDER BY a.id

