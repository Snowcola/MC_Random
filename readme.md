[![Build Status](https://travis-ci.org/Snowcola/MC_Random.svg?branch=master)](https://travis-ci.org/Snowcola/MC_Random) [![codecov](https://codecov.io/gh/Snowcola/MC_Random/branch/master/graph/badge.svg)](https://codecov.io/gh/Snowcola/MC_Random) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT )  
# MC_Random.py

A python 3.6 implementation of the Measurement Canada [S-S-01—Specifications for random sampling and randomization](https://strategis.ic.gc.ca/eic/site/mc-mc.nsf/eng/lm00180.html)

## Installation


## Usage
`RandomSample()` takes the following arguments
```python
lotsize: int
sample_size: int
data: datetime
seed: int
single: bool
```
### Example code
```python
from MC_Random import RandomSample
from datetime import dateime

date = datetime(2018-11-26)
sample = RandomSample(lot_size=3000, sample_size=80, single=True)

print(sample.samples)
print(f"seed 1: {sample.s_e}")
print(f"seed 2: {sample.seed}")
```
### Output
```
[sample1, sample2]
seed 1: 596505600
seed 2: 1016303
```

Where `sample1` and `sample2` are lists of sample items. In the case of this example `sample1` would be a list of 80 numbers and `sample2` would be an empty list

## Defaults
date = current date using  `datetime.utcnow()`  
lot_size = 3000  
sample_size = 80  
single = True  

## Available Data

`RandomSample.s_e`: seed 1 or seconds from 2000-01-01 00:00:00 to datetime specified  
`RandomSample.seed`: automatically generated seed or the seed provided
`RandomSample.samples`: always returns a list of lists `[sample1, sample2]` samples are scaled to the `lost_size`  
`RandomSample.stat_sample`: returns unscaled samples selected  
`RandomSample.start_array`: returns the original shuffling array  
`RandomeSample.mode`: returns 1 for single sample or 2 for double


