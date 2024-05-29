# -*- coding: utf-8 -*-
"""SheetDivider.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eiAQrfCQRN3btJIzgEH8w-_KLjH5H7hz
"""

import csv
import os
from google.colab import files

def split_csv(input_file, num_splits):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        rows = list(reader)

    total_rows = len(rows)
    rows_per_file = total_rows // num_splits
    remainder = total_rows % num_splits

    base_filename = os.path.splitext(input_file)[0]

    start = 0
    for i in range(num_splits):
        end = start + rows_per_file + (1 if i < remainder else 0)
        output_file = f"{base_filename}_part_{i+1}.csv"

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(rows[start:end])

        start = end

    print(f"CSV file has been split into {num_splits} parts.")
    return [f"{base_filename}_part_{i+1}.csv" for i in range(num_splits)]

# Upload the CSV file
uploaded = files.upload()

# Assuming only one file is uploaded
input_file = list(uploaded.keys())[0]

# Get the number of splits from the user
num_splits = int(input("Enter the number of parts to split the CSV file into: "))

# Split the CSV
output_files = split_csv(input_file, num_splits)

# Download the output files
for output_file in output_files:
    files.download(output_file)