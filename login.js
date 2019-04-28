"use strict";
var $ = function(id) {
     return document.getElementById(id); 
};

function testUserNameAndPassword(){
    var email = $("email").value;
    var password = $("password").value;

    var pass = localStorage.getItem(email);

    if(!(pass!=null && (password.localeCompare(pass)==0))){
    alert("Username/password invalid")
    }
}