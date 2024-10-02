#3
SELECT * FROM `employees`;

#4
SELECT distinct dept FROM `department`;

#5
SELECT `salary`, `name` FROM `employees`
ORDER BY salary desc limit 5;

#6
SELECT avg(salary) FROM `employees`;

#7
SELECT avg(salary), `dept` FROM `employees`
GROUP BY dept;

#8
SELECT `name`, `building` 
FROM employees
JOIN department ON employees.id = department.id;

#9
SELECT avg(salary), `building` 
FROM employees
JOIN department ON employees.id = department.id
GROUP BY building;

#10
SELECT name, employees.dept, salary, department.dept, building
FROM employees
CROSS JOIN department;

