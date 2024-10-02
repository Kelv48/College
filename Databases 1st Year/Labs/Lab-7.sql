--1
SELECT *
FROM hotels
WHERE city = "Cork";

--2
SELECT * 
FROM guests
WHERE guest_address LIKE "%Limerick%";

--3
SELECT *
FROM rooms
WHERE room_type = "double" AND price < 70
ORDER BY price;

--4
SELECT *
FROM bookings
WHERE dep_date = " ";

--5
SELECT count(hotel_name)
FROM hotels;

--7
SELECT h.hotel_name, r.room_num, r.price
FROM hotels as h
JOIN rooms as r on h.hotel_num = r.hotel_num
WHERE price < 70 and
(
SELECT room_num
FROM rooms
WHERE price < 70);

--8
SELECT h.hotel_name, r.room_type, price, r.room_num
FROM hotels as h
JOIN rooms as r on h.hotel_num = r.hotel_num
WHERE room_type = "double" and price < 70;

--9
SELECT avg(price)
FROM rooms;

--10
SELECT avg(price)
FROM rooms as r
JOIN hotels as h on h.hotel_num = r.hotel_num
WHERE h.city = "Cork";

--11
SELECT avg(price)
FROM rooms as r
JOIN hotels as h on h.hotel_num = r.hotel_num
WHERE h.city = "Cork" and r.room_type = "double";

--12
SELECT count(h.hotel_name)
FROM hotels as h
JOIN bookings as b on b.hotel_num = h.hotel_num
WHERE arr_date > '2002-10-31' AND arr_date < '2002-12-01';

--13
SELECT r.price, r.room_type
FROM rooms as r
JOIN hotels as h on r.hotel_num = h.hotel_num
WHERE hotel_name = "Hotel Splendide";

--14
SELECT hotel_name, count(room_num)
FROM hotels as h
JOIN rooms as r on r.hotel_num = h.hotel_num
WHERE city = "Galway";

--15
SELECT guest_num
FROM bookings as b
JOIN hotels as h on h.hotel_num = b.hotel_num
Where hotel_name ="Hotel Splendide" AND 
(SELECT arr_date
FROM bookings
WHERE arr_date > 2002-01-01 AND arr_date < 2002-02-01);

--16





