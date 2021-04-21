SELECT 
    Name 
FROM 
    STUDENTS
WHERE
    Marks > 75
ORDER BY
    SUBSTRING(Name, LENGTH(Name)-2, 3), ID;