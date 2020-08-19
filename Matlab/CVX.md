## CVX installation

```matlab
cd ~/path of the cvx folder
cvx_setup
```
## Solvers included with CVX
- SeDuMi: optimization over symmetric cones. 
- SDPT3: semidefinite-quadratic-linear programming

## Return values
- x: solution variable
- cvx_optval: the optimal value
- cvx_status: solver status( solved, unbounded, infeasible,...)

## Examples-LP
```matlab
maximize c^Tx
subject to Ax=b
           x>=0
```
```matlab
cvx_begin
   variables x(n)
   maximize(c'*x)
   subject to
      A*x==b
      x>=0
cvx_end
```










