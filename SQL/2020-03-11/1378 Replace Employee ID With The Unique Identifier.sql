SELECT 
    unid.unique_id,
    eid.name
FROM Employees eid

LEFT JOIN
    EmployeeUNI unid
ON unid.id = eid.id
ORDER BY unid.unique_id

