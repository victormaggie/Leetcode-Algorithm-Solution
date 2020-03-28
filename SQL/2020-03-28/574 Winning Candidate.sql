SELECT 
    c.name
FROM Vote v 
LEFT JOIN Candidate c 
ON v.CandidateId = c.id
GROUP BY v.CandidateId
ORDER BY COUNT(*) DESC
LIMIT 1

