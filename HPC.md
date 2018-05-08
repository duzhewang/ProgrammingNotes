## Reference:
- https://www.stat.wisc.edu/reproducible#high

## HPC cluster

### Overview
- bash file(.sh file): commanf to execute job, SLURM

### Getting an account
- Send mail to lab@stat.wisc.edu to request access to the HPC submit nodes.
- Data must reside in the /workspace/[user] or /workspace2/[user] directory in order for the HPC cluster to read/write for your job.


### Getting started with SLURM
- https://www.stat.wisc.edu/services/hpc-cluster1/users-guide-getting-started

### SLURM commands
- sbatch: submit bash script to the scheduler.
```R
sbatch myScript.sh
```
- srun: run a job interactively (not scheduled)
```R
srun -pty/bin/bach [script or App]
```

- sinfo: displays current node usage for each partition of the cluster
```R
sinfo
```

- scancel: cancel specific job ID number
```
scancel 12345678
```
