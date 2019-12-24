-- 12-24-2019

SELECT 
    FirstName,
    LastName,
    City,
    State
FROM Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId;