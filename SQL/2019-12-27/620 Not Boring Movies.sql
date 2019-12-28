SELECT
    *
FROM
    cinema
WHERE
    cinema.id % 2 = 1 AND
    cinema.description != 'boring'
ORDER BY rating DESC;
