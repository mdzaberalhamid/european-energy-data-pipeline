SELECT
    country,
    MIN(price_eur_mwh) AS min_price,
    MAX(price_eur_mwh) AS max_price,
    ROUND(AVG(price_eur_mwh)::numeric, 2) AS avg_price,
    ROUND(STDDEV(price_eur_mwh)::numeric, 2) AS volatility
FROM energy_prices
GROUP BY country
ORDER BY avg_price DESC;