$(document).ready(function(){
    $('[data-toggle="popover"]').popover(); 
    console.log("Hello world from main.js")
});

function popMenu(){
	// alert("Clicked!")
	$("#popupMenu").toggleClass("show")
}