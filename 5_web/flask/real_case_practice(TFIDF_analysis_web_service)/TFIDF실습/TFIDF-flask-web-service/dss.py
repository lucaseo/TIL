from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)  #(__name__) = dss
app.config.update(
    TEMPLATES_AUTO_RELOAD = True, # index.html을 reload하면 바로 수정될 수 있도록
)


# model을 가져오는 기능 글로벌로 선언
models = {}
def init():
    with open("./models/classification.plk", "rb") as f:
        models["classification"] = pickle.load(f)

init()


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/predict/", methods=["POST"])  # method = 문자열이기 때문에 POST로 설정
def predict():

    classification_list = ["정치", "경제", "사회", "생활/문화", "세계", "IT/과학"]
    model = models["classification"]

    if request.method == "POST": #포스트인 경우에만 실행이 되도록
        sentence = request.values.get("sentense")

        predict_data = model.predict_proba([sentence])[0]

        result = {"status":200, "result":list(predict_data), "category": classification_list}

    else:
        result = {"status":201}

    return jsonify(result)
