#!/bin/bash

# Give the job a name
#SBATCH --job-name=twitter1n8c

# How many nodes and cores to run on
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8

# Minimum acceptable walltime=hr:min:sec
#SBATCH -t 24:00:00

# Specify email to be notified of progress
#SBATCH --mail-user=chungw4@student.unimelb.edu.au
#SBATCH --mail-type=ALL

# Load environment variables for python
module purge
module load gcc/8.3.0
module load openmpi/3.1.4
module load python/3.7.4

# Command to run the job!
python3 main_1c1n.py
