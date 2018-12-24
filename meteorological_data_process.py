import os
import gzip


def data_process(filepath):
    path_dir = os.listdir(filepath)
    for alldir in path_dir:
        subdir = os.path.join('{}\{}'.format(filepath, alldir))
        gz_dir = os.listdir(subdir)
        minimum, maximum, count = 100, -100, 0
        n, tempe_list = [], []
        for gz_name in gz_dir:
            gzname = os.path.join('{}\{}'.format(subdir, gz_name))
            data = gzip.open(gzname, mode='rt')
            for eachline in data:
                temperature = int(eachline[87:93]) / 100
                tempe_list.append(temperature)
                if temperature != 999.99 and temperature < minimum:
                    minimum = temperature
                if temperature != 999.99 and temperature > maximum:
                    maximum = temperature
                count += 1
                n.append(count)
        print("%s年  最低气温为%.2f℃, 最高气温为%f℃" % (alldir, minimum, maximum))


def main():
    data_process('noaa')


if __name__ == "__main__":
    main()
