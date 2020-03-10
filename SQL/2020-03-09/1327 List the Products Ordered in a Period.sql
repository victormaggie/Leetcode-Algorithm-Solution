/*
The easy category sql questions
*/

/*The output file in this locations*/
# Write your MySQL query statement below

SELECT p.product_name,
        sum(o.unit) as unit

from Products p
join Orders o
on p.product_id = o.product_id
/* Extract the left string from the data*/
where Left(order_date, 7) = '2020-02'

/*Group the data from the new product table*/
group by p.product_name
having sum(o.unit) >= 100


