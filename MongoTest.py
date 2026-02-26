from pymongo import MongoClient
import random

# Replace with your MongoDB Atlas connection string
uri = "mongodb+srv://jazcarlos4_db_user:rO2ekaME0CtWH4te@rather-db.z8ogimc.mongodb.net/?appName=rather-db"

# Connect to MongoDB
client = MongoClient(uri)

# Select database and collection
db = client["WouldRather"]
collection = db["Choices"]

# --- WRITE (Insert) ---
#collection.insert_one({
#        "id" : 1,
#        "text" : "Go to the Moves or the Mall ",
#        "optionA" : " Movies ",
#        "optionA_url" : "https://assets.westchestermagazine.com/wp-content/uploads/2023/10/movie-theater-adobe-stock.jpg",
#        "optionB" : " Mall ",
#        "optionB_url" : "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/1d/bd/1c/view-from-2nd-level.jpg?w=900&h=500&s=1"
#    })

#collection.insert_one({
#        "id" : 2,
#        "text" : "Have Tea or Coffee ",
#        "optionA" : " Tea ",
#        "optionA_url" : "https://www.errenskitchen.com/wp-content/uploads/2014/08/lemon-Iced-Tea.jpg",
#        "optionB" : " Coffee ",
#       "optionB_url" : "https://www.bhg.com/thmb/UcTbMWKkDYip1DojqgSbfufQRpU=/4000x0/filters:no_upscale():strip_icc()/bhg-Affogatto-Style-Caramel-Iced-Coffee-0s0juRT-4PG97XVeJSnJ9_-3004cfb890654e3e8914a44b70fb35d4.jpg"
#    })

#collection.insert_one({
#        "id" : 3,
#       "text" : " Sleep In or Wake up Early  ",
#       "optionA" : " Sleep In ",
#       "optionA_url" : "https://domf5oio6qrcr.cloudfront.net/medialibrary/9909/GettyImages-149040090.jpg",
#        "optionB" : " Wake Up Early ",
#        "optionB_url" : "https://cms-upload.app.sleep.me/01_25_wake_up_early_blog_image_1200x800_2x_0eac4ca9c0.webp"
#    })

#collection.insert_one({
#       "id" : 4,
#        "text" : "Windows or Apple   ",
#        "optionA" : " Windows ",
#        "optionA_url" : "https://www.thespectrum.com/gcdn/media/2021/07/03/USATODAY/usatsports/Reviewed.com-RvEW-28149-Hero-1080-16-9.jpg",
#        "optionB" : " Apple ",
#    })
#print("Document inserted!")

# --- READ (Find one) ---
num = random.randint(0, 4)
doc = collection.find_one({"id": num })
print("Document found:", doc)