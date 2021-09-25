
def image_url_split(link):
    link = link.strip("https://drive.google.com/file/d/").strip("/view?usp=sharing")
    return "https://drive.google.com/uc?id=" + link
