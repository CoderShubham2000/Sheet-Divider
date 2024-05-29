# CSV File Splitter in Google Colab

## Overview
This script enables users to split a single large CSV file into multiple smaller CSV files within the Google Colab environment. The script prompts the user to upload a CSV file, specify the number of parts to split it into, and then automatically downloads the resulting smaller CSV files. Each smaller CSV file retains the header row from the original file.

## Key Features
- **File Upload and Handling**: Utilizes Google Colab's `files.upload()` function to facilitate easy file upload directly from the user's local machine.
- **User Input for Splitting**: Prompts the user to enter the desired number of parts to split the CSV file into.
- **CSV Splitting Logic**: Efficiently splits the CSV file while ensuring that the header row is included in each resulting file. It balances the rows as evenly as possible across the smaller files.
- **Automatic Download**: The split CSV files are automatically downloaded back to the user's local machine using `files.download()`.

## Detailed Steps

### 1. Open Google Colab
- Open your web browser and navigate to [Google Colab](https://colab.research.google.com).

### 2. Create a New Notebook
- Click on "File" > "New notebook" to create a new Colab notebook.

### 3. Copy and Paste the Script
- Copy the provided script and paste it into a code cell in the new Colab notebook.

### 4. Run the Script
- Run the code cell by pressing `Shift + Enter`.

### 5. Upload the CSV File
- A file upload dialog will appear. Select the CSV file you want to split and upload it.

### 6. Enter the Number of Splits
- When prompted, enter the number of parts you want to split the CSV file into and press `Enter`.

### 7. Download the Resulting Files
- The script will process the file and automatically download the resulting smaller CSV files to your local machine.

## Usage Instructions
To use this script effectively, follow these detailed steps:

1. **Open Google Colab**:
   - Open your web browser and go to [Google Colab](https://colab.research.google.com).

2. **Create a New Notebook**:
   - Click on "File" > "New notebook" to create a new Colab notebook.

3. **Copy and Paste the Script**:
   - Copy the provided script and paste it into a code cell in the new notebook.

4. **Run the Script**:
   - Execute the code cell by pressing `Shift + Enter`.

5. **Upload the CSV File**:
   - A file upload prompt will appear. Upload your CSV file.

6. **Enter Number of Splits**:
   - Input the number of parts you wish to split the file into when prompted.

7. **Download Split Files**:
   - The script will generate and download the split CSV files to your machine.

## Conclusion
This script offers a simple and interactive way to manage and manipulate large CSV files within the Google Colab environment. By following the provided instructions, users can efficiently split their CSV files into smaller, more manageable parts, ensuring each resulting file retains the necessary header information.
