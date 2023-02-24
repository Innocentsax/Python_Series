import webbrowser


def chrome_automation():

    web_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

    urls = (
        "https://www.google.com",
        "https://intranet.alxswe.com",
        "https://www.youtube.com",
        "https://github.com/Innocentsax"
    )

    for url in urls:

        print("opening " + url)
        webbrowser.get(web_path).open(url)

chrome_automation()
