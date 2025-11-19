import sys 
from utils import * 

base_path: str = "/"

if (len(sys.argv) >= 2):
    base_path = sys.argv[1]

refresh_util("static/", "docs/")
generate_pages_recursive("content/", "template.html", "docs/", base_path)


