-- SQL queries to set up schemas in BigQuery

/*
  Author : Ganesh Balaji 
  Date	 : 17-04-2024
  Note   : 1) Used MSSQL database for loading & building the Select statement as SQLlite is not friendly for data analysis
           2) Load the Sample data provided using the ETL pipelines
		   3) Query execution output attached to excel 

  Recommendation : Creating Table partitioning on SalesRecords table by OrderDate will further improve the performance of the query execution
           
*/

/*Table to load the Sales Record data*/
CREATE TABLE [dbo].[SalesRecords](
	[Region] [varchar](255) NULL,
	[Country] [varchar](255) NULL,
	[ItemType] [varchar](255) NULL,
	[SalesChannel] [varchar](255) NULL,
	[OrderPriority] [varchar](10) NULL,
	[OrderDate] [date] NULL,
	[OrderID] [int] NULL,
	[ShipDate] [date] NULL,
	[UnitsSold] [int] NULL,
	[UnitPrice] [decimal](18, 2) NULL,
	[UnitCost] [decimal](18, 2) NULL,
	[TotalRevenue] [decimal](18, 2) NULL,
	[TotalCost] [decimal](18, 2) NULL,
	[TotalProfit] [decimal](18, 2) NULL
) ON [PRIMARY]
GO

/*Indexes for supporting the query performance after analyzing the frequently used columns.*/
CREATE NONCLUSTERED INDEX [idx_order_date] ON [dbo].[SalesRecords]([OrderDate])
CREATE NONCLUSTERED INDEX [idx_item_type] ON [dbo].[SalesRecords]([ItemType])


