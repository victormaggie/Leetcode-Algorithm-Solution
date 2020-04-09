SELECT
    DISTINCT L.page_id AS recommended_page
FROM
    (
        SELECT user1_id f1, user2_id f2 FROM Friendship
        UNION 
        SELECT user2_id f1, user1_id f2 FROM Friendship
    ) t
    JOIN Likes L
    ON L.user_id = t.f2
WHERE t.f1 = 1 AND page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1)

