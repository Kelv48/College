--1
SELECT actorid
FROM castings
WHERE movieid = 
(SELECT id
FROM movies
WHERE title = "Big Sleep, The");

--2
SELECT title, director, yr
FROM movies
WHERE director =
(SELECT director
FROM movies
WHERE title = "Citizen Kane");

--3
SELECT name
FROM actors 
JOIN castings
WHERE id = actorid and movieid =
(SELECT id
FROM movies
WHERE title = "Big Sleep, The");

--4
SELECT DISTINCT title
FROM movies
JOIN castings as c on id = c.movieid
WHERE yr >= "1950" and yr <= "1960"  or actorid =
(SELECT id
FROM actors
WHERE name = "Elizabeth Taylor");

--5
SELECT title, score
FROM movies
WHERE score =
(SELECT max(score)
FROM movies);

--6
SELECT cl.actorid
FROM castings AS cl 
GROUP BY cl.actorid
HAVING count(*) >= 10;

--7
SELECT name
FROM actors
WHERE id IN
(SELECT actorid
FROM castings 
GROUP BY actorid
HAVING count(*) >= 10)

--8
SELECT title
FROM movies
WHERE score >= 0.9 * 
(SELECT max(score)
FROM movies)

--9
SELECT c.actorid, a.name
FROM movies
JOIN castings AS c on id = c.movieid 
JOIN actors AS a on a.id = c.actorid
WHERE score < 3.0











