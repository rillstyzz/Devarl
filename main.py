from flask import Flask, render_template, request, redirect, url_for, session, flash
from groq import Grog
app = Flask(__name__)

AI_KEY = "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";

@app.route('/')
def dashboard():
    return render_template ('dashboard.html')


@app.route('/materi')
def materi():
    return render_template ('materi.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        jawaban = 'jawab'
        jawaban_user = request.form['tugas']
        if jawaban_user.lower() == jawaban.lower():
            print('Jawaban Benar')  
        else:
            print('Jawaban anda salah')
            exit
        return render_template ('login.html', jawaban_benar=jawaban)
    return render_template ("login.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=90)