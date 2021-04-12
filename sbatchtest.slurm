#!/bin/bash

# Give the job a name
#SBATCH --job-name=tinytest

# How many CPU to run on
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

# Minimum acceptable walltime=hr:min:sec
#SBATCH -t 10:00:00

# Specify email to be notified of progress
#SBATCH --mail-user=chungw4@student.unimelb.edu.au
#SBATCH --mail-type=ALL

# Load environment variables for python
module purge
module load foss/2019b
module load python/3.7.4

# Command to run the job!
python3 main_1n1c.py
