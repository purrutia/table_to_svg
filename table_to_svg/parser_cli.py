# parse_cli.py
# Archivo para procesar los datos de la línea de comandos

import argparse

# parser func
def parser_cli():

    # Creates the parser
    my_parser = argparse.ArgumentParser(description="Creates SVG image Table from CSV file")

    # Add the arguments
    my_parser.add_argument('Input_File',
            metavar='inputfile',
            type=str,
            help='the path to the CSV input file')

    my_parser.add_argument('-o',
            '--output',
            metavar='outputfile',
            action='store',
            help='the path to the SVG output file')

    # Execute parse_args()
    args = my_parser.parse_args()

    return args.Input_File, args.output

if __name__ == '__main__':
    input_path, output_path = parser_cli()
    print(f'Input file is: {input_path}')
    print(f'Output file is: {output_path}')
