# Okay im using the file to test, itself, it is kinda funky but seems fun lol

import sys

def python_to_markdown(path_in: str, path_out:str):
    with open(path_in, 'r') as input:
        with open(path_out, 'w') as output:

            code_block = False
            for i, line in enumerate(input):
                if code_block:
                    if is_comment(line):
                        code_block = False
                        output.write('```\n')
                        output.write(line[2:])
                    else:
                        output.write(line)
                else:
                    if not is_comment(line):
                        code_block = True
                        output.write('\n```python')
                        output.write(line)
                    else:
                        output.write(line[2:])
            
            if code_block:
                output.write('')

    return True

# this is an intermediate
# big comment
# to see if it works

def is_comment(line:str):
    return line[0] == '#'

def main():
    # stuff with the arguments i guess
    path_in = sys.argv[0]
    path_out = sys.argv[1]
    
    python_to_markdown(path_in, path_out)

if __name__ =='__main__':
    main()


