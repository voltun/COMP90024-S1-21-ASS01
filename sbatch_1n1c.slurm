#!/bin/bash

# Give the job a name
#SBATCH --job-name=twit1n1c

# How many CPU to run on
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

# Minimum acceptable walltime=hr:min:sec
#SBATCH -t 2-00:00:00

# Specify email to be notified of progress
#SBATCH --mail-user=chungw4@student.unimelb.edu.au
#SBATCH --mail-type=ALL

# Load environment variables for python
module purge

module load foss/2019b
module load python/3.7.4

echo "Running the script with 1 node 1 core\n"

echo "\nRunning with tinyTwitter.json"
time srun -n 1 python3 script_final.py "tinyTwitter.json"

echo "\nRunning with smallTwitter.json"
time srun -n 1 python3 script_final.py "smallTwitter.json"

echo "\nRunning with bigTwitter.json"
time srun -n 1 python3 script_final.py "bigTwitter.json"
