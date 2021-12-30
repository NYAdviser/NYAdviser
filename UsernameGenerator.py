#File: UsernameGenerator.py
# This program generates usernames in batch mode from an input file.
#by: Noah Porcelain

def main():
    print("This program generates usernames")
    print("from a file of names.\n")
    # get the file names
    
    infileName  = input("What files are the names in? ")
    outfileName = input("Place usernames in this file: ")
    # open the files
    
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    for i in infile:
    # get user's first & last names
        
        first, last = i.split()
        uname = (first[0]+last[:7]).lower()
        print(uname, file=outfile)
        
    #close both files
    infile.close()
    outfile.close()
    print("Usernames have been")
    print("written to:", outfileName)
    
main()
