import os
from PyPDF2 import PdfMerger

def merge_pdfs_in_folder(folder_path, output_file):
    """
    Merges all PDF files in the specified folder into a single PDF.

    :param folder_path: Path to the folder containing PDF files.
    :param output_file: Name of the output merged PDF file.
    """
    # Initialize the PdfMerger object
    merger = PdfMerger()

    # Get all PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # Sort the files to maintain order (optional)
    pdf_files.sort()

    # Add each PDF file to the merger
    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        print(f"Adding: {pdf_path}")
        merger.append(pdf_path)

    # Write the merged PDF to the output file
    output_path = os.path.join(folder_path, output_file)
    merger.write(output_path)
    merger.close()

    print(f"Merged PDF saved as: {output_path}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing PDFs: ").strip()
    output_file = input("Enter the name for the output PDF (e.g., merged.pdf): ").strip()

    if not output_file.endswith('.pdf'):
        output_file += '.pdf'

    if os.path.isdir(folder_path):
        merge_pdfs_in_folder(folder_path, output_file)
    else:
        print("Invalid folder path. Please try again.")
