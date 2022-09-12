select us.name as name, sum(tr.amount) as balance
from Transactions tr left join Users us on tr.account = us.account
group by tr.account
having balance > 10000