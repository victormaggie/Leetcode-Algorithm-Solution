SELECT 
    extra as report_reason,
    Count(DISTINCT post_id) as report_count

FROM Actions
WHERE action = "report" AND action_date = "2019-07-04"
GROUP BY extra

/*Group by return 1 row for each group*/