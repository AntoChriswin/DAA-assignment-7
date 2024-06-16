SELECT customer_id
FROM (
    SELECT customer_id,
           EXTRACT(YEAR FROM order_date) AS year,
           SUM(price) AS total_purchases,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY EXTRACT(YEAR FROM order_date)) AS rn
    FROM Orders
    GROUP BY customer_id, EXTRACT(YEAR FROM order_date)
) AS subquery
WHERE rn = 1 OR total_purchases > LAG(total_purchases) OVER (PARTITION BY customer_id ORDER BY year)
GROUP BY customer_id
HAVING COUNT(*) = MAX(rn)
