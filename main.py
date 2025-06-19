from flask import Flask, request, render_template, jsonify
import sqlite3
import functions

app = Flask(__name__, template_folder='Pages', static_folder='Styles')



itemList = ["Unknown"]
chosenProject = "Unknown"

#Get connection to SQL database
def get_Database_Connection():
    conn = "Empty"
    try:
        print("trying to connect to Database")
        #Try to connect to sql database. 
        #Database's stored location is Database/projectDatabase.db
        conn = sqlite3.connect('Database/projectDatabase.db')
        print("trying to connect row_factory")
        #Indicate that you want the output from queries done by cursers to
        # be in the form of a sqlite3.Row class not a regular tuple. 
        conn.row_factory = sqlite3.Row
        print("Connection to Database Successfull")
    except: 
        print("Failed to connect database")

    return conn


#THIS CODE IS FOR THE HOME PAGE
@app.route('/', methods = ['GET','POST'])
def index():

    global itemList
    languageList = []
    languages = ""
    type = ""

    #Establish connection to sql database.
    connection = get_Database_Connection()

    #If application recieved "POST" Request. 
    #   Post requests are sent by users either through: 
    #   * clicking the submit button on the page. 
    #   * when they just loaded the page. 
    if (request.method == 'POST'):
        print("POST recieved")
        try: 
            #From the POST Request, get all the languages that have been chosen. 
            #   * The full list of languages are seen in Home.html. 
            #   * As seen in Home.html users pick languages by clicking their
            #     corresponding check box. 
            languageList = request.form.getlist('language')

            # Add all chosen languages into String variable "languages".
            for language in languageList: 
                languages += str(language) + ", " 

            if (len(languageList) == 0): 
                languages = "Not chosen"

        except:
            print("Error: Failed to get chosen langauges.")
            print("       Languages being set to \"Not Chosen\".")
            languages = "Not chosen"
        
        try: 
            #From Post request, get project type selected by user: 
            #   * list of the different project types are seen in 
            #     Home.html.
            #   * User can select project types through radio buttons. 
            type = request.form['projectType']
        except:
            print("Error: Failed to get chosen project type.")
            print("       Porject type set to \"Not Chosen \".")
            type = "Not chosen"

        # Get projects based on user determined specifications from the database. 
        result = functions.determineOutput(connection, languageList, type)
        
        # Extract the names of the projects from the output of the sql query results. 
        output = functions.formatOutput(result)
        itemList = output
        
        print("--------------Final Check---------------")
        print(itemList)
        print("-------------Finished Check-------------")

        return render_template('Home.html', output = itemList)
    else:
        # If no post request, render home page using default variables. 
        # Normally only done if application just been opened. 
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


#THIS CODE IS FOR PROJECT PAGES
@app.route('/new_Page')
def new_Page():
    #Establish connection to the sql database
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