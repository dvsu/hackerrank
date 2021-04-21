SELECT 
    * 
FROM (
    SELECT 
        CITY, LENGTH(CITY) 
    FROM 
        STATION 
    ORDER BY 
        LENGTH(CITY) ASC, CITY ASC 
    LIMIT 1) 
AS 
    derivedTable1
UNION
SELECT 
    * 
FROM (
    SELECT 
        CITY, LENGTH(CITY) 
    FROM 
        STATION 
    ORDER BY 
        LENGTH(CITY) DESC, CITY ASC 
    LIMIT 1) 
AS 
    derivedTable2;