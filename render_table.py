import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import datetime as dt


# Render table function
def render_the_table(data, col_width=3.0, row_height=0.625, font_size=14,
        header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color = 'w', bbox=[0, 0, 1, 1],
        header_columns=0, ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')
    the_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(font_size)
    the_table.auto_set_column_width(col=list(range(len(data.columns))))

    for k, cell in the_table._cells.items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors)])
    return ax.get_figure(), ax

if __name__ == '__main__':
    # Read Input file
    test_files_path = Path.cwd() / "test_files"
    input_file = str(test_files_path / "test_table1.csv")

    # Create output file
    output_file_name = f'table1_{dt.datetime.now()}.png'.replace(" ", "").replace(":", "_")
    output_file = str(test_files_path / output_file_name)

    # Define input data
    data = pd.read_csv(input_file)

    fig, ax = render_the_table(data, header_columns=0, col_width=3.0)
    fig.tight_layout()
    fig.savefig(output_file)
    print(f'data is type: {type(data)}')
    print(f'fig is type: {type(fig)}')
    print(f'ax is type: {type(ax)}')
