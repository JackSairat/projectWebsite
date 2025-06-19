let slideIndex = 0; 
showSlides(slideIndex);

//This function is used to change the images in the slide show, 
// located in the projectPage.html. 
function plusSlides(n) {
    //Increase the image index (image number) by n (n is either -1 or 1). 
    slideIndex = slideIndex + n; 
    //Display image at image index. 
    showSlides(slideIndex); 
}

//This function is used to display images in the slide show. 
function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    //If image index is greater than the number of images, 
    // image index is set the 1 (the first image).
    if (n > slides.length) {slideIndex = 1;}
    //If image index is less then 1, 
    // go to the last image. 
    if (n < 1) {slideIndex = slides.length;}

    //Set it so that all images are invisible.
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; 
    }
    console.log("Number of Slides: " + slides.length)
    console.log("Current Index: " + slideIndex);

    //Make the image at image index visible. 
    slides[slideIndex-1].style.display= "block"; 
}