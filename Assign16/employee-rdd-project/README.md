# Employee Salary Analysis using PySpark RDD

## Project Overview

This project uses PySpark RDDs to process employee salary data.

Operations performed:

1. Sort employees by salary in descending order.
2. Calculate department-wise salary totals.
3. Identify top three highest-paid employees.
4. Save top three employees to output files.

## Technologies Used

- Python 3.12
- Apache Spark (PySpark)
- Docker
- Java 17

## Dataset

employees.csv

## Build Docker Image

```bash
docker build -t employee-rdd .