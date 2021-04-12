#!/bin/bash

# Give the job a name
#SBATCH --job-name=big1n1c

# How many CPU to run on
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

# Minimum acceptable walltime=hr:min:sec
#SBATCH -t 1-12:00:00

# Specify email to be notified of progress
#SBATCH --mail-user=chungw4@student.unimelb.edu.au
#SBATCH --mail-type=ALL

# Load environment variables for python
module purge
module load gcc/8.3.0
module load openmpi/3.1.4
module load python/3.7.4

# Command to run the job!
python3 script.py "bigTwitter.json" 1 1
