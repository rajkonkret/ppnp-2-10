import os

for root, dirs, files in os.walk(".."):
    abs_root = os.path.abspath(root)
    # print(abs_root)
    if dirs:
        print("Directories")
        for dir_ in dirs:
            print(dir_)

    if files:
        print("Files:")
        for filenme in files:
            print(filenme)

for root, dirs, files in os.walk("../ppnp-2-10"):
    for file in files:
        if file == 'api_get.py':
            file_path = os.path.join(root, file)
            print(file_path)  # ../ppnp-2-10\api_get.py
