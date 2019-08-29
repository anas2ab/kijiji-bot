from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import scheduler as sch

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'


class ReusableForm(Form):
    item = StringField('Items name: ', validators=[validators.data_required()])
    # min_price = StringField('Min_price: ', validators=[validators.data_required()])
    # max_price = StringField('Max_price: ', validators=[validators.data_required()])
    # send_email = StringField('sender_email', validators=[validators.data_required()])
    # receive_email = StringField('Receive_email: ', validators=[validators.data_required()])
    # days = StringField('Days: ', validators=[validators.data_required()])
    # interval = StringField('Interval: ', validators=[validators.data_required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    # print(form.errors)
    if request.method == 'POST':
        item = request.form['item']
        min_price = request.form['min_price']
        max_price = request.form['max_price']
        # send_email = request.form['sender_email']
        # receive_email = request.form['receiver_email']
        # password = request.form['sender_password']
        chat_id = request.form['chat_id']
        period = request.form['period']
        interval = request.form['interval']

        if form.validate():
            sch.scheduler(item, min_price, max_price, int(chat_id), int(period), int(interval))
            flash('Done ')

        else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(port=8080)
