var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

$(document).ready(function(){
    $('[data-toggle="popover"]').popover(); 
	// testing()
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

function autoExpand() {
	var detailForm = document.getElementById("detailForm");
	var titleForm = document.getElementById("titleForm");
	$(detailForm).keyup(function(){
		console.log($(this).val())
	})
	// $(titleForm,detailForm).keypress(function(e){
	// 	var keycode = (e.keyCode ? e.keyCode : e.which);
	// 	var title = this.id;
	// 	if (keycode == '13') {
	// 		// console.log(title)
	// 		if (title == "titleForm") {
	// 			e.preventDefault()
	// 	 		$(this).blur()
	// 	 		$(detailForm).focus()

	// 		}else {
	// 			console.log(this.id)
	// 			this.style.height = (this.scrollHeight +10) + "px";
	// 		}
	// 	}
	// })
	// if (detailForm.value == "") {
	// 	this.style.height = ("88px"); 
	// 	console.log("empty")

	// } else {
	// 	$(detailForm).css("height", detailForm.scrollHeight + "px");
	// }
}
