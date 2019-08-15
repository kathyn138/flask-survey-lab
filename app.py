from flask import Flask, request, render_template, flash, redirect, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from surveys import surveys

app = Flask(__name__)
responses = []

chosen_survey = surveys['satisfaction']

@app.route('/')
def index():
    "Displays basic survey information on index"

    return render_template('home.html',
                           survey_title=chosen_survey.title,
                           survey_instructions=chosen_survey.instructions)


@app.route('/questions/<int:question_num>')
def question(question_num):
    "Displays a question and choices from a survey"

    question = chosen_survey.questions[question_num]

    return render_template('question.html',
                           question=question,
                           survey_title=chosen_survey.title,
                           question_num=question_num)


@app.route('/answer', methods=["POST"])
def record_response():
    "Takes user's response and puts it into responses list"
    
    # response = request.form[question_num]
    print(f"our message is {request.form[0]}")
    #can we grab the 0 from the tuple that's returned? 
    #request.form returns a list with a tuple inside
    # responses.append(response)

    return redirect('questions/{{question_num + 1}}')
