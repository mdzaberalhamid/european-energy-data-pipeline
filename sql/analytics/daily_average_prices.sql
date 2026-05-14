SELECT
    DATE(timestamp) AS date,
    country,
    ROUND(AVG(price_eur_mwh)::numeric, 2) AS avg_daily_price
FROM energy_prices
GROUP BY DATE(timestamp), country
ORDER BY date, country;