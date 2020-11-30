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

-- The new version is wrong 
-- please remember that 

-- 1 ---1
-- 2 ---1
-- 3 ---1
-- 4 ---1

-- we need return DISTINCT 1, otherwise it will return TWO!

SELECT
    L1.Num AS 'ConsecutiveNums'
FROM
    Logs L1,
    Logs L2,
    Logs L3
WHERE
    L1.Num = L2.Num AND
    L2.Num = L3.Num AND
    L1.Id = L2.Id -1 AND
    L2.Id = L3.Id -1
;
    