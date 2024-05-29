import os
import json
from pyresparser import ResumeParser

path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path, 'resume1.pdf')
data = ResumeParser(file_path).get_extracted_data()

print(json.dumps(data, indent=2))