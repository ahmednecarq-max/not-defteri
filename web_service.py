from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notlar = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        baslik = request.form.get("baslik")
        icerik = request.form.get("icerik")
        if baslik and icerik:
            notlar.append({"baslik": baslik, "icerik": icerik})
        return redirect("/")
    return render_template("index.html", notlar=notlar)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
