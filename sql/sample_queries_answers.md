## JSON Placeholder SQL
1. Find the top 5 users that post the longest posts (excl. the post title).

SELECT userId, SUM(LENGTH(body)) AS total_length
FROM GB_posts
GROUP BY userId
ORDER BY total_length DESC
LIMIT 5;

2. For each of these top 5 users, calculate their average post length (incl. the post title).

SELECT userId, AVG(LENGTH(title) + LENGTH(body)) AS average_length
FROM GB_posts
WHERE userId IN (
    SELECT userId
    FROM (
        SELECT userId
        FROM GB_posts
        GROUP BY userId
        ORDER BY SUM(LENGTH(body)) DESC
        LIMIT 5
    )
)
GROUP BY userId;


3. Identify the day of the week when the most `lengthy` posts are created (mock date using the `id` of posts as the day offset from the UNIX epoch).

SELECT
    STRFTIME('%w', DATETIME(id * 86400, 'unixepoch')) AS day_of_week,
    SUM(LENGTH(body)) AS total_length
FROM
    GB_posts
GROUP BY
    day_of_week
ORDER BY
    total_length DESC
LIMIT 1;



## Sales SQL
--Note :- Have used MSSQL database to load the data into the table. SQLlite is not friendly for data analysis
          Creating Table partitioning on SalesRecords table by OrderDate will improve the performance of the query execution.


1. Retrieve total sales revenue, number of units sold, and average price per unit for each item type for the first quarter of 2017.

SELECT ItemType,
       SUM(UnitsSold)	  AS TotalUnitsSold,
       SUM(TotalRevenue)  AS TotalRevenue,
       AVG(UnitPrice)     AS AveragePricePerUnit
FROM   SalesRecords
WHERE  OrderDate >= '2017-01-01' AND OrderDate < '2017-04-01'
GROUP BY ItemType;

2. Identify the top 3 item types by sales revenue for each region in the last quarter.

WITH LastQuarterSales AS (
SELECT
    Region,
    ItemType,
    SUM(TotalRevenue) AS TotalSalesRevenue,
    ROW_NUMBER() OVER (PARTITION BY Region ORDER BY SUM(TotalRevenue) DESC) AS Rank
FROM   SalesRecords
WHERE  OrderDate >= '2017-10-01' AND OrderDate < '2018-01-01'
GROUP BY Region, ItemType
)
SELECT  Region,
        ItemType,
        TotalSalesRevenue
FROM    LastQuarterSales
WHERE Rank <= 3;


3. Calculate the year-over-year growth in sales revenue for each item type.

WITH YearlySales AS (
  SELECT    ItemType, 
			YEAR(OrderDate) AS SalesYear, 
			SUM(TotalRevenue) AS TotalRevenue 
  FROM     SalesRecords
  GROUP BY  ItemType, 
            YEAR(OrderDate)
    ), 
YearlyGrowth AS (
  SELECT    a.ItemType, 
			a.SalesYear AS CurrentYear, 
			a.TotalRevenue AS CurrentRevenue, 
			b.SalesYear AS PreviousYear, 
			b.TotalRevenue AS PreviousRevenue, 
    ((a.TotalRevenue - b.TotalRevenue) / b.TotalRevenue
    ) * 100 AS RevenueGrowth 
  FROM  YearlySales a 
        LEFT JOIN YearlySales b ON a.ItemType = b.ItemType 
        AND a.SalesYear = b.SalesYear + 1
) 
SELECT   ItemType, 
         CurrentYear, 
         PreviousYear, 
		 CurrentRevenue, 
		 PreviousRevenue, 
		 RevenueGrowth 
FROM   YearlyGrowth 
ORDER BY   ItemType, 
           CurrentYear;
