let slideIndex = 0; 
showSlides(slideIndex);

function plusSlides(n) {
    slideIndex = slideIndex + 1; 
    showSlides(slideIndex); 
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    if (n > slides.length) {slideIndex = 1;}
    if (n < 1) {slideIndex = slides.length;}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; 
    }
    console.log("Number of Slides: " + slides.length)
    console.log("Current Index: " + slideIndex);
    slides[slideIndex-1].style.display= "block"; 
}