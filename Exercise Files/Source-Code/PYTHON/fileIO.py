# STEPS DECLARATION
# 1. Open and read the file
# 2. Create a for loop to read it line by line
# 3. Separate the fields by spaces taken from the input file.
# 4. If the filtered input in the array 2 [0,1,2] has the P Letter Then.
# 5. Print line by line those values with P.
# 6. Close the file.


f = open('../inputFile.txt', 'r')

for line in f:
    line_split = line.split()
    print(line_split)                   #Optional
    if line_split [2] == 'P':
        print(line)
f.close();