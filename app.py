#! /usr/bin/python2

"""
IMPORTANT

To run this example in the CSC 315 VM you first need to make
the following one-time configuration changes:

# install psycopg2 python package
sudo apt-get update
sudo apt-get install python-psycopg2

# set the postgreSQL password for user 'osc'
sudo -u postgres psql
    ALTER USER osc PASSWORD 'osc';
    \q

# install flask
sudo apt-get install python-pip
pip install flask
# logout, then login again to inherit new shell environment

"""

"""
CSC 315
Spring 2020
John DeGood

Usage:
export FLASK_APP=app.py 
flask run
# then browse to http://127.0.0.1:5000/

Purpose:
Demonstrate Flask/Python to PostgreSQL using the psycopg
adapter. Connects to the 7dbs database from "Seven Databases
in Seven Days" in the CSC 315 VM.

This example uses Python 2 because Python 2 is the default in
Ubuntu 18.04 LTS on the CSC 315 VM.

For psycopg documentation:
https://www.psycopg.org/

This example code is derived from:
https://www.postgresqltutorial.com/postgresql-python/
https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask
https://www.geeksforgeeks.org/python-using-for-loop-in-flask/
"""

import psycopg2
from config import config
from flask import Flask, render_template, request
 
def connect(location):
    location = '%' + location + '%'
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % (params['database']))
        conn = psycopg2.connect(**params)
        print('Connected.')
      
        # create a cursor
        cursor = conn.cursor()

	#if location = '%%'
	cumulativerows = list()
	
        
        
        postgreSQL_select_Query = "select * from VIDEO_TABLE where municipality like %s;"

        cursor.execute(postgreSQL_select_Query, (location,))
	rows = cursor.fetchall()
	cumulativerows = cumulativerows + rows
	
        
        postgreSQL_select_Query = "select * from PODCAST_TABLE where municipality like %s;"
	        
        cursor.execute(postgreSQL_select_Query, (location,))
	rows = cursor.fetchall()
	cumulativerows = cumulativerows + rows

        
        postgreSQL_select_Query = "select * from ARTICLE_TABLE where municipality like %s;"
        
        cursor.execute(postgreSQL_select_Query, (location,))

        
        # execute a query using fetchall()
        #cur.execute(query)
        rows = cursor.fetchall()
	cumulativerows = cumulativerows + rows


       # close the communication with the PostgreSQL
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    # return the query result from fetchall()
    return cumulativerows
 
 
 
 
 
 
 
def connect2(author):
    author = '%' + author + '%'
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % (params['database']))
        conn = psycopg2.connect(**params)
        print('Connected.')
      
        # create a cursor
        cursor = conn.cursor()
        cumulativerows = list()
        

        postgreSQL_select_Query = "SELECT * from VIDEO_TABLE where author like %s;"
        
        cursor.execute(postgreSQL_select_Query, (author,))
	rows = cursor.fetchall()
	cumulativerows = cumulativerows + rows
        
        postgreSQL_select_Query = "SELECT * from PODCAST_TABLE where author like %s;"
        
        cursor.execute(postgreSQL_select_Query, (author,))
        rows = cursor.fetchall()
	cumulativerows = cumulativerows + rows

        postgreSQL_select_Query = "SELECT * from ARTICLE_TABLE where author like %s;"
        
        cursor.execute(postgreSQL_select_Query, (author,))

        
        # execute a query using fetchall()
        #cur.execute(query)
        rows = cursor.fetchall()
	cumulativerows = cumulativerows + rows

       # close the communication with the PostgreSQL
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    # return the query result from fetchall()
    return cumulativerows
 
 
 
def connect3(title):
    title = '%' + title + '%'
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % (params['database']))
        conn = psycopg2.connect(**params)
        print('Connected.')
      
        # create a cursor
        cursor = conn.cursor()
        cumulativerows = list()
        

        postgreSQL_select_Query = "select * from VIDEO_TABLE where video_title like %s;"
        
        cursor.execute(postgreSQL_select_Query, (title,))
	rows = cursor.fetchall()
	cumulativerows = cumulativerows + rows
        
        postgreSQL_select_Query = "select * from PODCAST_TABLE where title like %s;"
        
        cursor.execute(postgreSQL_select_Query, (title,))
	rows = cursor.fetchall()
	cumulativerows = cumulativerows + rows
        
        postgreSQL_select_Query = "select * from ARTICLE_TABLE where title like %s;"
        
        cursor.execute(postgreSQL_select_Query, (title,))
         

        
        # execute a query using fetchall()
        #cur.execute(query)
        rows = cursor.fetchall()
	cumulativerows = cumulativerows + rows

       # close the communication with the PostgreSQL
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    # return the query result from fetchall()
    return cumulativerows
 
 
 
 
 
 
# app.py

app = Flask(__name__)


# serve form web page
@app.route("/")
def form():
    return render_template('my-form.html')

# handle form data
@app.route('/form-handler', methods=['POST'])
def handle_data():
    rows = connect(request.form['query'])

    return render_template('my-result.html', rows=rows)

@app.route('/form-handler2', methods=['POST'])
def handle_data2():
    rows = connect2(request.form['query2'])

    return render_template('my-result.html', rows=rows)


@app.route('/form-handler3', methods=['POST'])
def handle_data3():
    rows = connect3(request.form['query3'])

    return render_template('my-result.html', rows=rows)



if __name__ == '__main__':
    app.run(debug = True)

