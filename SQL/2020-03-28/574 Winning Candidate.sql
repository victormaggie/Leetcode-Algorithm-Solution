SELECT 
    c.name
FROM Vote v 
LEFT JOIN Candidate c 
ON v.Candidate = c.id
GROUP BY v.CandidateId
ORDER BY COUNT(*) DESC
LIMIT 1

