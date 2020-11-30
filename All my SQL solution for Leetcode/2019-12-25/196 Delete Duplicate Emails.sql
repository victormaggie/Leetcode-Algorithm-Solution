-- 25-12-2019

SELECT p1
FROM 
    Person p1,
    Person p2

WHERE
    P1.Email = p2.Email
;

-- then we need to find a bigger id having same email address

DELETE 
    p1
FROM 
    -- alias
    Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id
;
