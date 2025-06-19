#This transforms chosen langauges into suitable,
# and add them to the sql query. 
def addLanguageToRequest(request, language):
    print(f"Checking Element: {language}")
    if (str(language) == "python"):
        request += f" (python = 1)"
    elif (str(language) == "java"):
        request += f" (java = 1)"
    elif (str(language) == "c++"):
        request += f" (c++ = 1)"
    elif (str(language) == "css"):
        request += f" (css = 1)"
    elif (str(language) == "sql"):
        request += f" (sql = 1)"
    elif (str(language) == "html"):
        request += f" (html = 1)"
    elif (str(language) == "lc3"):
        request += f" (lc3 = 1)"

    print(f"Request after Adding: {request}")

    return request

#This functions gets details of the user's chosen project. 
def getProjectData(connection, chosenProject):
    print("---------GETTING PROJECT DETAILS---------")

    result = "nothing"

    print(f"Project Chosen: {chosenProject}")

    if (chosenProject != "No Result Available") and (chosenProject != "Unknown"):

        #Forms sql query. 
        request = f"SELECT * FROM info WHERE name='{chosenProject}';\n"
        print(f"Request: {request}")

        #Creates curser with connection to database. 
        curser = connection.cursor()
        #Sends sql query to database. 
        curser.execute(request)
        #Store results of sql query. 
        result = curser.fetchall()

        #Used for debugging: Sees results of sql query. 
        for item in result:
            print(f"Project Name: {item['name']}\n")
            print(f"Summary: {item['summary']}\n")
            print(f"Languages used: {item['languages']}\n")
            print(f"Developers: {item['developers']}\n")
            print(f"Contribution: {item['contribution']}\n")
    
    else:
        print("Warning: Can't get data from a project.")

    print("------------PROCESS FINISHED-------------")

    return result

#Gets projects from databased that match
# user's provided parameters.  
def determineOutput(connection, languages, projectType): 

    print("-------------CREATE REQUEST-------------")

    print(f"Number of Languages: {len(languages)}")
    print(f"Project Type: {projectType}")

    #Setup default request. 
    request = "SELECT name FROM projects "

    conditionSet = False
    
    #Checks to see if the User has chosen a project type, 
    # and to see if the project type is not "all". 
    if ((str(projectType) != "all") and (str(projectType) != "Not chosen")): 
        conditionSet = True

        #Adds project type to the sql query. 
        request += f"WHERE (projectType = '{projectType}') "

    #Checks if user chosen specific langauges. 
    if (len(languages) != 0):
        if (conditionSet != True): 
            request += "WHERE"
        
        for i in range(len(languages)): # if broken change to len(languages) - 1
            if ((conditionSet == True) or (i > 1)): 
                request += " AND "

            request = addLanguageToRequest(request, languages[i])

            # if ((i + 1) == len(languages) - 1): 
            #     request += " AND "
            
            conditionSet = True

        
        # request = addLanguageToRequest(request, languages[len(languages) - 1])

    request += ";"

    print(f"Request: {request}")

    cursor = connection.cursor()
    cursor.execute(request)
    result = cursor.fetchall()

    print(f"Number of Result Found form SQL query: {len(result)}")

    print("-------------ENDING REQUEST-------------")


    return result; 




def formatOutput(result): 

    print("------------GETTING PROJECT NAMES------------")

    # output = ""

    # for item in result: 
    #     output += "<div>\n"
    #     output += f"\t<p>{item['name']}</p>\n"
    #     output += "</div>\n"

    # print("Editied html: ")
    # print(output)

    output = []
    for item in result: 
        output.append(item['name'])

    if (len(output) == 0): 
        output = ["No Result Available."]
        
    print("Items Found: ")

    for i in range(len(output)): 
        print(output[i], end=", ")

    print()

    print("--------------FINISHED GETTING PROJECTS--------------")

    return output
