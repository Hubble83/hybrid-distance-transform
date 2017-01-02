#!/bin/bash

module load gnu/4.9.0 gnu/openmpi_eth/1.8.4 cuda/7.0.28
cd ~/remoteDir/MPI-DT
python cluster.py
