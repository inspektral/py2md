# # py2md

# Okay im using the file to test, itself, it is kinda funky but seems fun lol

# - this
# - is
# - a
# - list

import sys
import argparse
from pathlib import Path

def python_to_markdown(path_in: str, path_out:str):
    with open(path_in, 'r') as input:
        with open(path_out, 'w') as output:

            code = False
            for line in input:
                
                empty = is_empty(line)
                comment = is_comment(line)

                if empty:
                    output.write(line)
                
                elif code and comment:
                    code = False
                    output.write('```\n')
                    output.write(line[2:])

                elif code and not comment:
                    output.write(line)

                elif not code and not comment:
                    code = True
                    output.write('\n```python\n')
                    output.write(line)

                elif not code and comment:
                    output.write(line[2:])
            
            if code:
                output.write('```\n')

    return True

# this is an intermediate
# big comment
# to see if it works

def is_comment(line:str):
    return line[0] == '#'

def is_empty(line:str):
    return line.isspace() or not line

def main():
    parser = argparse.ArgumentParser(description='.py to .md')
    
    parser.add_argument('-i',
                        '--input', 
                        type=str, 
                        default='.', 
                        help='Input path')
    
    parser.add_argument('-o', 
                        '--output', 
                        type=str, 
                        default='.', 
                        help='Output path')

    args = parser.parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    for file_path in Path(input_path).rglob('*.py'):
        python_to_markdown(file_path, file_path.with_suffix('.md'))    

if __name__ =='__main__':
    main()
