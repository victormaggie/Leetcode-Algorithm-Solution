-- rising temperature
SELECT
    w1.Id
FROM
    Weather w1,
    Weather w2
WHERE
    w1.RecordDate = AddDate(w2.RecordDate, 1) AND
    w1.Temperature > w2.Temperature
;