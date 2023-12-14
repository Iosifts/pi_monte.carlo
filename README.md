# Multiprocessing Pi Estimation

This Python script estimates the value of Pi using a multiprocessing approach. The method is based on the Monte Carlo simulation, where random points are generated inside a unit square and the number of points falling inside the unit circle is counted to approximate Pi.

## Features

- Utilizes all available CPU cores for parallel computation.
- Employs the Monte Carlo method for Pi estimation.

## Requirements

- Python 3.x
- multiprocessing module

## Usage

1. Set the variable `n` to the desired number of points for the simulation. The higher the number, the more accurate the estimation (e.g., `10**8`).
2. Run the script: `python pi_multiprocessing.py`

The script will output the estimated value of Pi based on the given number of points.

## How It Works

- The script divides the total number of points by the number of available CPU cores.
- Each core calculates the number of points within the unit circle for its portion of points.
- The results are aggregated and used to estimate Pi.

Note: The script prints the number of available CPUs for reference.

## Customization

- Change the value of `n` for a different number of points.
- Uncomment the lines setting the `pool` variable to limit the number of processes used.
