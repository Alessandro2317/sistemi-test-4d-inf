import os

from flask import Flask, send_file, render_template

app = Flask(__name__, template_folder="src")


posts = [

{'posizione': '1)' ,'title': 'Napoli', 'punti': '78 punti'},
{'posizione': '2)' ,'title': 'Inter', 'punti': '77 punti'},
{'posizione': '3)' ,'title': 'Atalanta', 'punti': '73 punti'},
{'posizione': '4)' ,'title': 'Juventus', 'punti': '67 punti'},
{'posizione': '5)' ,'title': 'Roma', 'punti': '66 punti'},
{'posizione': '6)' ,'title': 'Lazio', 'punti': '64 punti'},
{'posizione': '7)' ,'title': 'Bologna', 'punti': '59 punti'},
{'posizione': '8)' ,'title': 'Fiorentina', 'punti': '59 punti'},
{'posizione': '9)' ,'title': 'Milan', 'punti': '48 punti'},
{'posizione': '10)', 'title': 'Udinese', 'punti': '44 punti'},
{'posizione': '11)' ,'title': 'Torino', 'punti': '44 punti'},
{'posizione': '12)' ,'title': 'Genoa', 'punti': '40 punti'},
{'posizione': '13)' ,'title': 'Como', 'punti': '37 punti'},
{'posizione': '14)' ,'title': 'Hellas Verona', 'punti': '33 punti'},
{'posizione': '15)', 'title': 'Cagliari', 'punti': '34 punti'},
{'posizione': '16)', 'title': 'Lecce', 'punti': '33 punti'},
{'posizione': '17)', 'title': 'Empoli', 'punti': '31 punti'},
{'posizione': '17)', 'title': 'Venezia', 'punti': '31 punti'},
{'posizione': '19)', 'title': 'Parma', 'punti': '29 punti'},
{'posizione': '20)', 'title': 'Monza', 'punti': '18 punti'}
 
]

@app.route("/")
def index():
    return render_template('index.html', posts=posts)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
