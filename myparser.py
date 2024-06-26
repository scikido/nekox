import time
import os
from llmware.setup import Setup
from llmware.library import Library
from llmware.retrieval import Query
import re
import json

input_fp = r"C:\Users\DELL\Downloads\Logithon - NekoX\docs"
output_fp = r"new_outputs"

def parsing_with_docs(filename):
    t0 = time.time()

    lib = Library().create_new_library(filename)

    parsing_output = lib.add_files(input_folder_path=input_fp)

    print("update: parsing time - ", time.time() - t0)
    print("update: parsing_output - ", parsing_output)

    output1 = lib.export_library_to_jsonl_file(output_fp, filename)

    output2 = Query(lib).export_all_tables(query="",output_fp=output_fp)

    return 0

def getting_text(path):
    with open(path,'r') as file:
        text = r"" + file.read()
        pattern = "{.*}"
        matches = re.findall(pattern, text)
        store = ""
        for match in matches:
            file = json.loads(match, strict=False)
            print(file['text_search'])
            store += file['text_search']
        return store
    

# q = parsing_with_docs()
# p = parse_using_llama(r"C:\Users\DELL\Downloads\table extract\pdf_tables\new_output.jsonl")
# print(p)


"""This 'Getting Started' example demonstrates how to parse document files into a library
      1. Create a library
      2. Assemble input files into a single folder path (fp)
      3. Pass the folder path to library.add_files(fp) to automatically parse, text chunk, index
"""




def parsing_documents_into_library(library_name):

    print(f"\nExample - Parsing Files into Library")

    #   create new library
    print (f"\nStep 1 - creating library {library_name}")
    library = Library().create_new_library(library_name)

    #   load the llmware sample files
    #   -- note: if you have used this example previously, UN-Resolutions-500 is new path
    #   -- to pull updated sample files, set: 'over_write=True'

    # sample_files_path = Setup().load_sample_files(over_write=False)
    # print (f"Step 2 - loading the llmware sample files and saving at: {sample_files_path}")

    #   note: to replace with your own documents, just point to a local folder path with the documents
    ingestion_folder_path = "docs"

    print (f"Step 3 - parsing and indexing files from {ingestion_folder_path}")

    #   add files is the key ingestion method - parses, text chunks and indexes all files in folder
    #       --will automatically route to correct parser based on file extension
    #       --supported file extensions:  .pdf, .pptx, .docx, .xlsx, .csv, .md, .txt, .json, .wav, and .zip, .jpg, .png

    parsing_output = library.add_files(ingestion_folder_path)

    print (f"Step 4 - completed parsing - {parsing_output}")

    #   check the updated library card
    updated_library_card = library.get_library_card()
    doc_count = updated_library_card["documents"]
    block_count = updated_library_card["blocks"]
    print(f"Step 5 - updated library card - documents - {doc_count} - blocks - {block_count} - {updated_library_card}")

    #   check the main folder structure created for the library - check /images to find extracted images
    library_path = library.library_main_path
    print(f"Step 6 - library artifacts - including extracted images - saved at folder path - {library_path}")

    return parsing_output



    