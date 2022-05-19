# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person as tb1
LEFT JOIN Address as tb2
ON tb1.personID = tb2.personID;