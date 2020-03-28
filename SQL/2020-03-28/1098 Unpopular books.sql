/* Multiple condition filter for each table*/

SELECT 
    b.book_id,
    b.name
FROM
    (SELECT * FROM Books WHERE available_from < '2019-05-23') b
    LEFT JOIN
    (SELECT * FROM Orders WHERE dispatch_date > '2018-06-23') o 
ON b.book_id = o.book_id 
GROUP BY b.book_id, b.name
HAVING SUM(o.quantity) IS NULL OR SUM(o.quantity) < 10

