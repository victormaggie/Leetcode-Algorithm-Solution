-- 12-24-2019

SELECT
    Score,
    (
        SELECT COUNT(DISTINCT Score)
        FROM
            Scores
        WHERE
        -- use alias
            Score >= s.Score
    )
FROM Scores s 
ORDER BY Score DESC;

-- 