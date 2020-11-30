SELECT
    a.stock_name,
    (b.sell - a.buy) AS capital_gain_loss

FROM
    (SELECT stock_name, SUM(price) as buy FROM Stocks WHERE operation='buy' GROUP BY stock_name) a
    JOIN
    (SELECT stock_name, SUM(price) as sell FROM Stocks WHERE operation='Sell' GROUP BY stock_name) b
    ON a.stock_name = b.stock_name

