import sys

def generateTests(data):
    data_header = data[0].strip().split(",")
    inputs = data_header[:-1]
    output = data_header[-1]
    tests = [createHeader(data_header)]
    for i, line in enumerate(data[1:]):
        values = line.strip().split(",")
        test_number = "//Test {}\n".format(i+1)
        input_vals = " ".join(["{} = {};".format(input, values[index]) for index, input in enumerate(inputs)]) + "\n"
        time_paused = "#10\n"
        error_condition = 'if ({}!=={}) $display("Error'.format(output, values[-1])
        error_output_1 = " ".join([ " {}:%b".format(input) for input in inputs]) +'",'
        error_output_2 = ",".join([input for input in inputs]) + ");\n"
        tests.append(test_number + input_vals + time_paused + error_condition + error_output_1 + error_output_2)
    tests.append('\n$display("Finished");\nend\nendmodule')
    return tests

def createHeader(header):
    verilog_header = "logic"
    for index, inout in enumerate(header):
        verilog_header += (" " + inout)
        if index != len(header) - 1:
            verilog_header += ","
        else:
            verilog_header += ";\n"
        
    verilog_header += "Lab(number) Lab(number)_inst ("
    for index, inout in enumerate(header):
        verilog_header += ".{a}({a})".format(a=inout)
        if index != len(header)-1:
            verilog_header += ", "
        else:
            verilog_header += ");"
        
    verilog_header += "\n\tinitial\n\t\tbegin\n"

    return verilog_header


def main():
    try:
        file = sys.argv[1]
        with open(file) as truth_table:
            table_data = truth_table.readlines()
    except:
        print("Please provide a legitimate file name.")
        return
    output_text = generateTests(table_data)
    file_name = file.split(".")[0]
    
    
    with open(file_name + "_tests.txt", "w+") as verilog_file:
        verilog_file.writelines(output_text)
    print("Tests created!\nFound in {}_tests.txt".format(file_name))    

if __name__ == "__main__":
    main()
    

        
        
    