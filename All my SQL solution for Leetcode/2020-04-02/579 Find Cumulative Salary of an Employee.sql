SELECT e.id, e.month
    SUM(e2.Salary) AS Salary

FROM Employee e
JOIN Employee e2
ON (e.Id = e2.Id AND e.Month >= e2.Month AND (e.Month - e2.Month <= 2))
WHERE e.Month < (SELECT MAX(Month) FROM Employee WHERE Id = e.Id)
GROUP BY e.Id, e.Month
ORDER BY e.Id, e.Month DESC

