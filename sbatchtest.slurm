#!/bin/bash

# Give the job a name
#SBATCH --job-name=bigtest

# How many CPU to run on
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4

# Minimum acceptable walltime=hr:min:sec
#SBATCH -t 00:15:00

# Load environment variables for python
module purge

module load foss/2019b
module load python/3.7.4

# Command to run the job!
time srun -n 8 python3 script_test.py "tinyTwitter.json"
