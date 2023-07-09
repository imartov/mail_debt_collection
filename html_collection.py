import base64


def html_collection() -> None:

    files = ["static_base64\\styles.html",
             "static_base64\\logo.html",
             "static_base64\\email_template.html",
             "static_base64\\footer-inst.html",
             "static_base64\\footer-link.html",
             "static_base64\\footer-site.html"]
    
    outpute_html_content = ''
    for file in files:
        
        if file in ["static_base64\\logo.html", "static_base64\\footer-inst.html", "static_base64\\footer-link.html", "static_base64\\footer-site.html"]:
            print(file)
            if file == "static_base64\\logo.html":
                path_pic = "static_base64\\images\\corporate-logo.png"
            elif file == "static_base64\\footer-inst.html":
                path_pic = "static_base64\\images\\instagram-icon.png"
            elif file == "static_base64\\footer-link.html":
                path_pic = "static_base64\\images\\linkedin-icon.png"
            elif file == "static_base64\\footer-site.html":
                path_pic = "static_base64\\images\\site-icon.png"

            data = open(path_pic, 'rb').read()
            data_base64 = base64.b64encode(data)
            data_base64 = data_base64.decode()

            replace_html = ' src="data:image/jpeg;base64,' + data_base64 + ''
            with open(file, "r", encoding="utf-8") as file_html:
                html_content = file_html.read().format(replace_html=replace_html)
            outpute_html_content += str(html_content)
        
        else:
            with open(file, "r", encoding="utf-8") as file_html:
                html_content = file_html.read()
            outpute_html_content += str(html_content)

    with open("static_base64\\output.html", "w") as file:
        file.write(outpute_html_content)


if __name__ == "__main__":
    html_collection()