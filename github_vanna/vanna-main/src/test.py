import plotly
from flask import Flask, jsonify,request
from kaleido.scopes import plotly
import pandas as pd
import vanna.flask as vanna_flask
import plotly.express as px
from vanna.remote import VannaDefault
from vanna.flask import VannaFlaskApp

app = Flask(__name__)

m_vn = VannaDefault(model='chinook', api_key='253e0c6afda74a15bcaa5e81e24e67ee')
m_vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')

vanna_app = VannaFlaskApp(m_vn)

@app.route('/generate_plotly_figure',methods=['POST'])
def generate_plotly_figure_route():
    question = request.json.get('question')
    result = m_vn.ask(question)
    df = pd.DataFrame(result)

    return jsonify(vanna_app.generate_plotly_figure(df))

vanna_app.run()

@app.route("/api/v0/train", methods=["POST"])
def add_training_data():
  question = request.json.get('question')
  sql = m_vn.request.json.get("sql")
  ddl = m_vn.request.json.get("ddl")
  documentation = m_vn.request.json.get("documentation")
  question_function=m_vn.request.json.get("question_function")("question_function")

  return jsonify(vanna_app.add_training_data())

