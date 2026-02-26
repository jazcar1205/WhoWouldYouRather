from flask import Flask, render_template, request, jsonify
import random
from pymongo import MongoClient

uri = "mongodb+srv://jazcarlos4_db_user:rO2ekaME0CtWH4te@rather-db.z8ogimc.mongodb.net/?appName=rather-db"

client = MongoClient(uri)

db = client["WouldRather"]
collection = db["Choices"]
votes_collection = db["votes"]
app = Flask(__name__)

#data = [
#    {
#        "id" : 0,
#        "text" : "Have Chocolate or Vanilla Ice Cream ",
#        "optionA" : "Chocolate Ice Cream ",
#        "optionA_url" : "https://delightfuladventures.com/wp-content/uploads/2024/09/vegan-chocolate-ice-cream-recipe.jpg",
#        "optionB" : "Vanilla Ice Cream ",
#        "optionB_url" : "https://www.foodandwine.com/thmb/QnTrAIt3aY1g4ToQEk-jULmKMsQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/vanilla-ice-cream-FT-RECIPE0324-cebca493f53c4431a0049ea65bfb4796.jpg"
#
#    {
#        "id" : 1,
#        "text" : "Go to the Moves or the Mall ",
#        "optionA" : " Movies ",
#        "optionA_url" : "https://assets.westchestermagazine.com/wp-content/uploads/2023/10/movie-theater-adobe-stock.jpg",
#        "optionB" : " Mall ",
#        "optionB_url" : "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/1d/bd/1c/view-from-2nd-level.jpg?w=900&h=500&s=1"
#    },
#
#    {
#        "id" : 2,
#        "text" : "Have Tea or Coffee ",
#       "optionA" : " Tea ",
#       "optionA_url" : "https://www.errenskitchen.com/wp-content/uploads/2014/08/lemon-Iced-Tea.jpg",
#       "optionB" : " Coffee ",
#        "optionB_url" : "https://www.bhg.com/thmb/UcTbMWKkDYip1DojqgSbfufQRpU=/4000x0/filters:no_upscale():strip_icc()/bhg-Affogatto-Style-Caramel-Iced-Coffee-0s0juRT-4PG97XVeJSnJ9_-3004cfb890654e3e8914a44b70fb35d4.jpg"
#   },
#
#    {
#        "id" : 3,
#        "text" : " Sleep In or Wake up Early  ",
#        "optionA" : " Sleep In ",
#        "optionA_url" : "https://domf5oio6qrcr.cloudfront.net/medialibrary/9909/GettyImages-149040090.jpg",
#        "optionB" : " Wake Up Early ",
#        "optionB_url" : "https://cms-upload.app.sleep.me/01_25_wake_up_early_blog_image_1200x800_2x_0eac4ca9c0.webp"
#    },
#
#    {
#        "id" : 4,
#        "text" : "Windows or Apple   ",
#       "optionA" : " Windows ",
#        "optionA_url" : "https://www.thespectrum.com/gcdn/media/2021/07/03/USATODAY/usatsports/Reviewed.com-RvEW-28149-Hero-1080-16-9.jpg",
#       "optionB" : " Apple ",
#       "optionB_url" : "https://cdn.uistore.design/assets/images/macos-bigsur-free-ui-kit-01.webp"
#   },
#]

#votes = {
#    0:{"A": 0 ,"B": 0},
#    1:{"A": 0 ,"B": 0},
#    2:{"A": 0 ,"B": 0},
#    3:{"A": 0 ,"B": 0},
#    4:{"A": 0 ,"B": 0},
#}
@app.route("/genQuestion")
def gen_question():
    count = collection.count_documents({})
    if count == 0:
        return jsonify({"error": "No questions found"}), 500

    num = random.randint(0, count - 1)
    doc = collection.find_one({"id": num}, {"_id": 0})

    if not doc:
        return jsonify({"error": "Question not found"}), 404

    return jsonify(doc)

@app.route("/vote", methods=["POST"])
def vote():
    data = request.get_json()

    if not data or data.get("id") is None:
        return jsonify({"error": "Missing question id"}), 400

    if data.get("option") not in ("A", "B"):
        return jsonify({"error": "Invalid option"}), 400

    question_id = int(data.get("id"))
    option = data.get("option")

    field_name = "OptionA" if option == "A" else "OptionB"

    result = votes_collection.update_one(
        {"id": question_id},
        {"$inc": {field_name: 1}}
    )

    if result.matched_count == 0:
        return jsonify({"error": "Invalid question id"}), 400

    vote_doc = votes_collection.find_one({"id": question_id}, {"_id": 0})

    total_votes = vote_doc["OptionA"] + vote_doc["OptionB"]

    if total_votes == 0:
        percent_A = 0
        percent_B = 0
    else:
        percent_A = round((vote_doc["OptionA"] / total_votes) * 100, 1)
        percent_B = round((vote_doc["OptionB"] / total_votes) * 100, 1)

    return jsonify({
        "status": "success",
        "votes": {
            "A": vote_doc["OptionA"],
            "B": vote_doc["OptionB"]
        },
        "percentages": {
            "A": percent_A,
            "B": percent_B
        }
    })

@app.route("/welcome")
def welcome():
    return "<html> <body><h1>!!Welcome To What Would You Rather !! </h1></body></html>"
@app.route("/")
def start_index():
    return render_template("index.html")

app.run(host = "0.0.0.0", port = 5051)