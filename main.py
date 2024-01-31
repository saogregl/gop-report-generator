import os
from dotenv import load_dotenv
from src.extract import extract_gop
from src.extract_gop import run_extraction
from src.to_excel import to_excel

# Load environment variables
load_dotenv()

def main():
    # Step 0: Extract the GOP data and save it to JSON files. 
    extract_gop()
    # Step 1: Run the extraction process to fetch and save occurrences to JSON files
    print("Starting the extraction process...")
    run_extraction()
    print("Extraction completed successfully.")

    # Step 2: Generate Excel report from saved JSON files
    print("Generating Excel report...")
    to_excel()
    print("Report generated successfully. Check the output Excel file.")

if __name__ == "__main__":
    main()
