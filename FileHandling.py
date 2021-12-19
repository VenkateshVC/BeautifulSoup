#Program for File Handling. Reads a file and gets the email ID's and prints out a file with
#the Email ID's and their number of occurrences

FileName = "mbox.txt"
outFileName = "outputSorted.txt"
FileHandle = open(FileName)
outFileHandle = open(outFileName,"w")
FromAddresses = {}
maxEmailIDLen = 0
for Lines in FileHandle.readlines():
    if Lines.startswith("From"):
        Words = Lines.split()
        EmailID = Words[1]

        #Determine the Length of Email ID. The Longest Email ID length is used for formatting the report

        if len(EmailID) > maxEmailIDLen:
            maxEmailIDLen = len(EmailID)

        #If Email ID is not found in the Dictionary, then it is a new email ID and so Add to Dictionary
        #If the Email ID exists, then increment the counter
        if EmailID not in FromAddresses:
            FromAddresses[EmailID] = 1
        else:
            FromAddresses[EmailID] += 1

outFileHandle.write("Email ID".center(maxEmailIDLen) + " | " + "Total Count".center(13) + "\n")

outFileHandle.write("==========================".center(maxEmailIDLen) + " | " + "===========".center(13) + "\n")

#Print the report of Email ID's in the Ascending order of occurrence of the count.

for key,value in sorted(FromAddresses.items(),key= lambda item:item[1]): #Sort by the Value
    #Left Justify the Email ID and then print the count of Email ID
    outFileHandle.write(str(key).ljust(maxEmailIDLen) + " | " + str(value).center(13) + "\n")

outFileHandle.close()