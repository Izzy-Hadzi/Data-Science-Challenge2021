# Data-Science-Challenge2021
Submission for the Shopify Data Science Challenge.

Question 1:

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

See Python file average_order_value.py for the code used to get these answers.

a.	Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 

The calculation is technically correct, however just by glancing at the data it is obvious that there are several outliers (704 000$ spent on 2000 shoes and store 78 also seems to sell shoes that do not quite fit the same price range as the other stores) that skew the data. To account for this, we need to consider the outliers as separate from the general data. Using interquartile range to remove outliers then recalculating the average, we get a new average of 293.71.

b.	What metric would you report for this dataset?

The metric I would report would be the mean of the interquartile range. Interquartile range describes the middle 50% of values when ordered from lowest to highest, and considering the higher outliers in this dataset, the mean of this range would provide a more realistic idea of the average order value.

c.	What is its value?

The value of the mean of the interquartile range on this dataset would be 227.0.


Question 2: Using the database found at https://www.w3schools.com/SQL/TRYSQL.ASP?FILENAME=TRYSQL_SELECT_ALL

a.	How many orders were shipped by Speedy Express in total?

	Query: 
	
	SELECT Count(o.OrderID) 
	FROM Shippers s, Orders o
	WHERE s.ShipperName = 'Speedy Express' AND s.ShipperID = o.ShipperID
	GROUP BY o.ShipperID;
	Answer:
	54

b.	What is the last name of the employee with the most orders?

	Query:
	
	SELECT e.LastName, t.TotalOrders
	FROM Employees e, (SELECT o.EmployeeID, count(o.OrderID) AS TotalOrders
			   FROM Orders o
			   GROUP BY o.employeeID) t 
	WHERE e.EmployeeID = t.EmployeeID AND t.TotalOrders = (SELECT MAX(TotalOrders)
				                  		FROM (SELECT o.EmployeeID, count(o.OrderID) AS TotalOrders
					                      		FROM Orders o
					                      		GROUP BY o.employeeID));
	Answer:
	Peacock

c.	What product was ordered the most by customers in Germany?

	Query:
	
	SELECT T3.TotalOrders, T3.ProductName
	FROM (SELECT COUNT(T.ProductID) AS TotalOrders, T.ProductName
		  FROM (SELECT P.ProductID, P.ProductName
			FROM Customers C, OrderDetails OD, Orders O, Products P
			WHERE C.Country = 'Germany' AND O.OrderID = OD.OrderID AND C.CustomerID = O.CustomerID AND OD.ProductID = P.ProductID) T
		  GROUP BY T.ProductName) AS T3
	WHERE T3.TotalOrders = (SELECT MAX(T2.TotalOrders) 
			FROM (SELECT COUNT(T.ProductID) AS TotalOrders, T.ProductName
	                            FROM (SELECT P.ProductID, P.ProductName
		                              	FROM Customers C, OrderDetails OD, Orders O, Products P
			                              WHERE C.Country = 'Germany' AND O.OrderID = OD.OrderID AND C.CustomerID = O.CustomerID AND OD.ProductID = P.ProductID) T
			                  GROUP BY T.ProductName) AS T2);
	Answer:
	Product Name: Gorgonzola Telino, ProductID: 31

