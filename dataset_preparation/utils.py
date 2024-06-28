
def change_name_batch(path, new_name):
    import os
    for count, filename in enumerate(os.listdir(path)):
        dst = new_name + str(count) + ".jpg"
        src = path + filename
        dst = path + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        print(f"Renamed {filename} to {dst}")