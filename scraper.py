from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

url = "https://www.kijiji.ca/b-cell-phone/gta-greater-toronto-area/c760l1700272?uli=true&ad=offering&price=50__500"

# opening up connection, grabbing the page
content = uReq(url)

# puts content in a variable
page_html = content.read()

# close the connection
content.close()

# putting info in an html file
page_soup = bs(page_html, "html.parser")

# print(page_soup.findAll("div", {"class": "regular-ad"}))
containers = page_soup.findAll("div", {"class": "regular-ad"})

# file to be saved in

filename = "products.csv"
f = open(filename, "w")

headers = "title, price\n"
f.write(headers)

for container in containers:
    # print(container.findAll("div", {"class": "price"}))
    # print(container.findAll("div", {"class": "title"}))

    title_container = container.findAll("div", {"class": "title"})
    price_container = container.findAll("div", {"class": "price"})

    product_name = title_container[0].text.strip()  # stripping any white space
    price = price_container[0].text.strip()

    # print(product_name + price)
    # print("\n")

    f.write(product_name.replace(",", "|") + ", " + price + "\n")

f.close()