def user_input_and_directory_generator(potential_directories):
    short_list = list()

    def Diff(user_list, newlist):
        incorrect_entry = list(set(user_list) - set(newlist)) + list(set(newlist) - set(user_list))
        return incorrect_entry

    while True:
        input_string = input("Enter the names of the people you want to analyze separated by spaces. The possible names are: anjany, aron, chinmay, esther, fahrad, ivna, kyriakos, laura, leon, matteo, matthias, professor, todor, zsolt. Please "
            "write in all lowercase. The code will not work if the names arent typed correctly. Don't enter the same names again if you have already done so. If you want to use everyone, type all. \n")
        if input_string == 'all':
            input_string = 'anjany aron chinmay esther fahrad ivna kyriakos laura leon matteo matthias professor todor zsolt'
        long_list = input_string.split()
        #     short_list = []
        #     [short_list.append(x) for x in long_list if x not in short_list]


        newlist = [x for x in long_list if
                   "aron" in x or "leon" in x or "fahrad" in x or "kyriakos" in x or "anjany" in x or "matteo" in x or "todor" in x or "zsolt" in x or 'ivna' in x or 'chinmay' in x or 'laura' in x or 'professor' in x or 'esther' in x or 'matthias' in x]

        short_list = short_list + newlist
        print(short_list)
        if len(newlist) < len(long_list):
            incorrect_entry = Diff(long_list, newlist)
            if len(incorrect_entry) > 0:
                print(f" You have entered the incorrect names: {incorrect_entry} Please reread the initial message")
                incorrect_entry = list()
                continue  # print('hi')
        else:
            break
    final = list()
    [final.append(x) for x in short_list if x not in final]
    print("\n")
    final_directories = list()
    # print list
    print('list: ', final)
    for s1 in final:
        for i, s2 in enumerate(potential_directories):
            if s1 in s2:
                final_directories.append(potential_directories[i])
    input_integer = int(input("Enter the percentage of the data that you want to be to train the machine learning code. \n"))
    print(type(input_integer))
    return final_directories, input_integer