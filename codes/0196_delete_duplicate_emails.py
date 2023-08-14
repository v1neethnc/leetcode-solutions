delete b from Person a inner JOIN Person b
on a.email = b.email where a.id < b.id