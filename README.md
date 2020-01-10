# Latin Hypercube Sampling

This script generates n unique sets of hyperparameters, which can be used to optimise trading algorithms during back testing.

## Using The Script

To run this script you should ensure you have a file named `param_ranges.json` in the same directory as the script, and then execute `python main.py 10`, where 10 is the number of parameter sets you wish to generate. The values will be written to an output file named param_sets.json.