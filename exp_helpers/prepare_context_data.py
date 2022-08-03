import argparse
import glob
import re
import os
from collections import defaultdict

IDIOM_TOKEN_PATTERN = re.compile(r'ID[a-z]*ID')

def _get_output_file_for_idiom(idiom_token, output_dir):
    return f'{output_dir}/{idiom_token}.txt'

def prepare_data_for_bertram(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    idiom_file_dict = defaultdict(list)
    for text_file in glob.glob(f'{input_dir}/*.txt'):
        with open(text_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                for match in IDIOM_TOKEN_PATTERN.finditer(line):
                    found_idi_token = match.group()
                    context_list = idiom_file_dict[found_idi_token]
                    context_list.append(line.strip())
    # Write contexts to separate files
    for idiom_token, context_list in idiom_file_dict.items():
        output_file = _get_output_file_for_idiom(idiom_token, output_dir)
        with open(output_file, 'w') as f:
            for context in context_list:
                f.write(context+'\n')
    print(f"Prepared data for bertram in {output_dir}. Found {len(idiom_file_dict)} idiom tokens.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Prepare context data for all the idioms into a folder")
    parser.add_argument('-i', '--input_dir', required=True, help='A directory with .txt files, each file containing one sentence per line. Sentence may have 0 or more idiom tokens.')
    parser.add_argument('-o', '--output_dir', required=True, help='A directory where the output files will be saved. One file per idiom will be created.')

    args = parser.parse_args()
    prepare_data_for_bertram(args.input_dir, args.output_dir)

