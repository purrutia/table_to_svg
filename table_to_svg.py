import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import getopt
import sys


# Get the commands from command line, except filename
argv = sys.argv[1:]

# try to get the options
try:
    # Define getopt parameters
    opts, args = getopt.getopt(argv, 'hf:o:', ['help','file', 'output'])

    # Review options qty
    if len(opts) == 0 or len(opts) > 2:
        print('usage: python3 table_svg_render.py -f <inputfile.csv> -o <outputfile.svg>')
    elif len(opts) == 1:
        if opts[0][0] in ('-h', '--help'):
            print('usage: python3 table_svg_render.py -f <inputfile.csv> -o <outputfile.svg>')
        elif opts[0][0] in ('-f', '--file'):
            if opts[0][1].endswith(".csv"):
                input_file = opts[0][1]
                output_file = opts[0][1][:-4] + ".svg"
            else:
                print('ERROR: Needs a CSV file')
                print('usage: python3 table_svg_render.py -f <inputfile.csv> -o <outputfile.svg>')
                sys.exit(0)
        else:
            print('ERROR: Needs input file')
            print('usage: python3 table_svg_render.py -f <inputfile.csv> -o <outputfile.svg>')
            sys.exit(0)
    else:
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print('usage: python3 table_svg_render.py -f <inputfile.csv> -o <outputfile.svg>')
                sys.exit(0)
            elif opt in ('-f', '--file'):
                if arg.endswith(".csv"):
                    input_file = arg
                else:
                    print('ERROR: Needs a CSV file')
                    print('usage: python3 table_svg_render.py -f <inputfile.csv> -o <outputfile.svg>')
                    sys.exit(0)
            else:
                if arg.endswith(".svg"):
                    output_file = arg
                else:
                    output_file = arg + '.svg'
except getopt.GetoptError:
    print('ERROR usage: python3 table_svg_render.py -f <inputfile.csv> -o <outputfile.svg>')
    sys.exit(2)

# Dataframe read
try:
    df = pd.read_csv(input_file)
except:
    print(f'Cannot read {input_file}')
    sys.exit(0)

# Render table function
def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
        header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color = 'w', bbox=[0, 0, 1, 1],
        header_columns=0, ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')
    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)
    mpl_table.auto_set_column_width(col=list(range(len(df.columns))))

    for k, cell in mpl_table._cells.items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors)])
    return ax.get_figure(), ax

fig, ax = render_mpl_table(df, header_columns=0, col_width=3.0)
fig.tight_layout()
fig.savefig(output_file)
