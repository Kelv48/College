#2 i)

INSERT INTO `EMPLOYEE`(`FNAME`, `LNAME`, `SSN`, `BDATE`, `ADDRESS`, `SALARY`)
VALUES ("John", "Smith", 12345678, "1965-01-09", "731 Western Road", 30000),
	   ("Franklin", "Wong", 33344555, "1955-12-08", "638 Eastern Road", 40000),
	   ("Alicia", "Zelaya", 99988777, "1968-07-19", "3321 Southern Castle", 25000),
       ("Jennifer", "Wallace", 98765432, "1941-06-20", "291 Berry Road", 43000),
       ("Ramesh", "Narayan", 66688444, "1962-09-15", "975 Fire Oak", 38000),
       ("Joyce", "English", 45345345, "1972-07-31", "5631 Rice Farm", 25000),
       ("Ahmad", "Jabbar", 98798798, "1969-03-29", "980 Eastern Gateway", 25000),
       ("James", "Borg", 88866555, "1937-11-10", "450 Good Stone", 55000);
       
INSERT INTO `WORKS_ON`(`ESSN`, `PNO`, `HOURS`)
VALUES (12345678, 1, 32.5),
	   (12345678, 2, 7.5),
       (66688444, 3, 40.0),
       (45345345, 1, 20.0),
	   (45345345, 2, 20.0),
	   (33344555, 2, 10.0),
	   (33344555, 3, 10.0),
	   (33344555, 10, 10.0),
	   (33344555, 20, 10.0),
	   (99988777, 30, 30.0),
	   (99988777, 10, 10.0),
	   (98798798, 10, 35.0),
	   (98798798, 30, 5.0),
	   (98765432, 30, 20.0),
	   (98765432, 20, 15.0),
	   (88866555, 20, 15.0);
       
INSERT INTO `PROJECT`(`PNAME`, `PNUMBER`)
VALUES ("ProductX", 1),
	   ("ProductY", 2),
	   ("ProductZ", 3),
	   ("Computerization", 10),
	   ("Reorganization", 20);

#2 ii)
select `HOURS` from `WORKS_ON`
WHERE ESSN = (SELECT SSN FROM EMPLOYEE
			  WHERE FNAME = "John" and LNAME = "Smith") and 
	  PNO = (SELECT PNUMBER FROM PROJECT
			 WHERE PNAME = "ProductX");
             
#2 iii)
SELECT sum(salary), avg(salary) from `EMPLOYEE`;

#2 iv)
SELECT sum(salary), avg(salary) from `EMPLOYEE` 
join `WORKS_ON` on ssn = WORKS_ON.essn
JOIN PROJECT on PROJECT.PNUMBER = WORKS_ON.PNO
WHERE PROJECT.PNAME = 'ProductX';






