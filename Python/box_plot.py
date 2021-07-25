# import numpy as np
# import matplotlib.pyplot as plt
# from Python.machine_learning_prep_functions.feature_position_tuple_list_generator import tuple_list_generator
# from Python.machine_learning_prep_functions.array2d_generator import array_2d_generator
# from Python.machine_learning_prep_functions.array_randomizer import array_randomizer_and_tupple_generator
#
# final_list, input_integer, encoded, position_and_person = tuple_list_generator()
#
# feature_matrix, position_matrix = array_2d_generator(final_list)
#
# # character_matrix = np.concatenate((encoded,position_matrix),axis=1)
# # print(character_matrix)
#
# num_rows1, num_cols1 = feature_matrix.shape
# # print(feature_matrix)
# print(num_cols1)
# feature_list = (np.split(feature_matrix, 12, axis=1))
# feature_list
# print(len(feature_list))
# feature_list2 = []
# feature_list3 = []
# for i, x in enumerate(feature_list):
#     feature_list2.append(np.concatenate((feature_list[i]), axis=None))
# for i, x in enumerate(feature_list2):
#     feature_list3.append(feature_list2[i] / np.mean(feature_list2[i]))
#
# feature_names = ['Max ttl', 'Max flr ', 'max tlt ', 'Time max ttl',
#                  'T- max flr ', 'T- max tlt', 'stable ttl', 'stable flr',
#                  'stable tlt  ', 'T- stable ttl  ',
#                  'T- stable flr',
#                  'T- stable tlt  ']
# my_dict = {}
#
# for f, b in zip(feature_names, feature_list3):
#     my_dict[f] = b
# # my_dict
# fig, ax = plt.subplots()
# ax.boxplot(my_dict.values())
# ax.set_xticklabels(my_dict.keys())
# plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from Python.machine_learning_prep_functions.feature_position_tuple_list_generator import tuple_list_generator
from Python.machine_learning_prep_functions.array2d_generator import array_2d_generator
from Python.machine_learning_prep_functions.array_randomizer import array_randomizer_and_tupple_generator

final_list, input_integer, encoded, position_and_person = tuple_list_generator()

feature_matrix, position_matrix = array_2d_generator(final_list)

# character_matrix = np.concatenate((encoded,position_matrix),axis=1)
# print(character_matrix)

num_rows1, num_cols1 = feature_matrix.shape
# print(feature_matrix)
print(num_cols1)
feature_list = (np.split(feature_matrix, 12, axis=1))
feature_list
print(len(feature_list))
feature_list2 = []
feature_list3 = []
for i, x in enumerate(feature_list):
    feature_list2.append(np.concatenate((feature_list[i]), axis=None))
for i, x in enumerate(feature_list2):
    feature_list3.append(feature_list2[i] / np.mean(feature_list2[i]))

feature_names = ['Max ttl', 'Max flr ', 'max tlt ', 'Time max ttl',
                 'T- max flr ', 'T- max tlt', 'stable ttl', 'stable flr',
                 'stable tlt  ', 'T- stable ttl  ',
                 'T- stable flr',
                 'T- stable tlt  ']
my_dict = {}

for f, b in zip(feature_names, feature_list3):
    my_dict[f] = b

sns.set(style="whitegrid")

ax = sns.boxplot(data=feature_list3, showfliers = False)
ax.set_xticks(range(12))
ax = sns.swarmplot(data=feature_list3, color="0", size = 1)
value_list = [x for x in range(0,12)]
value_list
plt.xticks(value_list, ['max total', 'max floor ', 'max toilet ', 'Time max total', 'T- max floor ', 'T- max toilet', 'stable total', 'stable floor',
                 'stable toilet  ', 'T- stable total',
                 'T- stable floor',
                 'T- stable toilet'], rotation=45)
plt.title("Variance of Individual Features")
# Set x-axis label
plt.xlabel('Features')
axes = plt.gca()
axes.set_ylim([0,4])
# Set y-axis label
plt.ylabel('Values Normalized to the Mean')
plt.show()