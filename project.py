import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import schedule
import time

account_sid = 'AC1738e30268f9a6dea86527188efa9710'
auth_token = '87ecea3c67f63eff92bcc709116bbdf4'
client = Client(account_sid, auth_token)


#URL = 'https://www.amazon.in/Test-A6010-Dummy-Asin_42/dp/B07X4R4F4G/ref=sr_1_omk_2?dchild=1&keywords=mobiles&qid=1624004584&sr=8-2'
products_to_track = [
    {
        "Product_url":"https://www.amazon.in/Test-A6010-Dummy-Asin_42/dp/B07X4R4F4G/ref=sr_1_omk_2?dchild=1&keywords=mobiles&qid=1624004584&sr=8-2",
        "name":"1st ",

        "target_price" : 54000
    },
    {
        "Product_url":"https://www.amazon.in/Redmi-Sky-Blue-64GB-Storage/dp/B08697N43N/ref=sr_1_1?dchild=1&keywords=mobiles&qid=1624004584&sr=8-1",
        "name":"2nd ",
        "target_price" : 8800
    },
    {
        "Product_url":"https://www.amazon.in/Oppo-Fantasy-Storage-Additional-Exchange/dp/B08444SXZ6/ref=sr_1_3?dchild=1&keywords=mobiles&qid=1624004584&sr=8-3",
        "name":"3nd ",
         "target_price" : 11000
    },
    {
        "Product_url":"https://www.amazon.in/Redmi-9A-2GB-32GB-Storage/dp/B08696XB4B/ref=sr_1_4?dchild=1&keywords=mobiles&qid=1624027901&sr=8-4",
        "name":"4th",
        "target_price" :6800
    },
{
        "Product_url":"https://www.amazon.in/Samsung-Metallic-Storage-Additional-Exchange/dp/B086KCCSDD/ref=sr_1_6?dchild=1&keywords=mobiles&qid=1624027901&sr=8-6",
        "name":"5th",
        "target_price" :9000
    }

]
def do_nothing():
    try:
        for every_product in products_to_track:

            product_price_returned = give_product_price(every_product.get("Product_url"))

            print(product_price_returned + "---" + every_product.get("name"))

            my_product_price = product_price_returned[2:]
            my_product_price = my_product_price.replace(',', '')
            my_product_price = float(my_product_price)
            print(my_product_price)

            if my_product_price < every_product.get("target_price"):
                client.messages.create(
                    body='you can buy this product now',
                    from_="+12532367018",
                    to="+918792323574"

                )
                print("Availabel to buy this product")
                my_result.write(every_product.get(
                    "name") + "----------\t" +
                                "available at the target price\t" + "current product price\t" + str(
                    my_product_price) + "\n")
            else:
                print("Product is not availabel to ur amount")




    finally:
        my_result.close()



def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    # print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    product_price = soup.find(id="priceblock_ourprice")

    if (product_price == None):
        product_price = soup.find(id='priceblock_dealprice')
    return product_price.get_text()
    #print(product_price.get_text())

my_result = open('my_output.txt','w')

schedule.every().day.at("20:26").do(do_nothing)
while 1:
    schedule.run_pending()
    time.sleep(1)




# Download the helper library from https://www.twilio.com/docs/python/install



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure








