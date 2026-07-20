import json
import csv


with open ("nothing-personal.json", "r") as f:
    data = json.load(f)
    for i, product in enumerate(data["products"]):
        print(f"PRODUCT NUMBER {i}")

        productName = product["title"]
        print(f"Name: {productName}")
        
        productType = product["product_type"]
        print(f"Type: {productType}")

        sizes = []
        for variant in product["variants"]:
            sizes.append(variant["title"])
        
        print(f"Sizes: {sizes}")

        price = variant["price"]
        print(f"Price: {price}")

        imgs = []
        for i, img in enumerate(product["images"]):
            imgs.append(img["src"])

        print(f"Imgs: {imgs}")
        print()
    