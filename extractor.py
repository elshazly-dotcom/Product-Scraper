import json
#import jsonScraper

def extract_product(product):
    vIDtoColor = {}
    colorPosition = 0
    sizePosition = 0
    colorOption = None
    for i, option in enumerate(product["options"]):
                if option["name"] == "Color":
                    colorPosition = i + 1
                    colorOption = option
                elif option["name"] == "Size":
                    sizePosition = i + 1


    if colorOption == None:
        sizes=[]
        for i in product["variants"]:
            sizes.append({
                "size": i[f"option{sizePosition}"],
                "price": i["price"],
                "compare_at_price": i["compare_at_price"],
                "available": i["available"]
            })

        Images = []
        for img in product["images"]:
            Images.append(img["src"])

        return{
            "id": product["id"],
            "title": product["title"],
            "colors": None,
            "sizes": sizes,
            "images": Images
        }

    for variant in product["variants"]:
        if colorPosition:   
            color = variant[f"option{colorPosition}"]
        vID = variant["id"]
        vIDtoColor[vID] = color

    colors = colorOption["values"]

    resultColors = []

    for color in colors:
        matchingVariants = []
        for i in product["variants"]:
            if vIDtoColor[i["id"]] == color:
                matchingVariants.append(i)

        sizes=[]
        matchingVariantsIds = []
        for j in matchingVariants:
            matchingVariantsIds.append(j["id"])
            sizes.append({
                "size": j[f"option{sizePosition}"],
                "price": j["price"],
                "compare_at_price": j["compare_at_price"],
                "available": j["available"]
            })

        Images = []
        for img in product["images"]:
           if not img["variant_ids"]:
                continue
           else:
               for vId in img["variant_ids"]:
                if vId in matchingVariantsIds:
                    Images.append(img["src"])
                    break

        resultColors.append({
            "color": color,
            "sizes": sizes,
            "images": Images
        })


    return{
        "id": product["id"],
        "title": product["title"],
        "colors": resultColors
    }     
             
def main():
    #name = jsonScraper.name
    with open ("nothingRAW.json", "r") as f:
        data = json.load(f)

    with open ("nothing.json", "w") as f:
        products = []
        for product in data["products"]:
            products.append(extract_product(product))
        json.dump(products, f, indent=4)
    
main()