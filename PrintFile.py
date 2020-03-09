import os

def main():
    print(os.getcwd)
    myFile = open("Covid19-Confirmed.csv", 'r')

    for line in myFile:

        if "US" in line:
            #print(line)
            info = line.split(",")
            last = len(info)-1
            print(info[0], ",", info[1], ",", info[last])


    myFile.close()


if __name__ == '__main__':
    main()
