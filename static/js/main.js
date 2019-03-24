var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

$(document).ready(function(){
    $('[data-toggle="popover"]').popover(); 
    // loginUser()
});

function popMenu(){
	$("#popupEdit").removeClass("show");
	$("#popupMenu").toggleClass("show")
}

function rotateSignup() {
	$("#login").css("transform", "rotateY(-180deg)")
	$("#signup").removeClass("form-side--back");
	// function (callback){
		var url = "http://127.0.0.1:8000/accounts/register/"
		// window.location = url;
	// }
	// callback()

}
function rotateLogin() {
	// $(".form-side--front").css("transform", "rotateY(-180deg)");
	// location.reload()
	
	$("#signup").addClass("form-side--back");
	$("#login").css("transform", "rotateY(0)");
	var url = "http://127.0.0.1:8000/accounts/login/";
}

function popupCog() {
	$("#popupEdit").toggleClass("show");
	$("#popupMenu").removeClass("show");
}
function loginUser(){
	// event.preventDefault();
	// var formData = $("#loginForm").serialize();
	// var loginUrl = "/accounts/login/";
	// authUser(formData, loginUrl)
	$( "#loginForm" ).submit(function( event ) {
		event.preventDefault();
		var formData = $("#loginForm").serialize();
		var loginUrl = "/accounts/login/";
		authUser(formData, loginUrl)

});

}

function signupUser(){
	$( "#signupForm" ).submit(function( event ) {
		event.preventDefault();
		var formData = $("#signupForm").serialize();
		var signupUrl = "/accounts/register/";
		authUser(formData, signupUrl)
	});
}



// Ajax post call
function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
 function authUser(formData, url){
 	$.ajax({
	    url     : url,
	    method  : "POST",
	    data    : formData,
	    beforeSend: function (xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    },
	    success : function(data){
	    	// alert("Success")
	      if (url =="/accounts/login/") {
	      	url = "http://127.0.0.1:8000/";
	    	console.log(url)

	      	location.replace(url);
	      } else {
	      	console.log("No url")
	      }
	    },
	    errors  : function(data){
	        alert("Form errors")
	    },
	})
 }