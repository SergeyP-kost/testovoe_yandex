SELECT
    Countries.name,
    count(Companies.id)
FROM
    Countries
    JOIN Cities
    JOIN Companies
    ON
        Companies.city_id = Cities.id
        AND Companies.labors > 1000
        AND Cities.country_id = Countries.id
GROUP BY
    Countries.name
ORDER BY
    Companies.id