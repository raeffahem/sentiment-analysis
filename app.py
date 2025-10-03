from flask import Flask , render_template , request , jsonify
from Analyzer import analyze_text
app = Flask("sentiment analysis")

@app.route("/", methods=['GET', 'POST'])
def SentimentAnalysis():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        text = request.form['text']
        result = analyze_text(text)
        return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True)


