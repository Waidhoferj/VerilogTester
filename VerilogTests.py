import sys

def generateTests(data, input_count, module_name):
    data_header = data[0].strip().split(",")
    if input_count is None:
        input_count = len(data_header) - 1
    inputs = data_header[:input_count]
    outputs = data_header[input_count:]
    tests = [createHeader(data_header, module_name)]
    for i, line in enumerate(data[1:]):
        values = line.strip().split(",")
        test_number = "//Test {}\n".format(i+1)
        input_vals = " ".join(["{} = {};".format(input, values[index]) for index, input in enumerate(inputs)]) + "\n"
        time_paused = "#10\n"
        error_condition = "if (" + " || ".join(["{}!=={}".format(output, values[input_count + index]) for index, output in enumerate(outputs)]) + ') '
        error_output_1 = '$display("Error'  + " ".join([ " {}:%b".format(input) for input in inputs]) +'",'
        error_output_2 = ",".join([input for input in inputs]) + ");\n"
        tests.append(test_number + input_vals + time_paused + error_condition + error_output_1 + error_output_2)
    tests.append('\n$display("Finished");\nend\nendmodule')
    return tests

def createHeader(header, module_name):
    verilog_header = "logic"
    for index, inout in enumerate(header):
        verilog_header += (" " + inout)
        if index != len(header) - 1:
            verilog_header += ","
        else:
            verilog_header += ";\n"
        
    verilog_header += "{module} {module}_inst (".format(module = module_name)
    for index, inout in enumerate(header):
        verilog_header += ".{a}({a})".format(a=inout)
        if index != len(header)-1:
            verilog_header += ", "
        else:
            verilog_header += ");"
        
    verilog_header += "\n\tinitial\n\t\tbegin\n"

    return verilog_header


def main():
    input_count = None
    module_name = "[Sim_Name]"
    try:
        file = sys.argv[1]
        with open(file) as truth_table:
            table_data = truth_table.readlines()
    except:
        print("Please provide a legitimate file name.")
        return
    if len(sys.argv) > 3:
        module_name = sys.argv[3]
    if len(sys.argv) > 2 and sys.argv[2].isdigit():
        input_count = int(sys.argv[2])
    
    output_text = generateTests(table_data, input_count, module_name)
    file_name = file.split(".")[0]
    with open(file_name + "_tests.txt", "w+") as verilog_file:
        verilog_file.writelines(output_text)
    print("Tests created!\nFound in {}_tests.txt".format(file_name))    

if __name__ == "__main__":
    main()
    

        
        
    