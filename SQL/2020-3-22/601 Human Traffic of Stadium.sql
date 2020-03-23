SELECT DISTINCT t1.*

FROM stadium t1,
    stadium t2,
    stadium t3

WHERE
    t1.people >= 100 AND t2.people >= 100 AND t3.people >= 100

AND
    (
        (t1.id - t2.id = 1 AND t1.id - t3.id = 2)
    )

