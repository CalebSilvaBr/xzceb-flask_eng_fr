from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation as mt

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french=mt.translator.english_to_french(textToTranslate)
    return french

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english=mt.translator.french_to_english(textToTranslate)    
    return english

@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
