
fetch('/get_rowCount')
    .then(response => response.json())
    .then(data => {
    const container = document.getElementsByClassName('outputCells')[0];
    var numItems = data.length; 
    var numRows = Math.ceil(numItems/2); 
    container.style.gridTemplateRows = `repeat(${numRows}, 5vw)`; 
    })
    .catch(error => console.error('Error fetching data:', error)); 

document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', function(event) {
        var linkName = this.textContent; 

        fetch('/get_linkName', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ linkName: linkName })
        })

        })

}); 


window.onload = function() {
    let filterInstances = document.getElementsByClassName("filterInstance")
    
    for (let i = 0; i < filterInstances.length; ++i){
        filterInstances[i].addEventListener('click', function(event) {
            let filterInstance = filterInstances[i];

            console.log("Title Size: " +  filterInstance.style.fontSize); 

            if ( (filterInstance.style.fontSize === '2vw') ||
                (filterInstance.style.fontSize === "") ) {

                filterInstance.style.fontSize = '2.5vw';
            }
            else if (filterInstance.style.fontSize === '2.5vw') {
                filterInstance.style.fontSize = '2vw'; 
            }

            console.log("New Title Size: " +  filterInstance.style.fontSize); 

            let instanceContents = filterInstance.textContent; 

            console.log("Title: " +  instanceContents); 

            if (instanceContents.charAt(0) === '+') {
                filterInstance.textContent = "-" + (instanceContents.substring(1));
            }
            else if (instanceContents.charAt(0) === '-') {
                filterInstance.textContent = "+" + (instanceContents.substring(1));
            }

            console.log("New Title: " +  filterInstance.textContent); 

            let elementValue = filterInstance.getAttribute('value'); 

            console.log("Element has been CLICK!"); 
            console.log("Element Value: " + elementValue);

            if ( (elementValue === "languages") || 
                (elementValue === "projectTypes") ||
                (elementValue === "subjects")) {
                editDisplay(elementValue);
            }
        });
    }
};

function editDisplay(elementID) {
    let dropBar = document.getElementById(elementID); 
    let displayValue = dropBar.style.display; 

    console.log("Display Value: " + displayValue);
    if ( (displayValue === "none") || (displayValue === "") ) {
        dropBar.style.display = 'block'; 
    }
    else if (displayValue === "block") {
        dropBar.style.display = 'none'; 
    }

    displayValue = dropBar.style.display; 
    console.log("New Display Value: " + displayValue); 
}