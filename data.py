def create_dataset(file):
    try:
        dataset = dict()

        with open('ukraine_deputies.csv', encoding="utf-8", mode='r') as f:
            file_line = f.readline()
            if not file_line:
                return dataset

            header = file_line.rstrip().split(",")
            file_line = f.readline()
            while file_line:
                [name, party, city, constituency] = [element.strip() for element in file_line.rstrip().split(",")]


                if city not in dataset:
                    dataset[city] = dict()

                if constituency not in dataset[city]:
                    dataset[city][constituency] = dict()

                if party not in dataset[city][constituency]:
                    dataset[city][constituency][party] = dict()

                if name not in dataset[city][constituency][party]:
                    dataset[city][constituency][party][name] = dict()

                dataset[city].update({constituency: {
                                                     party: {
                                                             name
                                                            }
                                                    }
                                     })

                file_line = f.readline()

        return dataset

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return dict()

print(create_dataset('ukraine_deputies.csv'))

# with open('ukraine_deputies.csv', encoding="utf-8", mode='r') as file:
#     data = file.readline()
#
#     data = csv.reader(file, dialect='excel')
#     for dep in data:
#         name = dep[3]
#         party = dep[4]
#         city = dep[5]
#         constituency = dep[6]
#         dataset[city] = {constituency: {
#                                         party: {
#                                                  name
#                                                }
#                                         }
#                          }
#
#     print(dataset)
