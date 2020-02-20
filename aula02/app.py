from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index"

def teste():
    return "<p> testando </p>
    
def.add_url_rule("/teste", "teste", )

if __name__ == "__main__":
    app.run(debug=True, port="3000")