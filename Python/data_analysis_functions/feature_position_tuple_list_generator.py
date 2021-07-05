def tuple_list_generator():
    import glob
    import numpy as np
    import matplotlib.pyplot as plt
    import os
    from Python.data_analysis_functions.user_input_function import user_input_and_directory_generator
    from Python.processing_functions.unpacking_data import unpack_and_append_data3
    from Python.processing_functions.theshold_locator_and_trimmers import threshold_locater_and_posterior_trimmer3
    from Python.processing_functions.find_shortest_length import find_shortest_length
    from Python.processing_functions.theshold_locator_and_trimmers import anterior_trimmer_x_and_y_and_z
    from Python.processing_functions.math import total_and_averager_y_and_z
    from Python.processing_functions.math import std_calculator_y_and_z
    from Python.processing_functions.Plotter import matplotlib_plotter_with_z_no_std
    # Functions
    # -------------------- user input ------------------------
    a =1
    pathway = '/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction/'
    potential_directories = (f"{pathway}anjany(straight)", f"{pathway}aron(straight)", f"{pathway}kyriakos(straight)",
                             f"{pathway}leon(straight)", f"{pathway}matteo(straight)", f"{pathway}anjany(hunched)",
                             f"{pathway}aron(hunched)", f"{pathway}kyriakos(hunched)", f"{pathway}leon(hunched)",
                             f"{pathway}matteo(hunched)")

    filename = "*.csv"
    weight_threshold = .05
    # -------------------- program ------------------------
    names = ('anjany', 'aron', 'kyriakos', 'leon', 'matteo')
    color_list = ('purple', 'red', 'green', 'orange', 'blue')

    random_array1 = np.array([])
    random_array2 = np.array([])
    feature_array_storage = list()
    position_array_storage = list()
    final_list = list()

    def threshold_finder(y_list, z_list):
        for i, y in enumerate(y_list):
            resy = np.argmax(y >= weight_threshold)
        for i, z in enumerate(z_list):
            resz = np.argmax(z >= weight_threshold)
            # print(resy, resz)
        return resy, resz

    def total_weight_calculator(y_list, z_list, total_list):
        for i, y in enumerate(y_list):
            a = y_list[i] + z_list[i]
            total_list.append(a)
        return total_list

    def normalizer(total_list, y_list, z_list):
        for i, y in enumerate(y_list):
            y_list[i] = y_list[i] / total_list[i][-1]
            z_list[i] = z_list[i] / total_list[i][-1]
            total_list[i] = total_list[i] / total_list[i][-1]
        return total_list, y_list, z_list

    def max_value_list_storage(total_list, random_array1, random_array2):
        for i, y in enumerate(total_list):
            max_floor = np.amax(total_list[i])
            max_floor_loc = np.argmax(total_list[i] * 100)
            random_array1 = np.append(random_array1, [max_floor])
            random_array2 = np.append(random_array2, [max_floor_loc])
        np.vstack(random_array1)
        np.vstack(random_array2)
        max_value_storage.append(random_array1)
        max_value_location_storage.append(random_array2)
        # print(max_value_storage)
        # print(max_value_location_storage)
        return max_value_storage, max_value_location_storage

    def stabilize_location(total_list, random_array1, random_array2):
        for i, t in enumerate(total_list):
            for idx, element in reversed(list(enumerate(total_list[i]))):
                stabilizer = abs(total_list[i][idx] - total_list[i][idx - 1])
                # print(i, idx, stabilizer)
                if stabilizer > .05:
                    # print(i, idx+1, element)
                    random_array1 = np.append(random_array1, [element])
                    random_array2 = np.append(random_array2, [idx * 100])
                    break
        np.vstack(random_array1)
        np.vstack(random_array2)
        stabilize_value_storage.append(random_array1)
        stabilize_location_storage.append(random_array2)
        return stabilize_value_storage, stabilize_location_storage

    def hunch_vs_straight(filenames):
        for h in filenames:
            if 'straight' in h:
                arr = np.array([0, 1])
                position_array_storage.append(arr)
            elif 'hunch' in h:
                arr = np.array([1, 0])
                position_array_storage.append(arr)

        return position_array_storage

    def storage_generators(max_value_storage, max_value_location_storage, stabilize_value_storage,
                           stabilize_location_storage, feature_array_storage):
        resulting_list = max_value_storage + max_value_location_storage + stabilize_value_storage + stabilize_location_storage
        com = np.vstack(resulting_list).T
        # print(com)
        num_rows, num_cols = com.shape
        feature_array_list = (np.split(com, num_rows))
        for ind, g in enumerate(feature_array_list):
            feature_array_storage.append(feature_array_list[ind][0])
        position_array_storage = hunch_vs_straight(filenames)
        return feature_array_storage, position_array_storage

    final_directories, input_integer = user_input_and_directory_generator(potential_directories)
    for i, file in enumerate(final_directories):
        max_value_storage = list()
        max_value_location_storage = list()
        stabilize_value_storage = list()
        stabilize_location_storage = list()
        files = (sorted(glob.glob("/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction//*/*.csv")))
        # for i, file in enumerate(project_dir_list2):
        x_list = list()  # This is where all the x arrays of data are uploaded
        y_list = list()  # This is where all the y arrays of data are uploaded
        z_list = list()
        total_list = list()
        res_list = list()  # This is used to list all the indexes for weight values above .weight threshhold.
        # All the indexes where the weight starts above a certain value go into this list. Multiple arrays are in this list
        final_0_list = list()  # This is used to list the smallest index from each array of indexes over weight_threshold. This takes the smallest values from each array
        # and puts it in a list.
        original_length_list = list()
        modifiedx_length_list = list()
        modifiedy_length_list = list()
        modifiedz_length_list = list()
        totaly = 0  # This is to add all the y lists into one array
        totalz = 0
        # files = (sorted(glob.glob("/Users/Leon/Documents/ToiletProjectUni2021/feature_extraction//*/*.csv")))
        filenames = sorted(glob.glob(os.path.join(final_directories[i], filename)))
        # filenames = filenames[0:number_of_files]
        # print(filenames)
        x_list, y_list, z_list = unpack_and_append_data3(filenames, x_list, y_list, z_list)
        resy, resz = threshold_finder(y_list, z_list)
        x_list, y_list, z_list = threshold_locater_and_posterior_trimmer3(x_list, y_list, z_list, weight_threshold)
        d = find_shortest_length(filenames, original_length_list, x_list)
        x_axis, x_list, y_list, z_list, modifiedx_length_list, modifiedy_length_list, modifiedz_length_list = anterior_trimmer_x_and_y_and_z(
            d, x_list, y_list, z_list, modifiedx_length_list, modifiedy_length_list, modifiedz_length_list)
        total_list = total_weight_calculator(y_list, z_list, total_list)
        total_list, y_list, z_list = normalizer(total_list, y_list, z_list)
        max_value_storage, max_value_location_storage = max_value_list_storage(total_list, random_array1, random_array2)
        max_value_storage, max_value_location_storage = max_value_list_storage(y_list, random_array1, random_array2)
        max_value_storage, max_value_location_storage = max_value_list_storage(z_list, random_array1, random_array2)
        # print(len(max_value_storage))
        # print(len(max_value_location_storage))
        stabilize_value_storage, stabilize_location_storage = stabilize_location(total_list, random_array1,
                                                                                 random_array2)
        stabilize_value_storage, stabilize_location_storage = stabilize_location(y_list, random_array1, random_array2)
        stabilize_value_storage, stabilize_location_storage = stabilize_location(z_list, random_array1, random_array2)
        # print(len(stabilize_value_storage))
        # print(len(stabilize_location_storage))
        feature_array_storage, position_array_storage = storage_generators(max_value_storage,
                                                                           max_value_location_storage,
                                                                           stabilize_value_storage,
                                                                           stabilize_location_storage,
                                                                           feature_array_storage)

    for i, array in enumerate(feature_array_storage):
        tupple = (feature_array_storage[i], position_array_storage[i])
        final_list.append(tupple)
    # print(len(feature_array_storage))
    # print(len(position_array_storage))
    # print(final_list)
    # print(len(final_list))

    return final_list, input_integer