# import pandas as pd
# import os
# import matplotlib as plt
# project_dir = "/Users/Leon/Documents/ToiletProjectUni2021/Python/"
# filename = "Summary.csv"
#
# fname = os.path.join(project_dir,
#                      filename)
#
# scatterplot_table = pd.read_csv(fname)
# #
# # scatterplot_table
# #
# # ax1 = scatterplot_table.plot.scatter(x='Floor_Weight', y='Toilet_Weight',
# #                       c='DarkBlue')
# # ax1
#
import pandas as pd
import os
import matplotlib.pyplot as plt
pd.options.plotting.backend = "plotly"

project_dir = "/Users/Leon/Documents/ToiletProjectUni2021/Python/"
filename = "Summary.csv"

fname = os.path.join(project_dir,
                     filename)

scatterplot_table = pd.read_csv(fname)

scatterplot_table
scatterplot_table.Position.astype('category').cat.codes
scatterplot_table.Person.astype('category').cat.codes

# ax1 = scatterplot_table.plot.scatter(x='Floor_Weight', y='Toilet_Weight',
#                       c=scatterplot_table.Position.astype('category').cat.codes)
# ax1
scatterplot_table['combo'] = scatterplot_table['Person'] + scatterplot_table['Position']
scatterplot_table
plt.scatter(x=scatterplot_table.Floor_Weight,
           y=scatterplot_table.Toilet_Weight,
           c=scatterplot_table.combo.astype('category').cat.codes,
           s=20)
plt.title("Toilet_Scale (kg) vs Floor_Scale (kg)")
plt.xlabel("Floor_Scale (kg)")
plt.ylabel("Toilet_Scale (kg)")
plt.legend(loc="best")
plt.show()


