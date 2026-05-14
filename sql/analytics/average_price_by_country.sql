SELECT
    country,
    ROUND(AVG(price_eur_mwh)::numeric, 2) AS avg_price_eur_mwh
FROM energy_prices
GROUP BY country
ORDER BY avg_price_eur_mwh DESC;