import bs4
import requests as req
from notify_run import Notify
from datetime import datetime
import time

conn = req.get("https://www.amazon.in/gp/offer-listing/B07ZPM2BVR/ref=dp_olp_new_mbc?ie=UTF8&condition=new")
soup = bs4.BeautifulSoup(conn.text,features="html.parser")
allCostElems = soup.findAll(attrs={'class' : 'a-size-large a-color-price olpOfferPrice a-text-bold'})
prodHead = soup.findAll(attrs={'class' : 'a-size-large a-spacing-none'})[0].text.split("\n")[1].strip()

allCosts = []
notify = Notify()

while (True):
    try:
        for costElement in allCostElems:
            cost = (float)(costElement.text.strip("Rs. ").strip("\xa0").split("Rs. ")[1].replace(",",""))
            allCosts.append(cost)
            allCosts.sort()
            print ("lowest cost : " + str(allCosts[0]))
            
            if (cost < 20500.0):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                notify.send("Price alert! Time: " + timestamp + " Price: " + str(cost)
                            + " | " + prodHead)
            time.sleep(600)

    except KeyboardInterrupt:
        print ("Interrupted.")
        break

    except Exception as e:
        print (e)