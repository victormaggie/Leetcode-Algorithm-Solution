SELECT e.employee_id,
/*Use a adjunction table to solve this question*/
    (SELECT COUNT(team_id)
    FROM Employee
    WHERE e.team_id = team_id) as team_size

from Employee e

