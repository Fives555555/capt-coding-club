#!/bin/bash
#SBATCH --partition=shortq
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=2g
#SBATCH --time=00:10:00
echo "Hello from $(hostname)!"
echo "Current data and time: $(date)"
sleep 30
echo "Job completed!"
