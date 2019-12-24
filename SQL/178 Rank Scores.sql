-- 12-24-2019

SELECT
    Score,
    (SELECT count(distinct Score) FROM Scores WHERE Score >= s.Score) AS Rank
FROM Scores s 
ORDER BY Score DESC

-- 