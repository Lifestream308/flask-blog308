from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)

    # venv\Scripts\activate
    # set FLASK_APP=run   ?? as in run.py
    # flask run

    # Debug mode was not turning on, had to use command below inside terminal 
    # set FLASK_DEBUG=1