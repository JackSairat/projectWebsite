
fetch('/get_rowCount')
    .then(response => response.json())
    .then(data => {
    const container = document.getElementsByClassName('outputCells')[0];

    //Gets the number of project names, from the /get_CountRow in main.py.
    var numItems = data.length; 

    //Each row will hold 2 project names, therefore 
    // the number of rows will be half the number of projects. 
    var numRows = Math.ceil(numItems/2); 

    //edit Home.html so that it would include the required 
    // number of rows to display the projects. 
    container.style.gridTemplateRows = `repeat(${numRows}, 5vw)`; 
    })
    .catch(error => console.error('Error fetching data:', error)); 

//This line makes it so that the block of code below will run, 
// when any link in Home page is clicked. 
document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', function(event) {

        //Gets the body contents assigned to the link clicked 
        // (ususally the name of the project) from the home page. 
        // And stores it into a variable called "linkName"
        var linkName = this.textContent; 

        //Creates request and sends it to /get_linkName in main.py. 
        fetch('/get_linkName', {
            //Sepecifies that its a Post request. 
            method: 'POST',
            headers: {

                //Sepecifies the type of content in the request. 
                'Content-Type': 'application/json'
            },

            //Stores linkName in the body.
            body: JSON.stringify({ linkName: linkName })
        })

        })

}); 

//This block of code is to change the display of the filters in the
// Home page when they are clicked by the user.
window.onload = function() {

    //Gets all elements with the class "filterInstance". 
    // Basically gets all filters in home page. 
    let filterInstances = document.getElementsByClassName("filterInstance")
    
    //For every filter do the following code. 
    for (let i = 0; i < filterInstances.length; ++i){

        //Do the following when this filter is clicked by users. 
        filterInstances[i].addEventListener('click', function(event) {
            let filterInstance = filterInstances[i];

            console.log("Title Size: " +  filterInstance.style.fontSize); 
            
            //If font size of filter is set to default, increase its size.
            if ( (filterInstance.style.fontSize === '2vw') ||
                (filterInstance.style.fontSize === "") ) {

                filterInstance.style.fontSize = '2.5vw';
            }

            //Otherwise if font size was increased, return it back to default size. 
            else if (filterInstance.style.fontSize === '2.5vw') {
                filterInstance.style.fontSize = '2vw'; 
            }

            console.log("New Title Size: " +  filterInstance.style.fontSize); 

            //Gets the title/name of the filter. 
            let instanceContents = filterInstance.textContent; 

            console.log("Title: " +  instanceContents); 

            //If the first character of the name is "+"
            // change it to "-". 
            if (instanceContents.charAt(0) === '+') {
                filterInstance.textContent = "-" + (instanceContents.substring(1));
            }

            //Otherwise if the first character of the name is "-"
            // change it back to "+". 
            else if (instanceContents.charAt(0) === '-') {
                filterInstance.textContent = "+" + (instanceContents.substring(1));
            }

            console.log("New Title: " +  filterInstance.textContent); 

            //Gets the value attribute of the filter (basically the name of the filter
            // but spelled differently). 
            let elementValue = filterInstance.getAttribute('value'); 

            console.log("Element has been CLICK!"); 
            console.log("Element Value: " + elementValue);

            if ( (elementValue === "languages") || 
                (elementValue === "projectTypes") ||
                (elementValue === "subjects")) {

                //Edit how the filter options from the filter are displayed. 
                // (example of filter options include "python" in filter "langauge".)
                editDisplay(elementValue);
            }
        });
    }
};


//This function changes how the filter options of a filter is diplayed on the Home Page. 
function editDisplay(elementID) {

    //Gets the filter options of a filter,
    // by getting elements with the id that is the same as the name of the filter. 
    let dropBar = document.getElementById(elementID); 

    //Get the display value of the filter options. 
    let displayValue = dropBar.style.display; 

    console.log("Display Value: " + displayValue);

    //If the filter options were invisable, make them visable. 
    if ( (displayValue === "none") || (displayValue === "") ) {
        dropBar.style.display = 'block'; 
    }

    //Otherwise if they where visiable, make them invisable. 
    else if (displayValue === "block") {
        dropBar.style.display = 'none'; 
    }

    displayValue = dropBar.style.display; 
    console.log("New Display Value: " + displayValue); 
}