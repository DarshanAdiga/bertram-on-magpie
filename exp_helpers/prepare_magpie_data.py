import argparse
import glob
import re
import os
from collections import defaultdict

IDIOM_TOKEN_PATTERN = re.compile(r'(ID[a-z]+ID)')

def convert_to_bertram_token(line):
    line = line.strip()
    bertram_line = IDIOM_TOKEN_PATTERN.sub(r"<BERTRAM:\1>", line)
    return bertram_line

def _test_replacement():
    test_cases = [
        ('this is a IDtesterID', 'this is a <BERTRAM:IDtesterID>'),
        ('IDtadaID is another test', '<BERTRAM:IDtadaID> is another test'),
        (' IDtrickyID test', '<BERTRAM:IDtrickyID> test'),
        ('this IDisaID multi IDtokenID test-IDerrrID', 'this <BERTRAM:IDisaID> multi <BERTRAM:IDtokenID> test-<BERTRAM:IDerrrID>'),
    ]
    for test_case,expected in test_cases:
        assert convert_to_bertram_token(test_case) == expected, f"Failed! {test_case}"

def prepare_magpie_data(input_dir, output_dir):
    """
    Convert all the single-tokens of the form "ID...ID" to "<BERTRAM:ID...ID>" in the CSV files in input_dir and save \
        them on the output_dir.
    """
    if not os.path.exists(input_dir):
        raise ValueError(f'Input directory {input_dir} does not exist')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    in_files = [f'{input_dir}/{t}.csv' for t in ['train', 'dev', 'test']]
    for in_file in in_files:
        print(f"Processing {in_file}")
        target_file = f'{output_dir}/{os.path.basename(in_file)}'
        with open(target_file, 'w') as out_file:
            with open(in_file, 'r') as ifile:
                for line in ifile.readlines():
                    bertram_line = convert_to_bertram_token(line)
                    out_file.write(bertram_line+'\n')
        print(f"Saved to {target_file}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Prepare MAGPIE data for Sequence Classification with <BERTRAM:> idiom tokens")
    parser.add_argument('-i', '--input_dir', required=True, help='A directory with {train,dev,test}.csv MAGPIE files, containing <ID..ID> single tokens.')
    parser.add_argument('-o', '--output_dir', required=True, help='A directory where {train,dev,test}.csv the output files will be saved. One files will contain <BERTRAM:ID...ID> tokens.')

    args = parser.parse_args()

    # Test the token replacement first
    _test_replacement()

    # Convert the data files
    prepare_magpie_data(args.input_dir, args.output_dir)

