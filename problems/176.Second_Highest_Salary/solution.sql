//176	Second Highest Salary
CREATE TABLE Test (id int, Salary int);

INSERT INTO Test VALUES(1, 100)
INSERT INTO Test VALUES(2, 200)
INSERT INTO Test VALUES(3, 300)

SELECT max(Salary)
FROM Employee
WHERE Salary <> (
SELECT max(Salary)
FROM Employee)


/*
select (
  select distinct Salary from Employee order by Salary Desc limit 1 offset 1
)as second
*/