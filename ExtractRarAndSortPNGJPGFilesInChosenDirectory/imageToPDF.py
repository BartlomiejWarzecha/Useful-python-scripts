
import os
import glob
import webbrowser

from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
def run():
    # Get the PDF file name from user input

    pdf_name = input("Enter PDF file name: "  + "\n")

    default_img_dir = "default path is empty - change default path in script file"
    

    # Set the directory containing the PNG and JPG files
    img_dir = input("Enter image directory path (press enter to use default directory): " + "\n"
                    + default_img_dir  + "\n")
    if img_dir == "":
        # If no image directory is provided, use the default directory
        img_dir = default_img_dir
        print("Chosen Default IMG Directory:" + "\n" + img_dir);
    else:
        # Make sure the provided directory exists
        if not os.path.exists(img_dir):
            print("Image directory does not exist!")
            exit()

    # Get the start and end prefixes from user input
    start_prefix = input("Enter start prefix (e.g. '080'): "  + "\n")
    end_prefix = input("Enter end prefix (e.g. '110'): "  + "\n")

    # Get a list of image files in the directory
    img_files = sorted(glob.glob(os.path.join(img_dir, '*.*')))

    # Find the index of the first file with the start prefix
    start_index = next((i for i, file in enumerate(img_files) if os.path.basename(file).startswith(start_prefix)), None)

    # Find the index of the first file with the end prefix
    end_index = next((i for i, file in enumerate(img_files) if os.path.basename(file).startswith(end_prefix)), None)

    # Select all files between the start and end indexes
    chosen_img_files = img_files[start_index:end_index]
    chosenFilesNumber = len(chosen_img_files)

    print("Found " + str(chosenFilesNumber) + " files")

    default_output_dir = 'C:\\Users\\Justyna\\Downloads\\ChomikBox\\Arcs'

    # Get the output directory from user input
    output_dir = input("Enter output directory path (press enter to use default directory):" + "\n"
                    + default_output_dir )
    if output_dir == "":
        # If no output directory is provided, use the default directory
        output_dir = default_output_dir
        print("Chosen Output Default Directory:" + "\n" + output_dir + "\\" + pdf_name);
    else:
        # Make sure the provided directory existss
        if not os.path.exists(output_dir):
            print("Output directory does not exist!")
            exit()

    # Combine the output directory and PDF file name to create the output path
    output_path = os.path.join(output_dir, pdf_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Create a new PDF file
    pdf_file = canvas.Canvas(os.path.join(output_path, pdf_name + '.pdf'), pagesize=letter)

    # Loop over each image file and add it to the PDF
    for img_file in chosen_img_files:
        # Open the image file with Pillow
        image = Image.open(img_file)

        # Get the dimensions of the image
        width, height = image.size

        # Add the image to the PDF file
        pdf_file.setPageSize((width, height))
        pdf_file.drawImage(img_file, 0, 0, width, height)

        # Add a new page to the PDF file
        pdf_file.showPage()
        print("page: " + img_file + " added")

    # Save the PDF file
    pdf_file.save()
    print("pdf file saved")

    pdf_path = os.path.join(output_path, pdf_name + '.pdf')

    print("Running " + pdf_path + " in Chrome browser")
    webbrowser.open('file://' + os.path.realpath(pdf_path))



if __name__ == "__main__":
    run()
