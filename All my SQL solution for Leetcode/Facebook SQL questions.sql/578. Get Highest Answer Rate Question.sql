SELECT
    question_id AS survey_log
FROM
    survey_log s 
GROUP BY question_id
ORDER BY SUM(IF(answer_id IS NOT NULL, 1, 0)) / COUNT(*) DESC
LIMIT 1
