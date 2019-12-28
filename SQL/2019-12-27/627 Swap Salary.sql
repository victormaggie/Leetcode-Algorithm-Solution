UPDATE salary
SET
    sex = CHAR(ASCII('f') ^ ASCII('m') ^ ASCII(sex));


-- Solution 2
-- We use the conditional CASE
UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END
;