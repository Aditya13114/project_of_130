import pandas as pd
import csv

df = pd.read_csv("C130csv.csv")

del df["hyperlink"]
del df["st_masserr1"]
del df["st_raderr1"]

df.to_csv('project.csv') 