import pandas as pd
import numpy as np
from itertools import cycle


df = pd.read_csv('input', sep="\n", names=['freq'])
freq = df['freq'].values

# Part 1
print('The frequency sum is:')
print(df["freq"].sum())


# Part 2
def find_first_repeated_freq(freq_mods):
    s = set()
    current_freq = 0
    for freq in cycle(freq_mods):
        if current_freq in s:
            return current_freq
        else:
            s.add(current_freq)
            current_freq += freq


print('\nThe first repeated freq is:')
print(find_first_repeated_freq(freq))
