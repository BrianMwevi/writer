var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

$(document).ready(function(){
    $('[data-toggle="popover"]').popover(); 
	testing()
	autoExpand()
});

function popMenu(){
	$("#popupEdit").removeClass("show");
	$("#popupMenu").toggleClass("show")
}

function rotateSignup() {
	$("#login").css("transform", "rotateY(-180deg)")
	$("#signup").removeClass("form-side--back");
}
function rotateLogin() {	
	$("#signup").addClass("form-side--back");
	$("#login").css("transform", "rotateY(0)");
	var url = "http://127.0.0.1:8000/accounts/login/";
}

function popupCog() {
	$("#popupEdit").toggleClass("show");
	$("#popupMenu").removeClass("show");
}
 
function testing() {
	$(".title_form").keypress(function(e){
		var keycode = (e.keyCode ? e.keyCode : e.which);
    if (keycode == '13') {
 		e.preventDefault()
 		$(this).blur()
 		$(".detail-form").focus()
    }

 })
}

function autoExpand() {
	var detail_form = document.getElementById("detail_form");
	// var 

	$(detail_form).keyup(function(e){
		var keycode = (e.keyCode ? e.keyCode : e.which);
		if (keycode == '13') {
			this.style.height = (this.scrollHeight +10) + "px";
		}
	})
	if (detail_form.value == "") {
		this.style.height = ("88px"); 
		console.log("empty")

	} else {
		$(detail_form).css("height", detail_form.scrollHeight + "px");
	}
}
