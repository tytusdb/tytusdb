select * from tbsujeto S 
inner join tbsujetoide SI on S.

create function promedio
Begin
	Declare @promedio as double
	Select @promedio = sum(ventas)/count(*) from tbventas where fecha='2020-12-04';
	return @promedio
End


create function agregadia(@dias int, @fecha as datatime) as datetime
Begin
	declare @fechafinal as datetime
	set @datetime = dateadd(dd,@dias,@fecha)
	return @datetime
End


Select Case When idestado=1 then 'Activo' else 'Inactivo' END
From tbsujeto


Select
	case when idestado = 1
	then 'Activo' else 'Inactivo'
	END
From tbsujeto;


Select * From tbcliente where id_cliente=45180;


SELECT Abs(5) AS AbsNum;
select x, cbrt(x) from tab;
SELECT CEIL(26);

SELECT LENGTH("SQL Tutorial") AS LengthOfString;
SELECT SUBSTRING('SQL Tutorial', 1, 3) AS ExtractString;
SELECT TRIM('     SQL Tutorial!     ') AS TrimmedString;
select get_byte('Th\\000omas', 4);
SELECT MD5('PostgreSQL MD5');

--expresions

SELECT OrderID, Quantity,
CASE WHEN Quantity > 30 THEN 'The quantity is greater than 30'
WHEN Quantity = 30 THEN 'The quantity is 30'
ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;

SELECT GREATEST(3, 12, 34, 8, 25);
SELECT LEAST(3, 12, 34, 8, 25);

--limit and offset

SELECT * FROM Orders LIMIT 10 OFFSET 15;
SELECT * FROM Orders LIMIT 15, 10;

SELECT * FROM tabla 
ORDER BY nivel ASC;


SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;

SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City asc;

SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM (Orders
INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID)
GROUP BY LastName
HAVING COUNT(Orders.OrderID) > 10;

SELECT * FROM Customers
WHERE ContactName LIKE 'a%o';

SELECT * FROM Customers
WHERE CustomerName NOT LIKE 'a%';