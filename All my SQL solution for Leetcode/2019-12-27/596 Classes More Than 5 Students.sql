SELECT
    class
FROM
    courses
GROUP BY class
-- To review the student
HAVING COUNT(DISTINCT student) >= 5
;
