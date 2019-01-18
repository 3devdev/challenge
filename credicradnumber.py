# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

for line in sys.stdin:
    strip_line_newline = line.rstrip()
    strip_line = strip_line_newline.replace("-", "")
    #print(strip_line)
    if( strip_line.isdigit()): # to check for [9-0] and integer
        if (len(strip_line) == 16): # to check 16 digits
            proceed = "true"
            if "-" in strip_line_newline:
                check_no_of_digits = strip_line_newline.split("-")
                proceed = "true"
                for sequence in check_no_of_digits:
                    if len(sequence) != "4":
                        proceed = "false"
            if (str(strip_line)[:1] == "4") or (str(strip_line)[:1] == "5") or (str(strip_line)[:1] == "6") and proceed == "true": # to check for 4,5,6
                invalid = "false"
                for match in re.finditer(r"(\w)\1\1", str(strip_line)):
                    match_string = str(strip_line)[match.start():match.end()]
                    #print(match_string)
                    if len(str(strip_line)[match.start():match.end()]) >=3:
                        invalid = "true"
                if str(invalid) == "false":
                    print("Valid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        elif (len(strip_line) < 4):
            nothing = 1
        else:
            print("Invalid")

    else:
        print("Invalid")
