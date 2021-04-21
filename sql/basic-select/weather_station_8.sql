SELECT 
    CITY 
FROM
    (SELECT DISTINCT 
        CITY 
    FROM 
        STATION
    WHERE 
        (CITY LIKE 'A%' OR
        CITY LIKE 'I%' OR
        CITY LIKE 'O%' OR
        CITY LIKE 'U%' OR
        CITY LIKE 'E%')) 
AS 
    subTable
WHERE
    (CITY LIKE '%a' OR
    CITY LIKE '%i' OR
    CITY LIKE '%u' OR
    CITY LIKE '%e' OR
    CITY LIKE '%o');