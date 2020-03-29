SELECT name AS results
FROM
    (
        SELECT user_id, name,
            count(rating) rating_num
        FROM 
            Movie_Rating
        LEFT JOIN
            Users using(user_id)
        GROUP BY user_id, name
        ORDER BY rating_num DESC, name ASC
        LIMIT 1
    ) a 

UNION
SELECT title AS results
    (
        SELECT movie_id, title,
            AVG(rating) avg_rating
        FROM
            Movie_Rating
        LEFT JOIN
            Movies using(movie_id)
        WHERE
        /*The time selection for this query*/
            created_at LIKE '2020-02-%'
        GROUP by movie_id, title
        ORDER BY avg_rating DESC, title ASC 
        LIMIT 1
    ) b
;