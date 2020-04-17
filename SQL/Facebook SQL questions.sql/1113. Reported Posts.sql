SELECT
    extra AS report_reason,
    /* post_id might be reported by different users, as such, we can do using DISTINCT*/
    COUNT(DISTINCT post_id) AS report_count
FROM
    Actions
WHERE Actions.action = 'report' AND DATEDIFF('2019-07-05', action_date) = 1
GROUP BY 1

