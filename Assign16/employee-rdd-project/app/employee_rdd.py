from pyspark import SparkContext

# Initialize Spark Context
sc = SparkContext("local[*]", "EmployeeRDDProject")

data = sc.textFile("data/employees.csv")

header = data.first()
rows = data.filter(lambda x: x != header)

# structured format
employees = rows.map(lambda x: x.split(","))

# 1. Sort employees by salary (descending)

sorted_employees = employees.sortBy(
    lambda x: int(x[3]),
    ascending=False
)

print("\n===== Employees Sorted By Salary =====")

for emp in sorted_employees.collect():
    print(emp)

# 2. Department-wise Salary Total

dept_salary = employees.map(
    lambda x: (x[2], int(x[3]))
)

dept_totals = dept_salary.reduceByKey(
    lambda a, b: a + b
)

print("\n===== Department Salary Totals =====")

for dept in dept_totals.collect():
    print(dept)

# 3. Top 3 Highest Paid Employees

top3 = sorted_employees.take(3)

top3_rdd = sc.parallelize(
    [
        f"{emp[0]},{emp[1]},{emp[2]},{emp[3]}"
        for emp in top3
    ],
    1
)

import shutil
import os

output_path = "output/top3_employees"

if os.path.exists(output_path):
    shutil.rmtree(output_path)

top3_rdd.saveAsTextFile(output_path)

print("\nTop 3 employees saved successfully.")

sc.stop()