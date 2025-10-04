

SELECT c.customer_state, COUNT(o.order_id) AS orders_count
FROM olist_customers_dataset c
JOIN olist_orders_dataset o ON c.customer_id = o.customer_id
GROUP BY c.customer_state
ORDER BY orders_count DESC;
