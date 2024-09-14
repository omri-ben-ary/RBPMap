Line 2000 first character was changed from N to T because it was the only instance of N out of roughly 30,000 sequences
sampled (including all other datasets). I tried rerunning BED2FASTA tool a few times to see if it would generate a different result but it stayed the same.
I also tried to make a larger window (200 chars to the right instead of 100) to see whether it was an edge case but got
same result. It seemed unreasonable to add another option in the one hot encoding just for 1 sample out of thousands and
so I decided to change it to T because the 2 chars to the right were T. I also decided it to be uppercase T because
it looks like an exon region based on it's neighbors. 