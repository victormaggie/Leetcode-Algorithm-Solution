
/*
    key points for this question
    1. join table based on two conditions Using LEFT JOIN ... OR ...
    2. ORDER BY will be executed at the end
    3. SUM ALL together + ... +
*/

SELECT 
    team_id, team_name,
    SUM(CASE WHEN team_id = host_team AND host_goals > guest_goals THEN 3 ELSE 0 END) +
    SUM(CASE WHEN team_id = guest_team AND guest_goals > host_goals THEN 3 ELSE 0 END) +
    SUM(CASE WHEN team_id = host_team AND host_goals = guest_goals THEN 1 ELSE 0 END) +
    SUM(CASE WHEN team_id = guest_team AND host_goals = guest_goals THEN 1 ELSE 0 END)
    AS num_points
FROM Teams
LEFT JOIN Matches
ON team_id = host_team OR team_id = guest_team
GROUP BY team_id
ORDER BY num_points DESC, team_id ASC