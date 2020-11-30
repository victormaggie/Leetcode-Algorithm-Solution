SELECT 
    cu.name
FROM customer cu
WHERE cu.referee_id <> 2 OR cu.referee_id is NULL


SELECT 
    name
FROM customer
WHERE referee_id <> 2 or referee_id is NULL
