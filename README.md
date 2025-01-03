RUN GUNICORN 
gunicorn -b:$PORT app:app
