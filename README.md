# INST326-Team-Project

For Project 2
This project is basically a mini information-retrieval system built with Python classes.You are able to add documents, and the program automatically builds an inverted index behind the scenes, and then you can search up any term you want.
On top of that, it can generate reports so you can actually see what’s going on inside the index — top terms, document stats, and much more.

For Project 3 
This project builds off our earlier system by applying the advanced OOP concepts including inheritance, polymorphism, abstract classes, and composition. This system evaluates NBA player statistics entered by the user and generates a rating from:

Excellent-5, Good-4, OK-3, Bad-2, Terrible-1
The system supports Five NBA stat categories:

Points Per Game

Shooting Percentage

Blocks/Steals Per Game

Assists Per Game 

Rebounds Per Game

For Project 4
This Project is out final project that delivers a NBA Player Stat Analsis system fully build on Object-Oriented Programming (OOP) Principles. We leverage Template method design, and polymorphism to provide Position Specifc ratings for their statitics.
Also The application begings by ingesting player data from a CSV file In our case (nba_2024_stats.CSV). For Each Players

Points Per Game

Shooting Percentage

Blocks/Steals Per Game

Assists Per Game 

Rebounds Per Game

These all go into the classes such as for example PointGuardAssists OR CenterAssists

All these specialized classes inherit from a common Abstract Base Class (PlayerMetric) ensuring a good interface. This analysis is made by our Evaluator class which runs polymorphic methods.
