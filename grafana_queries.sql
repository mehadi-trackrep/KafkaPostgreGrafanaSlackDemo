-- 1)
SELECT
  timestamp as time,
  id
FROM test
where
  usd_rate_float > 63270
ORDER BY 1

-- 2)
SELECT
  timestamp as time,
  id
FROM test
where
  usd_rate_float > 63270
    OR
  eur_rate_float >= 59060
ORDER BY 1