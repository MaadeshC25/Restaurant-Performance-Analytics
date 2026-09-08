create database Restaurants;
USE Restaurants;

CREATE TABLE Hotel_Analysis (
    Restaurant_Name VARCHAR(100),
    Region VARCHAR(50),
    Revenue INT,
    Expenses INT,
    Net_Profit INT,
    Profit_Margin_Pct FLOAT,
    Famous_Dish VARCHAR(50),
    Rating FLOAT,
    Total_Customers INT,
    Top_Delivery_Partner VARCHAR(50)
);
select * from Hotel_Analysis