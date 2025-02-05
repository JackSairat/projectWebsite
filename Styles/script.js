
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

