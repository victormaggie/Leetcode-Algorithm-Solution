SELECT
    LEFT(trans_date, 7) AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(IF(state='approved', 1, 0)) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state='approved', amount, 0)) AS approved_total_amount
FROM Transaction t 
Group by country, LEFT(trans_date, 7)
ORDER BY LEFT(trans_date, 7), country

/*
Bear in mind 2 things:

1. filter using LEFT(...)
2. COUNT(*)  if we count the conditional number, we can use COUNT(IF(CONDITION, 1, 0))  --> 

*/