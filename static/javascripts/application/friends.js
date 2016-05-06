$(function() {

    function list_friends() {
        console.log("LAUNCHED: list_friends")
        $.ajax({
             url : "/friends/list/",
             type : "POST",
             data: {},

             // Successful response
             success : function(data) {
                 $('.friends').append(data);
                 //console.log(data); // log returned data to console
                 console.log("SUCCESS: list_friends"); // another sanity check
             },

             // Non-successful response
             error : function(xhr,errmsg,err) {
                 $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                     " <a href='#' class='close'>&times;</a></div>");
                 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
             }
         });
    };

    list_friends()

    // launch msg
    console.log("LOADED: friends.js")
});
