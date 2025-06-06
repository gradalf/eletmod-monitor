
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('monitoring.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_meal', methods=('GET', 'POST'))
def add_meal():
    if request.method == 'POST':
        date = request.form['date']
        meal_type = request.form['meal_type']
        food = request.form['food']
        quantity = request.form['quantity']
        unit = request.form['unit']
        conn = get_db_connection()
        conn.execute('INSERT INTO meals (date, meal_type, food, quantity, unit) VALUES (?, ?, ?, ?, ?)',
                     (date, meal_type, food, quantity, unit))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_meal.html')

@app.route('/add_exercise', methods=('GET', 'POST'))
def add_exercise():
    if request.method == 'POST':
        date = request.form['date']
        exercise_type = request.form['exercise_type']
        duration = request.form['duration']
        calories = request.form['calories']
        conn = get_db_connection()
        conn.execute('INSERT INTO exercises (date, exercise_type, duration, calories) VALUES (?, ?, ?, ?, ?)',
                     (date, exercise_type, duration, calories))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_exercise.html')

@app.route('/meals')
def meals():
    conn = get_db_connection()
    meals = conn.execute('SELECT * FROM meals').fetchall()
    conn.close()
    return render_template('meals.html', meals=meals)

@app.route('/exercises')
def exercises():
    conn = get_db_connection()
    exercises = conn.execute('SELECT * FROM exercises').fetchall()
    conn.close()
    return render_template('exercises.html', exercises=exercises)

if __name__ == '__main__':
    app.run(debug=True)
