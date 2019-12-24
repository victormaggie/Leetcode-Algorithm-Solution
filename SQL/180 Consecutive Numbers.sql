-- 12-24-2019

-- write a sql query to find all numbers that appear at least three times

SELECT DISTINCT
    l1.Num AS ConsecutiveNums

FROM 
-- define 3 alias
    Logs l1,
    Logs l2,
    logs l3

WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND L2.Num = l3.Num
;