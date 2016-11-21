# Write your MySQL query statement below

SELECT FirstName, LastName, City, State FROM Person

LEFT JOIN
(

SELECT * FROM Address 

) AS Address2

ON Person.PersonId = Address2.PersonId