SELECT
    (CASE
        WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
        WHEN MOD(id, 2) != 0 AND counts = id THEN id
        ELSE id - 1
    END) AS id,
    student
FROM
    seat,
    (SELECT
        COUNT(*) AS counts
    FROM
        seat) AS seat_counts
ORDER BY id ASC;

-- More intuitive solutions

SELECT
    (CASE
        WHEN MOD(id, 2) = 0 THEN id -1
        WHEN MOD(id, 2) = 1 AND id != (SELECT MAX(id) FROM seat) THEN id + 1
        ELSE i
    END
    ) AS id, 
    student
FROM seat
ORDER BY id
;
