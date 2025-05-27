from flask import Flask, render_template, request, redirect

app = Flask(__name__)

regalos = [
    {"nombre": "Termichy Stackable Formula Dispenser Portable Milk Powder Container, 2 Pack, Grey", "link": "https://www.amazon.com/dp/B09V277ZRJ", "reservado_por": None},
    {"nombre": "Baby Jolie Memory for Babies, Alcohol Free Cologne", "link": "https://www.amazon.com/dp/B07HHJ3K5W", "reservado_por": None},
    {"nombre": "Baby Jolie Le Bebe Kids Perfume with Flower and Fruits Scent ", "link": "https://www.amazon.com/dp/B00RIC9EUK", "reservado_por": None},
    {"nombre": "XMWEALTHY Newborn Baby Wrap Swaddle Blanket Knit Sleeping Bag ", "link": "https://www.amazon.com/dp/B01N2NADKZ", "reservado_por": None},
    {"nombre": "Aablexema Baby Cotton Fooltess Pajamas with Mitten, 3-packt", "link": "https://www.amazon.com/dp/B0CSNJGY8R", "reservado_por": None},
    {"nombre": "Simple Joys by Carter's Baby 3-Pack Neutral Sleep and Play", "link": "https://www.amazon.com/dp/B075YZ1963", "reservado_por": None},
    {"nombre": "Mustela Newborn Arrival Gift Set - Baby Skincare & Bath Time Essentials", "link": "https://www.amazon.com/dp/B01NA7ZMIA", "reservado_por": None},
    {"nombre": "Aquaphor Baby Skincare Essentials Gift Set with Baby Wash and Shampoo", "link": "https://www.amazon.com/dp/B0CLHDBYR9", "reservado_por": None},
    {"nombre": "Baby Wet Wipes Dispenser and Diaper Wipe Warmer with Night Light,Temperature", "link": "https://www.amazon.com/dp/B08JYJKZNL", "reservado_por": None},
    {"nombre": "Dr. Brown's Natural Flow Anti-Colic Options+ Narrow Glass Baby Bottle 4", "link": "https://www.amazon.com/dp/B0F54RF5BZ", "reservado_por": None},
    {"nombre": "WaterWipes Plastic-Free Original Baby Wipes, 99.9% Water Based Wipes", "link": "https://www.amazon.com/dp/B008KJEYLO", "reservado_por": None},
    {"nombre": "Lictin Baby Hair Brush and Comb Set, 4 Pcs Newborn Hair Brush with Soft Bristle", "link": "https://www.amazon.com/dp/B0D12Q1FH9", "reservado_por": None},
    {"nombre": "5-Pack Muslin Burp Cloths Baby Boy, Girl - Very Absorbent Baby Burp Cloth Rags", "link": "https://www.amazon.com/dp/B0CC99GX75", "reservado_por": None},
    {"nombre": "rida Baby Control The Flow Bathtub Sprayer Attachment for Baby Bathtub", "link": "https://www.amazon.com/dp/B0DXXH3S2P", "reservado_por": None},
    {"nombre": "Diaper Bag Backpack Baby Diaper Bag Leather with 17 Diaper Bag Organizing Pouches", "link": "https://www.amazon.com/dp/B0BLBM99XG", "reservado_por": None},
    {"nombre": "GROWNSY Nasal Aspirator for Baby, Electric Baby Nose Sucker", "link": "https://www.amazon.com/dp/B08CMWHD3B", "reservado_por": None},
    {"nombre": "Momcozy Baby Carrier - Ergonomic, Cozy and Lightweight Carrier for 7-44lbs", "link": "https://www.amazon.com/dp/B0CDQ1ZLJ9", "reservado_por": None},
    {"nombre": "THERMOS Stainless King Vacuum-Insulated Beverage Bottle, 40 Ounce, Matte Stainless Steel", "link": "https://www.amazon.com/dp/B01DZQT3IU", "reservado_por": None},
    {"nombre": "Baby Sensory Toy 0-6 Month Music Animal Stuffed Plush Caterpillar Toy for Infant 0-3-6 Month", "link": "https://www.amazon.com/dp/B0CDWW374H", "reservado_por": None},
    {"nombre": "Smart Video Baby Monitor with Camera and Audio,Dual Mode,WiFi On/Off t", "link": "https://www.amazon.com/dp/B0CZHFQNYY", "reservado_por": None},
    {"nombre": "Baby Walker with Wheels, 5 in 1 Baby Walkers for Boys Girls 6-12 Months", "link": "https://www.amazon.com/dp/B0DS19ZLNZ", "reservado_por": None},
    {"nombre": "Lilian&Gema Baby Healthcare and Grooming Kit, 28-in-1 Rechargeable Nail Trimmer Electric Set", "link": "https://www.amazon.com/dp/B0DPCJ2R24", "reservado_por": None},
    {"nombre": "4 Pcs Fleece 30 x 40  Fluffy Baby Blanket for Boys Nursery Little Girl Infant or Newborn", "link": "https://www.amazon.com/dp/B0CY2Q2C4P", "reservado_por": None},
    {"nombre": "SWEET DOLPHIN Baby Sleep Sack 0-6 Months ", "link": "https://www.amazon.com/dp/B0DPKWG3PN", "reservado_por": None},
    {"nombre": "Nursing Pillow and Positioner, Breastfeeding, Bottle Feeding", "link": "https://www.amazon.com/dp/B09H6XX51K", "reservado_por": None},
    {"nombre": "NutriBullet NBY-50100 Baby Complete Food-Making System, 32-Oz, White, Blue, Clear", "link": "https://www.amazon.com/dp/B086DFCS7Y", "reservado_por": None},
    {"nombre": "nutribullet Baby BSR-0801N Turbo Food Steamer", "link": "https://www.amazon.com/dp/B006SODTTQ", "reservado_por": None},
    {"nombre": "No-Touch Forehead Thermometer for Adults and Kids, Fast Accurate Baby Thermometer", "link": "https://www.amazon.com/dp/B0CKW3K16P", "reservado_por": None},
    {"nombre": "Bottle Sterilizer and Dryer, HIYAKOI Electric Steam Baby Bottle Sterilizer and Dryer", "link": "https://www.amazon.com/dp/B0D474DSB6", "reservado_por": None},
    {"nombre": "Paruu Hands Free Breast Pump P16, Wearable Breast Pump Electirc Portable with 4 Modes & 12 Levels", "link": "https://www.amazon.com/dp/B0DLB6H6NM", "reservado_por": None},
    {"nombre": "Philips Avent Natural Newborn Glass Gift Set, Baby Bottles with Natural Response Nipples", "link": "https://www.amazon.com/dp/B098Z6HYGV", "reservado_por": None},
    {"nombre": "Tommee Tippee Advanced Anti-Colic Ready for Baby BPA Free 14 Piece Set, 5oz & 9oz Bottles", "link": "https://www.amazon.com/dp/B0CQMF9SGQ", "reservado_por": None},
    {"nombre": "Reginary 4 Pack Baby Hooded Towels Coral Fleece Baby Bath Towels 30 x 30 Inch Soft Absorbent Hooded Bath", "link": "https://www.amazon.com/dp/B0BFHRFXMD", "reservado_por": None},
    {"nombre": "UKIN Baby Washcloths - Soft Face Cloths for Newborn, Absorbent Bath Face Towels", "link": "https://www.amazon.com/dp/B0B1V5NNXD", "reservado_por": None},
    {"nombre": "3 Tier Rolling Cart - Baby Diaper Caddy Organizer", "link": "https://www.amazon.com/dp/B0D2VW6DW6", "reservado_por": None},
    {"nombre": "Montessori Baby Toy for 1+ Year Old Sorting Stacking Learning Toys 6 to 12 Months", "link": "https://www.amazon.com/dp/B0CBV56MRK", "reservado_por": None},
    {"nombre": "iaper Genie Select Pail (Grey) is Made of Durable Stainless", "link": "https://www.amazon.com/dp/B0CNS4H334", "reservado_por": None},
    {"nombre": "Kinder King Baby High Chair, 8 in 1 Coverts to Dining Booster", "link": "https://www.amazon.com/dp/B0D5QSWZ91", "reservado_por": None},
    {"nombre": "Baby Bathtub, Collapsible Newborn Bathtub for Infant to Toddler 0-24 Months", "link": "https://www.amazon.com/dp/B0CTJXJL4T", "reservado_por": None},
    {"nombre": "Dancing Talking Cactus Toy for Baby Toddler, Boys Girls Gifts Singing Mimicking", "link": "https://www.amazon.com/dp/B0C1SJVKCH", "reservado_por": None},
    {"nombre": "Baby Einstein 4-in-1 Kickin' Tunes Music and Language Play Gym and Piano ", "link": "https://www.amazon.com/dp/B07MPCCDM7", "reservado_por": None}
]

@app.route("/")
def index():
    return render_template("index.html", regalos=regalos)

@app.route("/reservar", methods=["POST"])
def reservar():
    nombre_invitado = request.form["nombre"]
    index_regalo = int(request.form["regalo_index"])
    if regalos[index_regalo]["reservado_por"] is None:
        regalos[index_regalo]["reservado_por"] = nombre_invitado
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
