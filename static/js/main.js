var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

$(document).ready(function(){
    $('[data-toggle="popover"]').popover(); 
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

// Posting and updating forms
function autoExpand() {
	var title = document.getElementById("titleForm");
	title.style.height=(title.scrollHeight) + "px";
	var detail = document.getElementById("detailForm");
	detail.style.height=(detail.scrollHeight) + "px";
	// $("#detailForm, #titleForm").css("height",scrollHeight + "px")
	$("#detailForm, #titleForm").on("keypress keyup", function(e){
		var keycode = (e.keyCode ? e.keyCode : e.which);
		// Resetting forms height on content delete
		if (this.value == "") {
			console.log("Empty!")
			this.style.height="98px";
		}
		else {
			this.style.height=(this.scrollHeight) + "px";
		}
		if (keycode == '13') { // Enter
			if (this.id == "titleForm") {
				e.preventDefault();
				// Focus the detail form
		 		$(this).blur()
		 		$(detail).focus()
			}
		} else {
			this.style.height = (this.scrollHeight) + "px";
		}
	})
}
