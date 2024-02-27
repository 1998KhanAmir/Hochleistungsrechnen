# SGE-Requests

#$ -M khuebner@physnet.uni-hamburg.de -m ea
#$ -o .
#$ -q graphix.q
#$ -cwd
#$ -pe smp 1
#$ -l h_vmem=20G
#$ -l gpu_gen=2080ti
#$ -l h_cpu=00:20:00
#$ -N "G2-A31"

#!/bin/sh

module purge
echo "Start von Task $SGE_TASK_ID"
module load python/3.9.2-infiniband
module load cuda/11.6.0
python3 a3_1_cupy_vs_numpy.py