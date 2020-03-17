SELECT E1.name
FROM
    Employee E1
INNER JOIN
    Employee E2
ON E1.Id = E2.ManagerId
GROUP BY E2.ManagerId
HAVING COUNT(E2.ManagerId) >= 5

