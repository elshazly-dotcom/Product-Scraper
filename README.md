#Shopify Product Scraper

A python script to grab product names, prices, sizes, colorways, images, and more from shopify stores through the use of there public /products.json API endpoint. The program handles shopify API pagination and rate limitations for you and produces output in an extremely clean and easily readable JSON output, cleverly chunking product images and variants into corresponding colors.

This program was developed as the initial phase of a product-collection project the aim of which is to produce a browse-only, local-brand index website.

Features

* Avoid Network Errors & Rate Limits Bypasses rate limitations for shopify by rotating http headers, making use of fake-useragent library, along with implementing slow sleep intervals to the script's fetching logic.
* Iterate Through all Product Pages The scraper automatically parses shopify API pagination and loops through all the different product pages available until all of a store's inventory is exhausted.
* Consolidated & Smart Variants Parses the complex shopify API responses to successfully group variantIDs and correctly tie them into their respective colorway descriptions. It’s able to properly map a specific image url and color/size data to the variant directly from the API data.
* Light-weight JSON output Transform messy/complex shopify api data to an extremely light-weight JSON file for use on a web interface without unnecessary data.

Prerequisites

A python 3.x version needs to be installed to the system and can be accessed locally. All of the necessary required libraries have been listed below; they should be easily obtained in any local development environment.

Install the necessary requirements using pip. These should then install with no issues:

pip install requests fake-useragent

(This would normally suggest a requirements.txt file, and indeed for an in-depth repository of this script: it would also require one. However, we avoid this for an exceptionally short, clean and to-the-point code-repo!)

How To Use

1. Download this code-base by running it against this github repo:

git clone https://github.com/elshazly-dotcom/Product-Scraper.git

cd Product-Scraper

2. Run the script as follows:

python extractor.py

3. You will be prompted with two questions and two text fields to input in:
 * Enter URL Paste the target url of either shopify store OR particular shopify collection. I.e. Https://store.co 
 * Name of file You can write whatever name(e.g. Local-brands) you want, as a prefix for all your output files. I.e. A products.json` from a store called "Apple" in Appleproducts.com , would now show up as the output of "appleproducts.comproducts.json"

Output File Generation

Upon completion, 3 files will be generated within the same folder as the script, these are as follows ( where [name] is specified in previous instructions:):

* [name]RAW.json Raw output of ALL the shopify api product calls
* [name]_meta.json An overview regarding the HTTP calls made during the process (HTTP status, success state, number of pages extracted...)
* [name].json Cleaned, and organised data of your requested information, separated by color, size, and product-image relationships.

Roadmap of the project:

This scrapper is version 1 and the initial step of a bigger initiative whose end objective is to provide the local brands products to users in a clean, browsable interface. This will eliminate the need for the customers, to check multiple individual stores to view and compare the products offered, and would result in a greatly optimized consumer buying process for local products.
