SELECT
    ad_id,
    ROUND(
        IFNULL(
                AVG(
                    CASE
                        WHEN action = 'Clicked' THEN 1
                        WHEN action = 'Viewed' THEN 0
                        ELSE NULL
                )
        ,0)
    ,2) AS ctr

FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id


/*Solution 2 for the calculation*/

SELECT 
    ad_id,
    ROUND(
        IFNULL(
            SUM(IF(action = 'Clicked', 1, 0)) / SUM(IF(action = 'Clicked', 1, 0)) + SUM(IF(action = 'Viewed', 1, 0))
            ,0)
        ,2) AS ctr

FROM Ads
GROUP BY ad_id 
ORDER BY ctr DESC, ad_id

