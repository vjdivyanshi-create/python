# PySpark DataFrame Sales Analysis Project

## Project Overview

Create a PySpark DataFrame application using the provided sales dataset. Read the CSV file into a DataFrame and perform the following operations: sort all products by sales in descending order and display the results, display the top 3 products with the highest sales values, and filter products with sales greater than 80,000 and save the output as a CSV file.

---

## Dataset

The dataset contains product information including product ID, product name, category, and sales amount.

### Sample Data

| Product ID | Product Name | Category    | Sales  |
| ---------- | ------------ | ----------- | ------ |
| 101        | Laptop       | Electronics | 150000 |
| 102        | Mobile       | Electronics | 95000  |
| 103        | TV           | Electronics | 120000 |
| 104        | Chair        | Furniture   | 30000  |
| 105        | Table        | Furniture   | 45000  |
| 106        | Sofa         | Furniture   | 80000  |
| 107        | Headphones   | Electronics | 25000  |
| 108        | Bed          | Furniture   | 90000  |


---

## Technologies Used

* Python 3.12
* Apache Spark (PySpark)
* Docker
* Java (JDK)

---

## Project Structure

```text
sales-dataframe-project/
│
├── app.py
├── sales.csv
├── requirements.txt
├── Dockerfile
├── README.md
└── output/
    └── high_sales_products/
```

---

## Build Docker Image

```bash
docker build -t sales-dataframe-app .
```

---

## Run Docker Container

```bash
docker run --name sales-container sales-dataframe-app
```

---

## Expected Output

### Top 3 Products by Sales

| Product Name | Sales  |
| ------------ | ------ |
| Laptop       | 150000 |
| TV           | 120000 |
| Mobile       | 95000  |

### Products with Sales Greater Than 80,000

| Product Name | Sales  |
| ------------ | ------ |
| Laptop       | 150000 |
| Mobile       | 95000  |
| TV           | 120000 |
| Bed          | 90000  |

---

## Output Files

The filtered products are saved in:

```text
output/high_sales_products/
```

The output directory contains:

```text
part-00000-xxxxx.csv
_SUCCESS
```

---

## Author

Divyanshi Vijay
