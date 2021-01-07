Problem: https://www.hackerrank.com/challenges/the-company/problem



SQL: 
```
SELECT c.company_code, c.founder, 
       COUNT(DISTINCT l.lead_manager_code), COUNT(DISTINCT s.senior_manager_code),
       COUNT(DISTINCT m.manager_code), COUNT(DISTINCT e.employee_code)
FROM Company c, Lead_Manager l, Senior_Manager s, Manager m, Employee e
WHERE c.company_code = l.company_code AND 
      l.lead_manager_code = s.lead_manager_code AND
      s.senior_manager_code = m.senior_manager_code AND
      m.manager_code = e.manager_code
GROUP BY c.company_code, c.founder ORDER BY c.company_code;
```


```
Select company_code, founder, count(distinct lead_manager_code), count(distinct senior_manager_code), count(distinct manager_code),count(distinct employee_code) from (Select distinct T1.company_code, T1.founder, T2.lead_manager_code, T2.senior_manager_code, T2.manager_code, T2.employee_code from Company as T1
join Employee as T2
on T1.company_code=T2.company_code) as T
group by company_code, founder
order by company_code asc; 

```


```
Select T.company_code, founder, leadnum, seniornum, managernum, employeenum from
(Select Company_Code, count(distinct lead_manager_code) as leadnum, count(distinct senior_manager_code) as seniornum, count(distinct manager_code) as managernum, count(distinct employee_code) as employeenum
from Employee 
group by company_code) as T
join Company as C
on C.company_code=T.company_code
order by T.company_code asc; 




```
