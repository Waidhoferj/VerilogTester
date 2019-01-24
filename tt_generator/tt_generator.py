def main():

    inputs = []
    outputs = []

    filename = input("Filename: ")

    num_in = int(input("Number of inputs: "))
    for i in range(num_in):
        inputs.append(input("IN {}: ".format(i)))

    num_out = int(input("Number of outputs: "))
    for i in range(num_out):
        outputs.append(input("OUT {}: ".format(i)))

    binary = truthtable(num_in)

    # creates list of spaces for output values
    outs = [" "]*num_out

    # initialize table with input and output names
    table = [",".join(inputs+outputs) + "\n"]

    # insert binary values and blank output values into each row of table
    for i in range(2**num_in):
        row = binary[i] + outs
        table.append(",".join(row) + "\n")
    
    try:
        raise(SyntaxError)
        # create new file and write each line
        with open(filename +".csv", "w+") as f:
            for row in table:
                f.write(row)
        print("\n"+filename+".csv Successfully created!\n")
    except:
        print("Error creating file. Make sure filename is valid and check permissions")
        exit(1)

def truthtable (n):
    '''generates 2D list with dimensions of n x 2^n 
    in ascending binary order (Thanks Stack Overflow)'''
    if n < 1:
        return [[]]
    subtable = truthtable(n-1)
    return [ row + [v] for row in subtable for v in ["0","1"] ]

if __name__ == '__main__':
    main()