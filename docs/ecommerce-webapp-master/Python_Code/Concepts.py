# Basic Programming Concepts:

# Understand basic programming terminology and concepts like variables, data types, control flow (loops, conditionals), and functions.
# Python Basics:

# Work with Python syntax: how to write simple programs and run them.
# Learn how to use Python's built-in data structures like lists, dictionaries, and strings.
# Practical Python for Your Goals:

# Data Analysis: Introduction to libraries like pandas, numpy, and matplotlib for working with data.
# Web Development: Basic concepts of web frameworks like Flask or Django.
# Automation: Writing simple Python scripts to automate repetitive tasks.

# Let's start with the basics.

# 1. Variables and Data Types

# In Python, you can store data in variables, and each variable has a specific data type. The most common data types are:

# Integer (int): Whole numbers (e.g., 1, -5, 100)
# Float (float): Decimal numbers (e.g., 3.14, -0.001, 2.0)
# String (str): Text (e.g., "Hello, World!", "Python")
# Boolean (bool): True or False values
# Let's write a simple Python program to print some of these:


# Example variables

    age = 25  # integer
    height = 5.9  # float
    name = "Alice"  # string
    is_student = True  # boolean

# Print the variables
    print(age)
    print(height)
    print(name)
    print(is_student)

# Try running this code in a Python environment (like an IDE, Jupyter Notebook, or an online tool like Repl.it) to see how variables work.

# 2. Basic Operations

# Python also allows you to perform basic mathematical operations:

# Addition (+), Subtraction (-), Multiplication (*), Division (/)
# We can also combine variables in expressions:

    a = 10
    b = 5
    sum = a + b
    product = a * b
    print("Sum:", sum)
    print("Product:", product)


# Next Steps:

# Control Flow: We'll go over if statements (conditional logic) and loops (repeating actions).

# Functions: How to define reusable blocks of code.

# Libraries: Start exploring Python libraries that will help you with your goals.

# Data Analysis, Web Development, and Automation—with a more detailed explanation and examples, 
# covering the essential concepts and tools we’ll need to get started in Python.
# Let's dive deeper into each area—Data Analysis, Web Development, and Automation—with a more detailed explanation and examples, 
# covering the essential concepts and tools we’ll need to get started in Python.

# 1. Data Analysis with Python

# 1.1. Introduction to Pandas

# Pandas is a powerful Python library for data manipulation and analysis. It’s particularly useful for working with structured data, such as data in CSV files, Excel files, and databases. The main data structures in Pandas are Series and DataFrame.

# Series: A one-dimensional array-like object that can hold any data type.

# DataFrame: A two-dimensional, tabular data structure with rows and columns, like a spreadsheet.

# 1.1.1. Installing Pandas

# To install Pandas, use the following:

    pip install pandas

#1.1.2. Working with a DataFrame

# Let’s start by loading a CSV file into a DataFrame:

    import pandas as pd

# Load a CSV file into a DataFrame

    df = pd.read_csv('your_file.csv')  # Replace with your file path

# Display the first 5 rows of the DataFrame

    print(df.head())
    pd.read_csv(): Reads a CSV file into a DataFrame.
    df.head(): Displays the first five rows of the DataFrame. # If you want to see more rows, you can pass an argument (e.g., df.head(10))

# 1.1.3. Basic Operations with DataFrame

# Selecting Columns: You can select a column by its name.
# Select a single column

    age_column = df['age']
    print(age_column)

# Selecting Multiple Columns:
# Select multiple columns

    subset_df = df[['name', 'age']]
    print(subset_df)
    Filtering Rows: You can filter rows based on conditions


# Filter rows where age is greater than 30

    filtered_df = df[df['age'] > 30]
    print(filtered_df)

# 1.1.4. Data Cleaning in Pandas

# We often need to clean the data before analysis. Some basic cleaning tasks include:
# Handling Missing Data: You can fill missing values or drop rows/columns with missing data.

