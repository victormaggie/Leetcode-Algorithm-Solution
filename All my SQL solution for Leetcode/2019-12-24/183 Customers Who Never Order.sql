-- 24-12-2019

SELECT
    Name as Customers
FROM Customers c 
LEFT JOIN orders o 
ON c.ID = o.CustomerId
WHERE o.CustomerId IS NULL;

