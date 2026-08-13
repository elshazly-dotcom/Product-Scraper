import json
import jsonScraper

def extract_product(product):
    colorPosition = None
    sizePosition = None
    
    # 1. Identify option positions for Color and Size
    for i, option in enumerate(product["options"]):
        name = option["name"].lower()
        if name in ["color", "colour"]:
            colorPosition = i + 1
        elif name == "size":
            sizePosition = i + 1

    colors = {}
    colorVIDs = {}

    # 2. Group all variants by their respective color
    for variant in product["variants"]:
        color_val = variant[f"option{colorPosition}"] if colorPosition else "Default"
        size_val = variant[f"option{sizePosition}"] if sizePosition else "One Size"
        
        if not color_val: color_val = "Default"
        if not size_val: size_val = "One Size"

        if color_val not in colors:
            colors[color_val] = []
            colorVIDs[color_val] = []

        colors[color_val].append({
            "size": size_val,
            "price": variant["price"],
            "compare_at_price": variant["compare_at_price"],
            "available": variant["available"]
        })
        
        colorVIDs[color_val].append(variant["id"])

    # 3. Match product images to the correct color group using variant IDs
    # 3. Match product images to the correct color group using variant IDs
    result_colors = []

    # If this product never tags any image with variant_ids, treat all images as shared across colors
    any_tagged = any(img["variant_ids"] for img in product["images"])

    for color_val, sizes in colors.items():
        images = []

        for img in product["images"]:
            if colorPosition and color_val != "Default" and any_tagged:
                if img["variant_ids"]:
                    for v_id in img["variant_ids"]:
                        if v_id in colorVIDs[color_val]:
                            images.append(img["src"])
                            break
            else:
                images.append(img["src"])

        result_colors.append({
            "color": color_val,
            "images": images,
            "sizes": sizes 
        })

    # 4. Return unified product structure
    return {
        "id": product["id"],
        "title": product["title"], 
        "colors": result_colors
    }     
             
def main():
    name = jsonScraper.name
    
    with open (f"{name}RAW.json", "r") as f:
        data = json.load(f)

    with open (f"{name}.json", "w") as f:
        products = []
        for product in data["products"]:
            products.append(extract_product(product))
            
        json.dump(products, f, indent=4)
    
main()