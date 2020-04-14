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

/* why this does not work ??*/

SELECT
    Score,
    Rank
FROM
    (
    SELECT
        Score,
        IF(Score = @score, @rank := @rank, @rank := @rank + 1) AS Rank,
        @score := Score

    FROM
        (SELECT @rank := 0, @score := 0) t,
        Scores
    ORDER BY Score DESC
    ) t
