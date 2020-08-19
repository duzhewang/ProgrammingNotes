Problem: https://www.hackerrank.com/challenges/binary-search-tree-1/problem

Solution 1: ``SELECT N, 
CASE WHEN P IS NULL THEN 'Root' 
WHEN(SELECT COUNT(*) FROM BST WHERE P = A.N) > 0 THEN 'Inner'
ELSE 'Leaf'
END
FROM BST A 
ORDER BY N;
``

Question: ``what is A.N?``



Solution 2: 
``
select  case when P is null then concat(N, ' Root')
        when N in (select distinct p from bst) then concat(N, ' Inner')
        else concat(n, ' Leaf')
        end
from bst
order by n asc;
``




