import pyshorteners as pys

url = input("Enter URL: ")

shortener = pys.Shortener().tinyurl.short(url)

print(f"The shorten URL: {shortener}")
