SELECT country_name,

    (
        SELECT 
            CASE
                WHEN AVG(weather_state) <= 15 THEN "Cold"
                WHEN AVG(weather_state) >= 25 THEN "Hot"
                ELSE "Warm"
            END
    ) AS weather_type

FROM Countries e 
JOIN Weather w 
ON w.country_id = e.country_id
WHEN LEFT(day, 7) = "2019-11"
GROUP BY e.country_id

