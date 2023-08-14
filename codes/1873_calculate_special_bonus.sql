select employee_id,
if(substring(name, 1, 1) = 'M' OR employee_id % 2 = 0, 0, salary) as bonus
from Employees
order by employee_id