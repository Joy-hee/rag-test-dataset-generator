import pdfplumber
from pdf2image import convert_from_path
import os
import json

# Function to extract images and charts from PDF pages

def extract_images_and_charts(pdf_path, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    metadata = []

    # Use pdfplumber to open the PDF
    with pdfplumber.open(pdf_path) as pdf:
        for page_number in range(len(pdf.pages)):
            page = pdf.pages[page_number]
            # Extract images from the page
            images = page.images
            for img_index, img in enumerate(images):
                # Get the image's coordinates
                x0, top, x1, bottom = img['x0'], img['top'], img['x1'], img['bottom']
                # Extract the image
                img_data = page.to_image().crop((x0, top, x1, bottom))
                img_filename = os.path.join(output_folder, f'image_page_{page_number+1}_{img_index+1}.png')
                img_data.save(img_filename)
                # Store metadata
                metadata.append({'page': page_number + 1, 'location': {'x0': x0, 'top': top, 'x1': x1, 'bottom': bottom}, 'filename': img_filename})

    # Convert PDF pages to images and save them
    converted_images = convert_from_path(pdf_path)
    for img_index, image in enumerate(converted_images):
        img_filename = os.path.join(output_folder, f'page_{img_index+1}.png')
        image.save(img_filename)

    # Save the metadata to a JSON file
    with open(os.path.join(output_folder, 'metadata.json'), 'w') as json_file:
        json.dump(metadata, json_file, indent=4)

# Example usage
# extract_images_and_charts('example.pdf', 'output_folder')
