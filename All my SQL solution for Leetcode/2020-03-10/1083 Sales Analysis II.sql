SELECT b.buyer_id
FROM Product As a
JOIN Sales AS b
ON a.product_id = b.product_id
GROUP BY b.buyer_id
HAVING SUM(a.product_name = 's8') >0 and SUM(a.product_name = 'iphone') = 0;