# Fill missing values with a default value

    df.fillna(0)

# Drop rows with missing values
    df.dropna()

# Renaming Columns:

# Rename columns

    df.rename(columns={'old_name': 'new_name'}, inplace=True)

# Converting Data Types:

# Convert a column to a specific data type

    df['age'] = df['age'].astype(int)

# 1.1.5. Basic Statistics with Pandas

# We can use Pandas to perform basic statistics like mean, sum, and standard deviation.


# Basic statistical summary

    print(df.describe())  # Shows count, mean, std, min, max, etc.

# Sum of a column
    total_age = df['age'].sum()
    print(f"Total Age: {total_age}")

# 1.2. Introduction to Numpy

# Numpy is a library for numerical computing in Python. It’s useful for large arrays and matrices, along with mathematical functions 
# to operate on these arrays.

# 1.2.1. Installing Numpy

    pip install numpy

#1.2.2. Creating Arrays with Numpy

    import numpy as np

# Create a simple 1D array

    arr = np.array([1, 2, 3, 4, 5])
    print(arr)

# Create a 2D array (matrix)

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(matrix)

# 1.2.3. Numpy Array Operations

# Numpy supports efficient element-wise operations.

# Add a constant to each element

    arr = arr + 5
    print(arr)

# Perform mathematical operations

    print(np.mean(arr))  # Mean
    print(np.sum(arr))   # Sum
    print(np.std(arr))   # Standard deviation

# 1.3. Introduction to Matplotlib
# Matplotlib is the most popular library for creating visualizations in Python. It helps you create line charts, bar charts, histograms, and more.

# 1.3.1. Installing Matplotlib

    pip install matplotlib

# 1.3.2. Plotting with Matplotlib
# Let’s create a basic line plot:


    import matplotlib.pyplot as plt

# Data for plotting
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

