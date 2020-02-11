import json
import requests

import arrow

import randomheaders
import randomproxies


class ShopifyStore:
    """
    A class used to represent a Shopify Store and allows the monitoring of sneakers.
    ...
    Attributes
    ----------
    name : str
        The name of the store
    blink : str
        The link to access the sneaker collection to the store
    filespath : str
        The relative path to the file where the product logs will be saved
    variants : array of product Variants
        Array of the class Variant to store the variants of the products from the website

    Methods
    -------
    scrap()
        Scraps all the products of the store
    save()
        Saves the array self.variants into json files stored on self.filespath
    """
    def __init__(self, name, link, ext=""):
        """
        Parameters
        ----------
        name : str
            The name of the store
        link : str
            The link to access the store
        ext : str, optional
            The link extension to get to the shoe collection in the store (by default there isn't)
        """

        self.name = name
        self.blink = link + ext
        self.file = "{}.json".format(self.name)
        self.products = []

    def scrap(self):
        """ Scraps the full product list of the store
        Parameters (None)
        ----------
        """
        print("starting scraping")

        self.link = self.blink + "products.json?limit=240"
        print(self.link)
        if self.__scrap(240):
            self.page = 9
            self.link = self.blink + "products.json?page={}".format(str(self.page)) 
            while self.__scrap(30):
                self.page += 1
                self.link = self.blink + "products.json?page={}".format(str(self.page)) 

    def __scrap(self, items):
        """ Scraps a page of the store
        Parameters
        -----------------
        items : int
            The number of products wanted for a successfull scrape
        Returns
        -------
        True: if has scraped the variants of the number of items wanted
        False: otherwise
        """

        #proxies = randomproxies.getProxie()
        headers = randomheaders.getHeader()

        #afegir proxies quan tornin a funcionar
        r = requests.get(self.link,  headers=headers)
        print(r)
        products = json.loads(r.text)['products']

        for product in products:
            self.products.append(product)
    
        print(self.link)

        return (len(products) == items)

    def save(self):
        """ Saves the variants on self.variants
        Parameters (None)
        -----------------
        Returns
        -------
        int : with the number of files created or updated
        """
        f = open(self.file, 'w')
        json.dump(self.products, f)

        return len(self.products)

        
        
        

