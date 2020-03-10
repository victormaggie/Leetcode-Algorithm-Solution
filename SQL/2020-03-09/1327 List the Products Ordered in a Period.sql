/*
The easy category sql questions
*/

/*The output file in this locations*/
SELECT p.product_name,
        sum(o.unit) as unit
join Orders o
on p.product_id = o.product_id
where Left(order_date, 7) = '2020-02'
group by p.product_name
having sum(o.unit) >= 100


