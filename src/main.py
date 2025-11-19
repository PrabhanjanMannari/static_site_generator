from utils import * 

refresh_util("static/", "public/")
generate_pages_recursive("content/", "template.html", "public/")


