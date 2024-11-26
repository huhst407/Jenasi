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


@app.route("/api/v0/train", methods=["POST"])
def add_training_data():
  question = request.json.get('question')
  sql = m_vn.request.json.get("sql")
  ddl = m_vn.request.json.get("ddl")
  documentation = m_vn.request.json.get("documentation")
  Question=m_vn.request.json.get("Question")

  try:
    id = m_vn.train(
      question=question, sql=sql, ddl=ddl, documentation=documentation,
      Question=Question
    )
    return jsonify({"id": id})
  except Exception as e:
    print("TRAINING ERROR", e)
  return jsonify(vanna_app.add_training_data())
vanna_app.run()


@app.route("/api/v0/generate_sql", methods=["GET"])
def generate_sql(user: any):
        """
        Generate SQL from a question
        从问题中生成SQL
        """
        question = m_vn.request.args.get("question")

        if question is None:
            return jsonify({"type": "error", "error": "No question provided"})

        id = m_vn.cache.generate_id(question=question)
        sql = m_vn.generate_sql(question=question, allow_llm_to_see_data=m_vn.allow_llm_to_see_data)

        m_vn.cache.set(id=id, field="question", value=question)
        m_vn.cache.set(id=id, field="sql", value=sql)

        if m_vn.is_sql_valid(sql=sql):
            return jsonify(
                {
                    "type": "sql",
                    "id": id,
                    "text": sql,
                  }
            )
        else:
            return jsonify(
                {
                    "type": "text",
                    "id": id,
                    "text": sql,
                }
            )

'''
@self.flask_app.route("/api/v0/get_function", methods=["GET"])
        @self.requires_auth
        def get_function(user: any):
            """
            Get a function from a question
            从问题直接生成一个对应的SQL查询函数
            ---
            parameters:
              - name: user
                in: query
              - name: question
                in: query
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: function
                    id:
                      type: object
                    function:
                      type: string
            """
            question = flask.request.args.get("question")

            if question is None:
                return jsonify({"type": "error", "error": "No question provided"})

            if not hasattr(vn, "get_function"):
                return jsonify({"type": "error", "error": "This setup does not support function generation."})

            id = self.cache.generate_id(question=question)
            function = vn.get_function(question=question)

            if function is None:
                return jsonify({"type": "error", "error": "No function found"})

            if 'instantiated_sql' not in function:
                self.vn.log(f"No instantiated SQL found for {question} in {function}")
                return jsonify({"type": "error", "error": "No instantiated SQL found"})

            self.cache.set(id=id, field="question", value=question)
            self.cache.set(id=id, field="sql", value=function['instantiated_sql'])

            if 'instantiated_post_processing_code' in function and function['instantiated_post_processing_code'] is not None and len(function['instantiated_post_processing_code']) > 0:
                self.cache.set(id=id, field="plotly_code", value=function['instantiated_post_processing_code'])

            return jsonify(
                {
                    "type": "function",
                    "id": id,
                    "function": function,
                }
            )
'''
