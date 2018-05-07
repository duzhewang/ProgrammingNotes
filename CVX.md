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
```
