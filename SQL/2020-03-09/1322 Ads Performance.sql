SELECT ad_id, IFNULL(ROUND(AVG(CASE
                                WHEN action = "Clicked" THEN 1
                                WHEN action = "View"    THEN 0
                                ELSE NULL) * 100,2), 0) as ctr

FROM Ads
GROUP BY ad_id

/* Decrease by DESC order for ctr
    increase by ad_id order
*/

ORDER BY ctr DESC, ad_id

/*
 be aware of the IFNULL function and 
 AVG() function
DESC order in the ads
*/

