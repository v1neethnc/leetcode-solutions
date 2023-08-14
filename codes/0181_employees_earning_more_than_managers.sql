select e1.name as Employee
from Employee e1
where e1.salary > (select salary from Employee where id = e1.managerId)