# Create a line plot
    plt.plot(x, y)
    plt.title("Simple Line Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()

# We can also create bar charts, histograms, and more:

# Bar plot example
    plt.bar(x, y)
    plt.show()

# Histogram example
    plt.hist([1, 2, 3, 4, 5, 5, 6, 7, 8, 9], bins=5)
    plt.show()

# 2. Web Development with Python:

# Python is also widely used for web development. The two most popular web frameworks in Python are Flask and Django. Let’s focus on Flask to get you started with web development.

# 2.1. Introduction to Flask
# Flask is a minimalistic web framework. It’s easy to learn and great for small to medium-sized projects.

# 2.1.1. Installing Flask

    pip install flask

# 2.1.2. Creating a Simple Flask Web Application

    Create a Python file app.py:


    from flask import Flask

# Initialize the Flask application

    app = Flask(__name__)

# Define a route for the home page

    @app.route('/')
    def home():
        return "Hello, World!"

# Run the application

    if __name__ == '__main__':
        app.run(debug=True)

# @app.route('/'): This decorator tells Flask to run the home() function when the root URL (/) is accessed.
# app.run(debug=True): Starts the web server and enables debugging.


# To run the app, simply execute python app.py and visit http://127.0.0.1:5000/ in your browser.

# 2.1.3. Templates and Static Files

# Flask allows you to use HTML templates (using Jinja2) and serve static files (like CSS and images).


    from flask import render_template

    @app.route('/greet/<name>')
    def greet(name):
        return render_template('greet.html', name=name)

# Here, greet.html is an HTML file in the templates folder.

# 3. Automation with Python

# Python is often used for automating repetitive tasks, such as file operations, data extraction, or sending emails. 
# Some useful libraries for automation include os, shutil, requests, and smtplib.

# Automation in Python can range from simple file operations to web scraping and sending emails. Let's focus on file operations and email automation 
# to get you started.

# 3.1. Automating File Operations

# We can use Python to automate tasks like renaming files, organizing files, and moving files between directories.

# 3.1.1. Renaming Files in a Directory


    import os

# Specify the directory and file names

    directory = '/path/to/directory'
    old_filename = 'old_name.txt'
    new_filename = 'new_name.txt'

# Rename the file

    os.rename(os.path.join(directory, old_filename), os.path.join(directory, new_filename))

# 3.1.2. Moving Files

    import shutil

# Move a file to a new directory

    shutil.move('old_path/file.txt', 'new_path/file.txt')

# 3.2. Automating Email Sending

# We can use Python’s smtplib to send emails automatically, which is great for reports or notifications.

# 3.2.1. Sending an Email with Gmail

    import smtplib
    from email.mime.text import MIMEText

# Set up the SMTP server and login

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Start TLS (secure connection)
    server.login('your_email@gmail.com', 'your_password')

# Compose the email

    msg = MIMEText("This is an automated email.")
    msg['Subject'] = 'Automated Email'
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'recipient_email@example.com'

# Send the email

    server.sendmail('your_email@gmail.com', 'recipient_email@example.com', msg.as_string())

# Close the connection

    server.quit()

# Make sure to replace 'your_email@gmail.com' and 'your_password' with your actual credentials.

# Summary and Next Steps:

# Data Analysis: We covered working with pandas for data manipulation, numpy for numerical computing, and matplotlib for visualization. Start experimenting with datasets you have to practice.

# Web Development: We introduced Flask to create a simple web application. You can now start building web apps with basic routes and templates.

# Automation: We looked at automating file operations and sending emails with Python. This can be expanded for more complex tasks like web scraping or scheduled automation.

# We can pick any of these areas to dive deeper into. Would you like to start by building a small project, or focus more on a specific area 
# (e.g., data analysis, building a web app)? 



# Building a web app with Python


# Building a web app is a great way to apply your Python skills! Since you're starting with Flask, we’ll walk through the steps of 
# building a simple web app using Flask. Along the way, we'll cover basic concepts like routes, templates, handling forms, and more.

# Let's build a simple Task Manager web app. This app will allow you to:

    # View a list of tasks
    # Add new tasks
    # Mark tasks as completed
    # Delete tasks

# Step 1: Setting Up Your Environment:

# Before we begin building the app, we'll need to install Flask and set up a basic project structure.

# 1. Install Flask:

# In your terminal or command prompt, install Flask by running:

    pip install flask


# 2. Set Up Your Project Structure:

# Create a project directory for your app. Inside that directory, create the following structure:


    # task_manager/
    #     ├── app.py
    #     ├── templates/
    #     │   ├── index.html
    #     │   └── layout.html
    #     └── static/
    #         ├── style.css


# app.py: This will be the main file that runs your Flask app.

# templates/: This folder will store your HTML files.

# static/: This folder will store static assets like CSS files.


# Step 2: Create the Flask App (app.py):

# 1.1. Basic Setup for app.py

# Open the app.py file and add the following code to initialize your Flask app:


    from flask import Flask, render_template, request, redirect, url_for


# Initialize the Flask application

    app = Flask(__name__)

# List to store tasks (in memory)

    tasks = []

# Route for the home page

    @app.route('/')
    def index():
        return render_template('index.html', tasks=tasks)

# Route to add a task

    @app.route('/add', methods=['POST'])
    def add_task():
        task_name = request.form.get('task_name')
        if task_name:
            tasks.append({'name': task_name, 'done': False})
        return redirect(url_for('index'))

# Route to mark a task as completed

    @app.route('/complete/<int:task_id>')
    def complete_task(task_id):
        tasks[task_id]['done'] = True
        return redirect(url_for('index'))

# Route to delete a task

    @app.route('/delete/<int:task_id>')
    def delete_task(task_id):
        tasks.pop(task_id)
        return redirect(url_for('index'))

# Run the app

    if __name__ == '__main__':
        app.run(debug=True)

# Explanation:

# Flask setup: We initialize a Flask app with app = Flask(__name__).

# Task list: For simplicity, we’re storing tasks in a Python list (tasks). Each task is a dictionary with a name and done status.

# Routes:

# /: Displays all tasks.
# /add: Handles adding a new task via a POST request.
# /complete/<task_id>: Marks a task as completed.
# /delete/<task_id>: Deletes a task.

# Step 3: Create the HTML Templates:

# Now, let’s build the HTML files inside the templates/ directory. These files will define the structure of the web pages.

# 3.1. Create layout.html

# layout.html will be the base template that other templates will extend from. This allows for a consistent header, footer, and structure across your pages.


    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Task Manager</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <header>
            <h1>Task Manager</h1>
        </header>
        
        <div class="content">
            {% block content %}{% endblock %}
        </div>

        <footer>
            <p>Task Manager &copy; 2024</p>
        </footer>
    </body>
    </html>
    {% block content %}: This is where child templates can insert content.


# 3.2. Create index.html

# index.html will extend layout.html and display the list of tasks.

    {% extends 'layout.html' %}

    {% block content %}
        <h2>Your Tasks</h2>

        <!-- Form to add new task -->
        <form action="{{ url_for('add_task') }}" method="POST">
            <input type="text" name="task_name" placeholder="Enter new task" required>
            <button type="submit">Add Task</button>
        </form>

        <ul>
            {% for task in tasks %}
                <li class="{{ 'completed' if task.done else '' }}">
                    {{ task.name }}
                    {% if not task.done %}
                        <a href="{{ url_for('complete_task', task_id=loop.index0) }}">Complete</a>
                    {% endif %}
                    <a href="{{ url_for('delete_task', task_id=loop.index0) }}">Delete</a>
                </li>
            {% else %}
                <li>No tasks available.</li>
            {% endfor %}
        </ul>
    {% endblock %}


    # Explanation:

    # Task List: We loop over the tasks and display them. If the task is marked as completed (task.done == True), we add a completed class for styling.
    # Links:
    # Complete: Links to mark the task as done.
    # Delete: Links to delete the task.


    # Step 4: Add Styles (style.css)

    # Now, let's add some basic styles in the static/ folder. Create the style.css file and add the following:


            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
            }

            header {
                background-color: #007bff;
                color: white;
                padding: 20px;
                text-align: center;
            }

            .content {
                margin: 20px;
            }

            form input {
                padding: 10px;
                margin-right: 10px;
                font-size: 16px;
            }

            form button {
                padding: 10px;
                background-color: #28a745;
                color: white;
                font-size: 16px;
                cursor: pointer;
            }

            form button:hover {
                background-color: #218838;
            }

            ul {
                list-style-type: none;
                padding: 0;
            }

            li {
                padding: 10px;
                margin: 10px 0;
                background-color: white;
                border: 1px solid #ddd;
            }

            .completed {
                text-decoration: line-through;
                color: #6c757d;
            }

            a {
                margin-left: 10px;
                color: #007bff;
                text-decoration: none;
            }

            a:hover {
                text-decoration: underline;
            }


# Step 5: Running Your Flask App:

# Now that you’ve set everything up, it's time to run the app.

# In your terminal, navigate to the directory containing app.py and run:

    python app.py


# You should see output like this:

# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

# Open your browser and go to http://127.0.0.1:5000/. You’ll see the Task Manager app where you can:

    Add tasks.
    Mark tasks as completed.
    Delete tasks.
    Step 6: Next Steps

# Now that you have a basic task manager app, you can expand it further. Some ideas to enhance the app:

# Persistent Storage: Right now, the tasks are stored in memory (which will be lost when you restart the app). 
# You could use a database (e.g., SQLite, PostgreSQL) to store tasks persistently.

# User Authentication: Add the ability for users to log in and manage their tasks.
    
# Styling: Improve the user interface with more CSS or frameworks like Bootstrap.

# Advanced Features: Add functionality like due dates for tasks, prioritization, etc.

# Let me know if you'd like more guidance on any of these steps or if you want to dive deeper into another area!