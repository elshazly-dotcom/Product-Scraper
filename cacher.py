import json
import jsonScraper

def extract_product(product):
    vIDtoColor = {}

    for i, option in enumerate(product["options"]):
                if option["name"] == "Color":
                    colorPosition = i + 1
                    colorOption = option
                elif option["name"] == "Size":
                    sizePosition = i + 1

    for variant in product["variants"]:
        vID = variant["id"]
        color = variant[f"option{colorPosition}"]
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

        matchingImages = []
        for img in product["images"]:
           if not img["variant_ids"]:
                matchingImages.append(img["src"])
           else:
               for vId in img["variant_ids"]:
                if vId in matchingVariantsIds:
                    matchingImages.append(img["src"])
                    break

        resultColors.append({
            "color": color,
            "sizes": sizes,
            "images": matchingImages
        })


    return{
        "id": product["id"],
        "title": product["title"],
        "colors": resultColors
    }     
             
def main():
    name = jsonScraper.name
    with open (f"{name}.json", "r") as f:
        data = json.load(f)
        product1 = data["products"][0]
        print(extract_product(product1))

main()