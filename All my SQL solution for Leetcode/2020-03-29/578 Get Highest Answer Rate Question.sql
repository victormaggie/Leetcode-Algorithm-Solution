SELECT 
    question_id AS survey_log
FROM
    (
        SELECT question_id,
            AVG(action='answer') R
        FROM survey_log
        GROUP BY question_id
        ORDER BY R DESC
        LIMIT 1
    ) t

    /*
    Calculate the rate using 
    AVG(condition 1)
    COUNT() / COUNT()
    
    */