# Write your MySQL query statement below
SELECT tb1.name as Employee
FROM Employee as tb1
LEFT JOIN Employee as tb2
ON tb1.managerID = tb2.id
WHERE tb1.salary > tb2.salary;