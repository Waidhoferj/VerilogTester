#Verilog Tester
Turn your truth tables into System Verilog simulation code.

##Quick Start
1. Clone the repo:
```
git clone https://github.com/Waidhoferj/VerilogTester.git
```
2. Locate your truth table
   You can put your truth table in the repo folder and call it with the file name. Otherwise you will have to provide the full file path. To get the path to your file, navigate to the file with the command line and type `pwd`. Take note of the number of inputs in your truth table.
3. Create your tests! Use the terminal to navigate to your cloned repo and process the truth table with this command:
   ```python3 VerilogTests.py [PATH/FILENAME] [NUMBER OF INPUTS (optional)] [SIM NAME (optional)]```
4. Find your output in the same folder as your truth table.
5. Copy the outputted text into your System Verilog Sim file
   
##Further Details
  -  truth  table must be in a CSV format.
  - If you don't specify the number of inputs, the program assumes that all but the rightmost column are inputs.
  - With an unspecified simulation name, the tests will input **[Sim_Name ]** in the required locations.
