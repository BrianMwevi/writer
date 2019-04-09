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

// Posting and updating forms
function autoExpand() {
	var detailForm = document.getElementById("detailForm");
	var titleForm = document.getElementById("titleForm");
	$("#detailForm, #titleForm").val(function(){
		if (this.value == "") {
			if (this.id == "titleForm") {
				this.style.height="148px";
			}else{
				// this.style.paddingTop="98px";
				console.log(this.id)
			}
		}
	})
	$("#detailForm, #titleForm").keypress(function(e){
		var keycode = (e.keyCode ? e.keyCode : e.which);
		console.log(this.scrollHeight)
		// Resetting forms height on content delete
		$(this).keyup(function(e){
			if (this.value == "") {
				this.style.height="98px";
				console.log(this.style.height=this.scrollHeight + "px")
			}
			else {
				this.style.height=(this.scrollHeight) + "px";
			}
		})
		if (keycode == '13') { // Enter
			if (this.id == "titleForm") {
				e.preventDefault();
				// Focus the detail form
		 		$(this).blur()
		 		$(detailForm).focus()

			}
		} else {
			this.style.height = (this.scrollHeight) + "px";
		}
	})
}
