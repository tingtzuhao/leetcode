# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE p1
FROM Person as p1
LEFT JOIN Person as p2
ON p1.email = p2.email 
WHERE p1.email = p2.email AND p1.id > p2.id;