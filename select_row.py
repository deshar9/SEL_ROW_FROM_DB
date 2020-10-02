import csv

def main():

    source = open('691359226421-aws-billing-detailed-line-items-with-resources-and-tags-2016-06.csv', 'r')
    dest = open('output.csv','w')
    reader = csv.reader(source, delimiter=',')

    #------------------------------
    cnt = 0
    for col in reader:

        if cnt == 0: #header row
            dest.write(','.join(col))
            cnt = cnt + 1
        elif col[2] == "066789247273":
            dest.write(','.join(col))

        #print(col[2])

    # ------------------------------

    dest.close()
    source.close()

#==============================================
if __name__=="__main__":
    main()
