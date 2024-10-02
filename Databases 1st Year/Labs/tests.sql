--2018 autumn

--i)
-- SELECT title, score, yr
-- FROM movies
-- WHERE yr == 1975
-- ORDER BY score DESC;

-- --ii)
-- SELECT m.id, title
-- FROM movies as m
-- JOIN castings as c ON c.movieid = m.id
-- WHERE actorid =
-- (SELECT id
-- FROM actors
-- WHERE name == "John Wayne");

-- SELECT name, head_of_state
-- FROM countries
-- WHERE head_of_state == (SELECT head_of_state FROM countries
--     WHERE head_of_state == head_of_state 
--     GROUP BY head_of_state
--     HAVING count(head_of_state) >= 5 ) OR name ==
--     (SELECT name FROM countries
--     WHERE head_of_state == head_of_state 
--     GROUP BY head_of_state
--     HAVING count(head_of_state) >= 5 );

-- SELECT name, head_of_state
-- FROM countries
-- GROUP BY head_of_state
-- HAVING count(head_of_state) >= 5;

SELECT name, head_of_state
FROM countries
WHERE head_of_state IN (SELECT head_of_state FROM countries
    GROUP BY head_of_state
    HAVING count(head_of_state) >= 5 )
ORDER BY head_of_state;

-- SELECT DISTINCT name
-- FROM countries 
-- JOIN country_languages as cl ON cl.country_code = country_code
-- WHERE cl.language is "English";

SELECT cl.language, SUM(c.population * cl.percentage / 100) AS num_speakers
FROM country_languages AS cl
JOIN countries AS c ON cl.country_code = c.code
GROUP BY cl.language
HAVING num_speakers >= 20000000
ORDER BY num_speakers DESC;




