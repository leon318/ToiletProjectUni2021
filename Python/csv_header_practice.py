'''
Practice CSV heading. Not important
'''
# import pandas as pd
# file-pd.read_csv('/Users/Leon/Documents/ToiletProjectUni2021/Exp5(Leon_toilet_test)/Exp5,T-2.csv')
# file.head()
import csv
import os
import pandas as pd
project_dir = "/Users/Leon/Documents/ToiletProjectUni2021/Exp5(Leon_toilet_test)"
filename = "Exp5,T-2.csv"
#
# df = pd.read_csv(os.path.join(project_dir, filename), header = None)
# print(df)
with open(os.path.join(project_dir, filename), 'w', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["Time", "Floorscale", "Toiletscale"])
