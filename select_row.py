import csv

def main():

    x = open('TEST_CSV.csv', 'r')
    y = open('output.csv','w')
    reader = csv.reader(y, delimiter=',')

    for i in x:

         y.write(i)

    y.close()
    x.close()

if __name__=="__main__":
    main()
