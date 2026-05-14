SELECT
    country,
    ROUND(STDDEV(price_eur_mwh)::numeric, 2) AS price_volatility
FROM energy_prices
GROUP BY country
ORDER BY price_volatility DESC;