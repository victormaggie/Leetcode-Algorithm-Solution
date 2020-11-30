/*
table name: friending
+-----------------+-------------+------------------------------------------+
|  column         |  data_type  |  description                             |
+-----------------+-------------+------------------------------------------+
|  sender_id      |  BIGINT     |  Facebook Id for user sending request    |
|  receiver_id    |  BIGINT     |  Facebook Id for user receiving request  |
|  sent_date      |  STRING     |  Date when request was sent              |
|  accepted_date  |  STRING     |  Date when request was accepted          |
|                                        (NULL if not accepted)            |
|  sender_country |  STRING     |  Facebook Identifier                     |
+---------------+---------------+------------------------------------------+
sender_id | receiver_id | sent_date    | accepted_date | sender_country
1         | 2           | 2019-09-15   | 2019-09-18    | US
1         | 3           | 2019-10-15   | 2019-10-15    | US
2         | 3           | 2019-10-15   | NULL          | CA
*/

/* What was the accept rate by country for requests sent in the past week? */


SELECT country,
    SUM(IF(accepted_date IS NOT NULL, 1, 0)) / COUNT(sender_id) AS accept_rate

FROM friending
WHERE DATEDIFF(CURDATE(), send_date) <= 7
GROUP BY country 


/*
table_name: fraud 
+---------------+---------------+----------------------------+
|  column       |  data_type    |  description               |
+---------------+---------------+----------------------------+
|  userid      |  BIGINT        |  Facebook ID for user      |
|  fraud_type  |  STRING        |  'spam', 'phishing'        |
+---------------+---------------+----------------------------+
SAMPLE ROWS:
| userid | fraud_type |
| 1234   | 'spam'     |
| 5678   | 'phishing' |
| 9010   | 'spam'     |
| 1112   | 'spam'     |
*/

/* What is the percentage of friend requests that come from non-fraud users in the past week? */

SELECT 
    ROUND(
    (SELECT COUNT(sender_id) FROM friending 
    WHERE sender_id  NOT IN (SELECT user_id AS sender_id FROM Fraud)) / COUNT(f.sender_id),2
    )AS percentage

FROM friending f

