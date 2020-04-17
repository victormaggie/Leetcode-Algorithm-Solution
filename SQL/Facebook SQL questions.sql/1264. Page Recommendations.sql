SELECT
    DISTINCT L.page_id AS recommended_page
FROM
    (
        /*be aware that the friend is in different table here*/
        SELECT user1_id f1, user2_id f2 FROM Friendship
        UNION 
        /*again*/
        SELECT user2_id f1, user1_id f2 FROM Friendship
    ) t
    /*use join get rid of the duplicate null*/
    JOIN Likes L
    ON L.user_id = t.f2
WHERE t.f1 = 1 AND page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1)

