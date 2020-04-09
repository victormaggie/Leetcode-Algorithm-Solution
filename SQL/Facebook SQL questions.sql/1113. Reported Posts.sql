SELECT
    extra AS report_reason,
    /* post_id might be reported by different users, as such, we can do using DISTINCT*/
    COUNT(DISTINCT post_id) AS report_count
FROM
    Actions
WHERE Actions.action = 'report'
GROUP BY 1

