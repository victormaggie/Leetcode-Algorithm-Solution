SELECT 
    a.follower,
    COUNT(DISTINCT b.follower) AS num

FROM
    follow a,
    follow b
WHERE a.follower = b.followee
GROUP BY b.followee
