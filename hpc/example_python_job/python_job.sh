#!/bin/bash
#SBATCH --partition=shortq
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=4g
#SBATCH --time=00:10:00

# Load Python module
module load anaconda-uoneasy/2023.09-0

# Run the Python script
python analyse_data.py
