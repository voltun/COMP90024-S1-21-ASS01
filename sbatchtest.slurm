#!/bin/bash

# Give the job a name
#SBATCH --job-name=tinytest

# How many CPU to run on
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4

# Minimum acceptable walltime=hr:min:sec
#SBATCH -t 0:15:00

# Specify email to be notified of progress
#SBATCH --mail-user=chungw4@student.unimelb.edu.au
#SBATCH --mail-type=ALL

# Load environment variables for python
module purge

module load foss/2019b
module load python/3.7.4

# Command to run the job!
time srun -n 4 python3 script_test.py "tinyTwitter.json"
