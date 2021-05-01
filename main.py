import os
import tqdm
import  time

input_path = input("Enter path of the directory: ")
# path of image folder
path = input_path

# read path of images
os.chdir(path)

# defining counter
counter = 1


# creating sequence number
def counter_create(num: int):
    if 10 > num >= 1:
        ctr = "000" + str(num)
    elif 100 > num >= 10:
        ctr = "00" + str(num)
    elif 1000 > num >= 100:
        ctr = "0" + str(num)
    else:
        ctr = str(num)
    return ctr


if __name__ == '__main__':
    r = 100
    s = []
    # defining prefix
    prefix = input("Enter Prefix: ") + "_"
    for file in os.listdir():
        suffix = file.split('.')[1]
        s.append(suffix)
        middle_counter = counter_create(counter)
        new_name = prefix + "{}".format(middle_counter) + "." + suffix
        os.rename(file, new_name)
        counter = counter + 1


    print("File extensions are :")
    print(s)
    print("#############################################################")
    print("Total file renamed --->" + str(counter))
    print("#############################################################")
