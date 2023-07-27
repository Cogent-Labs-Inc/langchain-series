# Timetable Scheduler for University Classes

Timetable scheduler is a `Generative-AI` based app, developed in `langchain` using OpenAI `gpt-4` model. It takes
subjects and students data in CSV format and generates schedule for each individual student.

### Steps to Execute:

- Create the virtual environment using the command

`python -m venv env-name`

- Activate the virtual environment using the command

`source env-name/bin/activate`

- Navigate to the app directory

`cd 003_timetable_scheduler/`

- Install the requirements using the command

`pip install -r requirements.txt`

- Run the Jupyter Notebook

`jupyter notebook timetable_scheduler.ipynb`

### How it Works?

- It reads subjects and students data from CSV files, parses it and creates a prompt using that.
- The prompt is used to get timetable from `gpt-4` model using langchain.

### POC Data

- For the POC, 5 subjects and 3 students data has been used. The data is prepared in such a way so that it covers all
  the scenarios and edges cases.