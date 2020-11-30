SELECT
    t1.follower,
    COUNT(DISTINCT t2.follower) AS num

FROM
    follow t1,
JOIN follow t2
ON t1.follower = t2.followee
