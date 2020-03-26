/*

	["employee_id", "employee_name", "manager_id", "employee_id", "employee_name", "manager_id", "employee_id", "employee_name", "manager_id"], "values": 
		[[1, "Boss", 1, 1, "Boss", 1, 1, "Boss", 1], 
		[2, "Bob", 1, 1, "Boss", 1, 1, "Boss", 1], 
		[77, "Robert", 1, 1, "Boss", 1, 1, "Boss", 1], 
		[4, "Daniel", 2, 2, "Bob", 1, 1, "Boss", 1], 
		[3, "Alice", 3, 3, "Alice", 3, 3, "Alice", 3], 
		[8, "John", 3, 3, "Alice", 3, 3, "Alice", 3], 
		[9, "Angela", 8, 8, "John", 3, 3, "Alice", 3], 
		[7, "Luis", 4, 4, "Daniel", 2, 2, "Bob", 1]]}

This indirection relationship, we can use join to find the combining effect

*/

SELECT
    e1.employee_id

From Employees e1
JOIN Employees e2
ON e1.manager_id = e2.employee_id
JOIN Employees e3
ON e2.manager_id = e3.employee_id
WHERE e3.manager_id = 1 AND e1.employee_id != 1




