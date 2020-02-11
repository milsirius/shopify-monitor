from shopify import ShopifyStore

s = ShopifyStore("undefeated", "https://undefeated.com/", "collections/footwear/")
s.scrap()
s.save()
