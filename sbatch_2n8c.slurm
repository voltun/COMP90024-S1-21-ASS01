#!/bin/bash

# Give the job a name
#SBATCH --job-name=twit2n8c

# How many CPU to run on
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4

# Minimum acceptable walltime=hr:min:sec
#SBATCH -t 2-00:00:00

# Specify email to be notified of progress
#SBATCH --mail-user=chungw4@student.unimelb.edu.au
#SBATCH --mail-type=ALL

# Load environment variables for python
module purge

module load foss/2019b
module load python/3.7.4

echo "Running the script with 2 node 8 core"

echo "Running with tinyTwitter.json"
time srun -n 8 python3 script_final.py "tinyTwitter.json"

echo "Running with smallTwitter.json"
time srun -n 8 python3 script_final.py "smallTwitter.json"

echo "Running with bigTwitter.json"
time srun -n 8 python3 script_final.py "bigTwitter.json"
