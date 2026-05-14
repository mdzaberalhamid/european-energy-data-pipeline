SELECT
    timestamp,
    country,
    zone,
    price_eur_mwh
FROM energy_prices
ORDER BY price_eur_mwh DESC
LIMIT 10;