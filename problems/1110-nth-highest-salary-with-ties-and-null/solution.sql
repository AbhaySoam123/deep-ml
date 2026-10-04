-- your query
WITH BASE AS (
        Select Salary, dense_rank() OVER(order by salary desc) as rk
        from Employee
)

Select Salary from BASE WHERE rk = 3 limit 1