import os
import re

import click
import xlsxwriter

EXT_TYPE_COMMAS = 'csv'
EXT_TYPE_EXCEL = 'xlsx'
EXT_TYPE_TABS = 'tsv'
EXT_TYPE_TEXT = 'txt'

EXT_DEFAULT_TYPE_IN = EXT_TYPE_TEXT
EXT_DEFAULT_TYPE_OUT = EXT_TYPE_EXCEL

REGEX_DELIMITER_COMMAS = ","
REGEX_DELIMITER_SPACES = r"\s{4,}"
REGEX_DELIMITER_TABS = r"\t"


def replace_extension(file_path, ext_type = EXT_DEFAULT_TYPE_IN):
    """Find the file extension in file_path and replace with ext_type."""
    return os.path.splitext(file_path)[0] + "." + ext_type


def expose_created_file(file_path, ext_type):
    """Print a status message and locate file in filesystem."""
    click.echo('Zoox created a new %s file: %s' %
               (ext_type, click.format_filename(file_path)))
    click.launch(file_path, locate=True)


@click.command()
@click.option('--type', '-t', 'file_extension',
    default=EXT_DEFAULT_TYPE_OUT,
    show_default=True,
    type=click.Choice([
        EXT_TYPE_EXCEL,
        EXT_TYPE_COMMAS,
        EXT_TYPE_TABS], case_sensitive=False))
@click.argument('file_path',
    type=click.Path(
        exists=True,
        dir_okay=False,
        resolve_path=True))
def cli(file_extension, file_path):
    """Convert a space-delimited text file into .xlsx, .csv, or .tsv."""
    if file_path:
        infile = open(file_path, "r")
        outpath = replace_extension(file_path, file_extension)
        regex = re.compile(REGEX_DELIMITER_SPACES)
        
        if file_extension == EXT_TYPE_EXCEL:
            row = 0
            workbook = xlsxwriter.Workbook(outpath)
            worksheet = workbook.add_worksheet()
            worksheet.write('A1', 'Time')
            worksheet.write('B1', 'Commenter')
            worksheet.write('C1', 'Comment')
            while True:
                line = infile.readline()
                if not line:
                    infile.close()
                    workbook.close()
                    expose_created_file(outpath, file_extension)
                    break
                row = row + 1
                for idx, cell in enumerate(regex.split(line)):
                    worksheet.write(row, idx, cell)
        else:
            outfile = open(outpath, 'w')
            delimiter = REGEX_DELIMITER_COMMAS if file_extension == EXT_TYPE_COMMAS else REGEX_DELIMITER_TABS
            while True:
                line = infile.readline()
                if not line:
                    infile.close()
                    outfile.close()
                    expose_created_file(outpath, file_extension)
                    break
                outfile.write(regex.sub(delimiter, line))
