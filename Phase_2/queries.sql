-- works
SELECT t_name
FROM truck, foodType
WHERE t_truckID = ft_truckID AND ft_name = "italian";

-- works
SELECT u_name 
FROM user
WHERE u_priority = "users";

-- works
SELECT * 
FROM foodtype;

-- works
SELECT u_name 
FROM user
WHERE u_priority = "admin";

-- works
SELECT v_name
FROM vendor;

-- works
SELECT t_name
FROM menu, truck
WHERE m_truckID = t_truckID
GROUP BY m_truckID
HAVING COUNT(m_food) = 1;


-- works
SELECT t_name
FROM menu, truck
WHERE m_truckID = t_truckID
GROUP BY m_truckID
HAVING COUNT(m_drinks) = 1;

-- works
SELECT * 
FROM user;

-- works
SELECT t_name
FROM menu, truck
WHERE m_truckID = t_truckID
GROUP BY m_truckID
HAVING COUNT(m_drinks) > 1;

--works
UPDATE menu
SET m_food = "chicken sandwhich"
WHERE m_menuID = 2

-- works
SELECT t_name
FROM truck
GROUP BY t_name
HAVING COUNT(t_truckID) > 3;

-- works
SELECT l_listID
FROM lists, user
WHERE l_userID = u_userID AND l_userID = 6;

-- works
SELECT *
FROM truck;



-- works
SELECT t_name
FROM menu, truck
WHERE m_truckID = t_truckID
GROUP BY m_truckID
HAVING COUNT(m_food) > 1;

-- works
SELECT * 
FROM supplier;

--works
SELECT t_name
FROM truck 
WHERE t_typeID IS NOT NULL;

--works
UPDATE menu
SET m_drinks = "water"
WHERE m_menuID = 2

--works
UPDATE truck
SET t_name = "CLOSED"
WHERE t_truckID = 1;

--works
UPDATE truck
SET t_name = "NONE", t_vendorID = 0, t_truckID = 0, t_typeID = 0 
WHERE t_vendorID = 4

--works
DELETE FROM truck
WHERE t_truckID = 4




