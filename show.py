# we need to create streamlit app that will present all the pdfs in the pdfs folder and allow the user to select and view one of them
import base64

import streamlit as st
import os

from PyPDF2 import PdfReader
from pdf2image import convert_from_path

# Get the current working directory
cwd = os.getcwd()
# Get the path to the pdfs folder
pdfs_path = os.path.join(cwd, 'pdfs')

# Get the list of files in the pdfs folder
files = os.listdir(pdfs_path)

# I want to set this as a list with file names as the values and downloadable file links as the labels
file_list = []
for file in files:
    if file.endswith('.pdf'):
        file_list.append(file)

# create a layout to show pdf files in the pdfs folder, every file has a thumbnail of first page and when you cick on it it opens in new page
# create a layout to show pdf files in the pdfs folder, every file has a thumbnail of first page and when you cick on it it opens in new page

# Initialize an empty dictionary to store pdf names and thumbnail locations
pdf_thumbnail_dict = {}

# for filename in os.listdir(pdfs_path):
#     if filename.endswith('.pdf'):
#         # Create a PDF file reader object
#         pdf_path = os.path.join(pdfs_path, filename)
#         pdf = PdfReader(pdf_path)
#
#         # If pdf has pages
#         if len(pdf.pages) > 0:
#             # Convert first page to image
#             images = convert_from_path(pdf_path, first_page=1, last_page=1)
#
#             # If conversion is successful and we have an image
#             if images:
#                 # Save the first page as an image (thumbnail)
#                 thumbnail_path = os.path.join(pdfs_path, f"{filename}_thumbnail.jpg")
#                 images[0].save(thumbnail_path, 'JPEG')
#
#                 # Add to dictionary
#                 pdf_thumbnail_dict[filename] = thumbnail_path
def main():

    st.title("ZOI84 TENDERSKE ODLUKE")
    st.write("Ovo je lista svih tenderskih odluka koje su objavljene od strane javnog preduzeca ZOI84 na jednom mjestu u 2020.")
    st.write("Izaberite odluku koju zelite pogledati.")

    # Create a dropdown menu of the files in the pdfs folder
    selected_file = st.selectbox("Select a PDF file", file_list)

    # Get the path to the selected file
    path_to_file = os.path.join(pdfs_path, selected_file)

    # Display the selected file
    container = st.container()

    # for file in files:
    #     if file.endswith('.pdf'):
    #         # Create a PDF file reader object
    #         with open(os.path.join(pdfs_path, file), "rb") as f:
    #             base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    #             pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    #             container.markdown(pdf_display, unsafe_allow_html=True)


    view_pdf(path_to_file)

    # pdf_layout_with_thumbnails(selected_file)

def view_pdf(pdfLocation):
    with open(pdfLocation, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_layout_with_thumbnails(selected_file):
    # use pdf_thumbnail_dict to create a layout to show pdf files in the pdfs folder, every file has a thumbnail of first page and when you cick on it it opens in new page
    st.title("ZOI84 TENDERSKE ODLUKE")
    st.write("Ovo je lista svih tenderskih odluka koje su objavljene od strane javnog preduzeca ZOI84 na jednom mjestu u 2020.")
    st.write("Izaberite odluku koju zelite pogledati.")

    container = st.container()
    # for(pdf, thumbnail) in pdf_thumbnail_dict.items():
    #     container.image(thumbnail)
    #     container.write(pdf)
    #     container.button("View PDF")

    # container.image(pdf_thumbnail_dict[selected_file])
    container.write(selected_file)
    container.button("View PDF")


if __name__ == "__main__":
    main()
