/*Alias solution*/

SELECT
    Score,
    (
        SELECT COUNT(DISTINCT Score)
        FROM Scores
        WHERE Score >= s.Score
    )
FROM Scores s
ORDER BY Score DESC
;