For each protein we have 1 or 2 experiments.
In each experiment we have selected 2 bed files, one with positive results taken from both replicates and one with all results taken from replicate 1.
From each experiment we will extract one dataset, positive values taken from the small bed file that only had positive results and negative values taken from the second file.
We choose the samples in each file via ranking using the 8th column (q-value), we take an equal amount of positive vs. negative results, from one file we take the best positive results and from the other we take the worst positive results.
For each file in the experiments we removed entries with a random chromosome (for some files there were no random entries so it stayed the same).
Lastly we shuffle the data and then preprocess.

The resources:

SRSF1
https://www.encodeproject.org/experiments/ENCSR432XUP/
ENCFF886XUO
ENCFF373NZF

https://www.encodeproject.org/experiments/ENCSR321PWZ/
ENCFF223KVR
ENCFF487OCT


PUM2
https://www.encodeproject.org/experiments/ENCSR661ICQ/
ENCFF880MWQ
ENCFF372VPV


QKI
https://www.encodeproject.org/experiments/ENCSR366YOG/
ENCFF786UOW
ENCFF190XSX

https://www.encodeproject.org/experiments/ENCSR570WLM/
ENCFF704OCI
ENCFF551IJQ


RBM5
https://www.encodeproject.org/experiments/ENCSR489ABS/
ENCFF927KRA
ENCFF176RGG


hnRNPL
https://www.encodeproject.org/experiments/ENCSR724RDN/
ENCFF266TKW
ENCFF073PCD

https://www.encodeproject.org/experiments/ENCSR795CAI/
ENCFF917CBK
ENCFF401YRZ