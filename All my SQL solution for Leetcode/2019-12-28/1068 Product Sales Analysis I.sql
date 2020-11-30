SELECT
    product_name,
    year,
    price
FROM Sales 
LEFT JOIN product
ON Sales.porduct_id = Product.porduct_id
;