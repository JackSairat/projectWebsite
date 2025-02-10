from flask import Flask, request, render_template, jsonify
import sqlite3
import functions

app = Flask(__name__, template_folder='Pages', static_folder='Styles')



itemList = ["Unknown"]
chosenProject = "Unknown"


def get_Database_Connection():
    conn = "Empty"
    try:
        print("trying to connect to Database")
        conn = sqlite3.connect('Database/projectDatabase.db')
        print("trying to connect row_factory")
        conn.row_factory = sqlite3.Row
        print("Connection to Database Successfull")
    except: 
        print("Failed to connect database")

    return conn



@app.route('/', methods = ['GET','POST'])
def index():

    global itemList
    languageList = []
    languages = ""
    type = ""

    connection = get_Database_Connection()

    if (request.method == 'POST'):
        print("POST recieved")
        try: 
            languageList = request.form.getlist('language')

            for language in languageList: 
                languages += str(language) + ", " 

            if (len(languageList) == 0): 
                languages = "Not chosen"

        except:
            languages = "Not chosen"
        
        try: 
            type = request.form['projectType']
        except:
            type = "Not chosen"

        result = functions.determineOutput(connection, languageList, type)
        output = functions.formatOutput(result)
        itemList = output
        
        print("--------------Final Check---------------")
        print(itemList)
        print("-------------Finished Check-------------")

        return render_template('Home.html', output = itemList)
    else:
        return render_template('Home.html', output = itemList)
    


@app.route('/get_rowCount')
def get_rowCount():
    print("------Starting JavaScript Process-------")
    print("Activating get_rowCount")
    print("Item List: ", end="")
    print(itemList)
    print()
    return jsonify(itemList)



@app.route('/get_linkName', methods = ['POST'])
def get_linkName():

    global chosenProject; 

    data = request.get_json()
    linkName = data.get('linkName')
    print(f"Project Chosen: {linkName}")

    chosenProject = linkName

    return jsonify()



@app.route('/new_Page')
def new_Page():
    connection = get_Database_Connection()
    result = functions.getProjectData(connection, chosenProject)

    print("------------STARTING NEW PAGE-----------")
    print(f"Result: {result}")
    if (result != "nothing") and (len(result) != 0):
        print("opening page...")
        projectDetails = result[0]

        numImages = projectDetails['numImages']
        images = []

        for i in range(numImages):
            images.append(f"/image{i+1}.png")

        return render_template('projectPage.html', details = projectDetails, images=images)
    else:
        print("page failed to oepen")
    print("------------FINISHED PROCESS------------")
    return render_template('Home.html', output=itemList)

if __name__ == '__main__':

    app.run(debug=False)
    index()