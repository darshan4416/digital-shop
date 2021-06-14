function validate(event){
    console.log("Form Submission")
    var error = document.getElementById("message")
    var message = ''

    var field = event.target.elements
    var name = field.name.value
    var email = field.email.value
    var phone = field.phone.value
    var password = field.password.value
    var re_password = field.re_password.value

    if(!name.trim())
    {
        message = "Name is required"
    }
    else if(!email.trim())
    {
        message = "Email is required"
    }
    else if(!password.trim())
    {
        message = "password is required"
    }else if(!re_password.trim())
    {
       message = "Password Enter again"
    }
    else if (password != re_password)
    {
        message = "Password is not matched"
    }

    if(message)
    {
        error.innerHTML = message
        error.hidden = false
    }
    else
    {
        error.innerHTML = ''
        error.hidden = true


        //sendEmail(name, email)
    }

//    event.stopPropagation();
//    return true;

}
//function sendEmail(name, email){
//    console.log(name,email)
//    alert()
//    $.ajax({
//     type: "POST",
//      url: "/send-otp",
//      data: {name:name, email:email}
//})
//      .done(function(msg){
//      alert("Data saved "+ msg);
//    });
//}
