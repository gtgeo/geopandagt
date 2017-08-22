import pybktree
import pandas as pd
import time
import geopandas
from shapely.geometry import Point

t1 = time.time()

df = pd.read_csv("/home/bigdata/Downloads/Data/miniNSPL.csv")
tree = pybktree.BKTree(pybktree.hamming_distance, [0, 4, 5, 14,65,4,76,4,35,63,23])
print sorted(tree)

print df
t2 = time.time()
print t2 -t1