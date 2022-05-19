# Write your MySQL query statement below
SELECT DISTINCT tb1.email as Email
FROM Person as tb1
INNER JOIN Person as tb2
ON tb1.email = tb2.email AND tb1.id != tb2.id;