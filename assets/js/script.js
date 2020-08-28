
      $("#username").focusout(function(){
       var username=$("#username").val();
        //  alert(username);
        $.ajax({
    url: "{% url 'checkusername' %}",
    type: 'GET',
    cache: false,
     data: {
                'username': username},
    success: function(response) {
       //alert(response);
       if(response=="True"){
             $('#username_error').text("Username Taken");



}    else if(response=="False"){
           $("#username_error").html("");

}
}
});
});

      $("#UpdatePassword").click(function(){
       var fp_email=$("#fp_email").val();
       var fp_password=$("#fp_password").val();
        //  alert(username);
        $.ajax({
    url: "{% url 'password-updated' %}",
    type: 'GET',
    cache: false,
     data: {
                'fp_email': fp_email,'fp_password': fp_password},
    success: function(response) {
       //alert(response);
       if(response=="True"){
    //  alert(response);
    $("#datapass").hide();
  $("#datapassupdate").show();
           //  $('#username_error').text("Username Taken");




}    else if(response=="False"){
 alert(response);
          // $("#username_error").html("");

}
}
});
});


      $("#email").focusout(function(){
       var email=$("#email").val();
        //  alert(username);
        $.ajax({
    url: "{% url 'checkemail' %}",
    type: 'GET',
    cache: false,
     data: {
                'email': email},
    success: function(response) {
       //alert(response);
       if(response=="True"){
             $('#useremail_error').text("Email Already Exsist");

}
           else{
           $("#useremail_error").text("");

}
}
});
});


      $("#email_login").focusout(function(){
       var email_login=$("#email_login").val();
        //  alert(username);
        $.ajax({
    url: "{% url 'checkemail' %}",
    type: 'GET',
    cache: false,
     data: {
                'email': email_login},
    success: function(response) {
       //alert(response);
       if(response=="True"){



       $("#useremail_error_login").text("");


}
           else{
           $('#useremail_error_login').text("Email not Found");



}
}
});
});


      $("#email_verify").keyup(function(){
       var email_verify=$("#email_verify").val();
        //  alert(username);
        $.ajax({
    url: "{% url 'checkemail' %}",
    type: 'GET',
    cache: false,
     data: {
                'email': email_verify},
    success: function(response) {
       //alert(response);
       if(response=="True"){


        active3();
       //$("#useremail_error_verify").text("");


}
           else{
           active4();
           //$('#useremail_error_verify').text("Email not Found");



}
}
});
});


      $("#password").keyup(function(){
       var password=$("#password").val();
       var email_login=$("#email_login").val();
       //  alert(password);
       //  alert(email_login);
        $.ajax({
    url: "{% url 'checkpassword' %}",
    type: 'GET',
    cache: false,
     data: {
                'password':password,'email':email_login},
    success: function(response) {
       //alert(response);
       if(response=="True"){

      // $("#useremail_error_login").text(response);
        active1();

}
           else{
              active2();
      //    $('#useremail_error_login').text(response);



}
}
});
});


function check_register(type) {
username=document.getElementById("username").value;
fullname=document.getElementById("fullname").value;
email=document.getElementById("email").value;
phoneno=document.getElementById("phoneno").value;
password=document.getElementById("password").value;

if(type=='load') {
register=document.getElementById("register");
register.removeAttribute("type");
register.classList.add("disable_btn");
register.classList.remove("myButton");
}
else if (type=='check') {
username=document.getElementById("username").value;
fullname=document.getElementById("fullname").value;
email=document.getElementById("email").value;
phoneno=document.getElementById("phoneno").value;
password=document.getElementById("password").value;

if (username.length!=0) {


if (fullname.length!=0) {
if (email.length!=0) {
if (phoneno.length!=0) {




var npass = passwordChanged();
if(npass=='Strong') {
register=document.getElementById("register");
register.setAttribute("type","submit");
register.classList.add("myButton");
register.classList.remove("disable_btn");
}
if(npass=='Medium') {
register=document.getElementById("register");
register.removeAttribute("type");
register.classList.add("disable_btn");
register.classList.remove("myButton");
}
if(npass=='weak') {
register=document.getElementById("register");

register.removeAttribute("type");
register.classList.add("disable_btn");
register.classList.remove("myButton");
}


}
}
}
}


}



}

function passwordChanged(req) {

        if(req=='typenewpass') {
         var strength = document.getElementById('strength');
        var strongRegex = new RegExp("^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$", "g");
        var mediumRegex = new RegExp("^(?=.{7,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
        var enoughRegex = new RegExp("(?=.{6,}).*", "g");
        var pwd = document.getElementById("fp_password");
        if (pwd.value.length == 0) {
            strength.innerHTML = 'Type Password';
            active6();
        } else if (false == enoughRegex.test(pwd.value)) {
            strength.innerHTML = 'More Characters';
            active6();
        } else if (strongRegex.test(pwd.value)) {
            strength.innerHTML = '<span style="color:green">Strong!</span>';
            active5();
              return 'Strong';
        } else if (mediumRegex.test(pwd.value)) {
            strength.innerHTML = '<span style="color:orange">Medium!</span>';
              return 'Medium';
              active6();

        } else {
            strength.innerHTML = '<span style="color:red">Weak!</span>';
            return 'weak';
            active6();
        }
        }

        var strength = document.getElementById('strength');
        var strongRegex = new RegExp("^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$", "g");
        var mediumRegex = new RegExp("^(?=.{7,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
        var enoughRegex = new RegExp("(?=.{6,}).*", "g");
        var pwd = document.getElementById("password");
        if (pwd.value.length == 0) {
            strength.innerHTML = 'Type Password';
        } else if (false == enoughRegex.test(pwd.value)) {
            strength.innerHTML = 'More Characters';
        } else if (strongRegex.test(pwd.value)) {
            strength.innerHTML = '<span style="color:green">Strong!</span>';
              return 'Strong';
        } else if (mediumRegex.test(pwd.value)) {
            strength.innerHTML = '<span style="color:orange">Medium!</span>';
              return 'Medium';

        } else {
            strength.innerHTML = '<span style="color:red">Weak!</span>';
            return 'weak';
        }
    }

function active1() {
logins=document.getElementById("logins");
logins.setAttribute("type","submit");
logins.classList.add("myButton");
logins.classList.remove("disable_btn");
}


function active2() {
logins=document.getElementById("logins");
logins.removeAttribute("type");
logins.classList.add("disable_btn");
logins.classList.remove("myButton");
}
function active3() {
send_forgetPass=document.getElementById("send_forgetPass");
send_forgetPass.setAttribute("type","submit");
send_forgetPass.classList.add("myButton");
send_forgetPass.classList.remove("disable_btn");
}


function active4() {
send_forgetPass=document.getElementById("send_forgetPass");
send_forgetPass.removeAttribute("type");
send_forgetPass.classList.add("disable_btn");
send_forgetPass.classList.remove("myButton");
}
function active5() {
UpdatePassword=document.getElementById("UpdatePassword");

UpdatePassword.classList.add("myButton");
UpdatePassword.classList.remove("disable_btn");
}


function active6() {
UpdatePassword=document.getElementById("UpdatePassword");
UpdatePassword.removeAttribute("type");
UpdatePassword.classList.add("disable_btn");
UpdatePassword.classList.remove("myButton");
}


    $("#forgetpass").click(function(){
  $("#login_form").hide();
  $("#reset_password").show();
});

    $("#Go_Back_to_Login").click(function(){
  $("#login_form").show();
  $("#reset_password").hide();
});