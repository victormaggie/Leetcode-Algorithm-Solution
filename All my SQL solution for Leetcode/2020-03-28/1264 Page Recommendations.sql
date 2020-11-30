SELECT 
    DISTINCT l.page_id AS recommended_page

FROM 
    (
    (SELECT user1_id, user2_id FROM Friendship WHERE user1_id = 1)
    UNION
    (SELECT user2_id AS user1_id, user1_id AS user2_id FROM Friendship WHERE user2_id = 1)
    ) t

    INNER JOIN
    Likes l 
    ON t.user2_id = l.user1_id
    WHERE l.page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1)

