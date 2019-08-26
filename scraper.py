from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from item import Item
import searcher as searcher

# number of pages to look into
page_num = "1"
age = 30


def scraper(item, min_price, max_price):
    # url = "https://www.kijiji.ca/b-cell-phone/gta-greater-toronto-area/c760l1700272?uli=true&ad=offering&price
    # =50__500"

    url = searcher.url_generator(item, min_price,  max_price, page_num)

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

    # filename = "products.csv"
    # f = open(filename, "w")

    # headers = "title, price\n"
    # f.write(headers)

    items = []
    for container in containers:
        # print(container.findAll("div", {"class": "price"}))
        # print(container.findAll("div", {"class": "title"}))

        title_container = container.findAll("div", {"class": "title"})
        price_container = container.findAll("div", {"class": "price"})
        date_container = container.findAll("div", {"class": "location"})
        description_container = container.findAll("div", {"class": "description"})

        date = date_container[0].span
        product_name = title_container[0].text.strip()  # stripping any white space
        price = price_container[0].text.strip()
        description = description_container[0].text.strip()
        url = ""

        for a in title_container:
            url = "www.kijiji.ca/v-search/v-search/" + (a.a['href'])[-10:]

        if date:
            date = date.text.strip()
            if "minute" in date:
                if int(''.join(filter(str.isdigit, date))) < 60:
                    #                print(date)
                    product = Item(product_name, price, date, description, url)
                    items.append(product)

        # print(product_name + price)
        # print("\n")

        # f.write(product_name.replace(",", "|") + ", " + price + "\n")

        # f.close()

    # for object in items:
    #   print(object.title)
    #   print(object.price)
    #   print(object.date)
    #   print(object.description)
    #   print(object.url)
    #   print("\n")

    return items
