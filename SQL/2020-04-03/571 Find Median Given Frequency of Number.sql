SELECT 
    AVG(Number) AS median
FROM
    (SELECT * FROM Number ORDER BY Numbers) a 
    INNER JOIN
    (SELECT SUM(Frequency) AS total FROM Numbers) b,
    (SELECT @i := 0) t
WHERE @i + <= FLOOR((total+2)/2) AND (@i := (@i + Frequency)) >= FLOOR((total+1)/2)

