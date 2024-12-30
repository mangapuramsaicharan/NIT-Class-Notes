import os
import re
import string
import unicodedata
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Set working directory to the folder where the XML file is located
os.chdir(r"C:\Users\manga\Desktop\NIT Class Notes\Assignments")

# Parse the XML file
tree = ET.parse('769952.xml')
root = tree.getroot()

# Convert XML to string
root_str = ET.tostring(root, encoding='utf8').decode('utf8')

# Define functions
def strip_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()  # Call the method

def remove_between_square_brackets(text):
    return re.sub(r'\[[^]]*\]', '', text)  # Corrected regex pattern

# Test the functions
text_without_html = strip_html(root_str)
text_cleaned = remove_between_square_brackets(text_without_html)

# Output the cleaned text
print(text_cleaned)

                  
                  