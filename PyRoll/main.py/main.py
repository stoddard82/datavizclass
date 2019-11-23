#import csv module to read data from csv file
import csv
#function to read data from the file
def readFile(filename):
    #initialise results as empty dictionary which will contain only voterId and candidate name who recieved tha vote
    results = {}
    #try catch block for handling file not found exception
    try:
        #open the file using file reader and name it as employees
        with open(filename,'r') as file:
            #use csv reader to read data from the file seperated by ','
            csv_reader=csv.reader(file)
            #remove column names
            headRow=next(csv_reader) #headrow[0] is VoterID and headrow[1] is county and headRow[2] is candidate
            #now for all rows in csv reader
            for row in csv_reader:
                #map voter id with candidate who recieved in dictionary
                results[row[0]]= row[2] 
    #if file not found then show error message
    except OSError as e:
        print("\nSorry, "+filename+" could not be found.\n")
    #now return results
    return results

#function to count votes for all candidates
def countVotes(data):
    #initialise a dictionary with key as candidate and value as votes
    count={}
    #now iterate all over data and count votes for candidate
    for voterId in data:
        #find candidate who recieved that voter id
        candidate=data[voterId]
        #if candidate is in count then add its value by 1
        if candidate in count:
            count[candidate]=count[candidate]+1
        #otherwise insert candidate in count with value 1
        else:
            count[candidate]=1
    #now return the dictionary of counts of votes
    return count

#main function implementation
def main():
    #read data from the file provided
    data=readFile('election_data.csv')
    #print interface
    print()
    print("\'\'\'text")
    print("Election Results")
    print(30*'-')
    #total votes in data is equal to length of data
    total=len(data)
    print("Total Votes: "+str(total)) 
    print(30*'-')
    #find and print total votes cast for candidates
    lst=countVotes(data) #lst will contain all candidates and their vote count
    #print all candidates and their vote data 
    for candidate in lst:
        #find vote count and its percentage
        votes=lst[candidate]
        percentage=(votes/total)*100
        print(candidate+": "+str("{0:.3f}".format(percentage))+"% ("+str(votes)+")")
    #now find the winner having maximum votes
    winner=''
    #initialise max vote as zero
    max_vote=0
    for candidate in lst:
        #if vote count of candidate is greater than max then update winner and max
        if lst[candidate]>max_vote:
            winner=candidate
            max_vote=lst[candidate]
    #find and print winner
    print(30*'-')
    print("Winner: "+winner)
    print(30*'-')
    print("\'\'\'")
    print()

#start the main function
if __name__=='__main__':
    main()