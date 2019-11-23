#import csv module to read data from csv file
import csv
#function to read data from the file
def readFile(filename):
    #initialise results as empty dictionary
    results = {}
    #try catch block for handling file not found exception
    try:
        #open the file using file reader and name it as employees
        with open(filename,'r') as file:
            #use csv reader to read data from the file seperated by ','
            csv_reader=csv.reader(file)
            #remove column names
            headRow=next(csv_reader) #headrow[0] is date and headrow[1] is profit/loss
            #now for all rows in csv reader
            for row in csv_reader:
                results[row[0]]=int(row[1]) #row[0] is month and row[1] is profit/loss
    #if file not found then show error message
    except OSError as e:
        print("\nSorry, "+filename+" could not be found.\n")
    #now return results
    return results

#function to find net profit loss in data 
def netProfitLoss(data):
    #initialise with 0
    net=0
    #iterate over all month and find profit loss in that month
    for month in data:
        net+=data[month] #add profit/loss of month
    #return net profit/loss
    return net

#function to find average change in data
def averageChange(data):
    #create a list of changes 
    change=[]
    #iterate over all month and find change from previous data
    prev=0
    for month in data:
        #if its first month then mark update prev
        if prev==0:
            prev=data[month]
        #otherwise find change and update prev
        else:
            change.append(data[month]-prev)
            prev=data[month]
    #now calculate average change and return it
    average=sum(change)/len(change)
    return average

#function to find greatest increase and decrease in profit
def increaseDecrease(data):
    #initialise greatest increase as minimum ans month as null
    increase=-100000
    inc_month=''
    #initialise greatest decrease as maximum ans month as null
    decrease=100000
    dec_month=''
    #iterate over all month and find change from previous data
    prev=0
    for month in data:
        #if its first month then mark update prev
        if prev==0:
            prev=data[month]
        #otherwise find change and update prev
        else:
            change=data[month]-prev
            prev=data[month]
            #if change is more than greatest increase update it
            if change>increase:
                increase=change
                inc_month=month
            #if change is less than greatest decrease update it
            if change<decrease:
                decrease=change
                dec_month=month
    #now create a list and and add greatest increase month with increase and 
    #greatest decrease month with decrease
    lst=[]
    lst.append(str(inc_month)+" ($"+str(increase)+")")
    lst.append(str(dec_month)+" ($"+str(decrease)+")")
    #now return the list as output
    return lst

#main function implementation
def main():
    #read data from the file provided
    data=readFile('budget_data.csv')
    #print interface
    print()
    print("\'\'\'text")
    print("Financial Ananlysis")
    print(30*'-')
    #months in data is equal to length of dictionary
    print("Total Months: "+str(len(data))) 
    #find and print net profit loss
    net=netProfitLoss(data)
    print("Total: $"+str(net))
    #find and print average change in data
    change=averageChange(data)
    print("Average Change: $"+str("{0:.2f}".format(change)))
    #find and print greatest increase and decrease in profit
    lst=increaseDecrease(data)
    print("Greatest Increase in Profit: "+str(lst[0]))
    print("Greatest Decrease in Profit: "+str(lst[1]))
    print("\'\'\'")
    
#start the main function
if __name__=='__main__':
    main()