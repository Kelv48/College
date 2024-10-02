SELECT *
FROM students;

SELECT first_name, last_name
FROM students;

SELECT first_name, last_name, points
FROM students
ORDER BY points;

SELECT first_name, last_name, date_of_birth
FROM students
ORDER BY date_of_birth DESC;

SELECT DISTINCT hometown
FROM students;

SELECT first_name, last_name
FROM students
WHERE points > 450;

SELECT first_name, last_name
FROM students
WHERE points = 525;

SELECT first_name, last_name
FROM students
WHERE points BETWEEN 400 and 500;

SELECT first_name, last_name
FROM students
WHERE hometown = 'Cork';

SELECT first_name, last_name
FROM students
WHERE date_of_birth <= '1994-01-01';

SELECT first_name, last_name
FROM students
WHERE date_of_birth > '1992-10-01';

SELECT first_name, last_name
FROM students
WHERE date_of_birth = '1994-12-25';

SELECT *
FROM students
WHERE first_name = "Ciara";

SELECT *
FROM students
WHERE first_name = "ciara";

SELECT *
FROM students
WHERE first_name = "Barry" or last_name = "Barry";

SELECT *
FROM students
WHERE last_name = "O'Kelly";

SELECT first_name, last_name
FROM students
WHERE date_of_birth BETWEEN '1994-01-01' and '1994-12-31';

SELECT first_name, last_name, hometown
FROM students
WHERE first_name = "Aoife" or first_name = "Ciara" or first_name = "Eimear";

SELECT *
FROM students
WHERE course = 'ck401' or course = 'ck402';

SELECT *
FROM students
WHERE hometown = "Cork" and points > 450;

SELECT *
FROM students
WHERE hometown != "Cork" and points > 450;

SELECT last_name
FROM students
WHERE last_name < "Cuddihy";

SELECT *
FROM students
WHERE last_name < "Callaghan" and first_name < "Harry";

SELECT *
FROM students
WHERE last_name like 'H%';





