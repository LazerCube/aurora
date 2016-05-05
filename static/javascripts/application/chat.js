$(function() {
    var out = document.getElementById("auto-scroll");
    var isScrolledToBottom = out.scrollHeight - out.clientHeight <= out.scrollTop + 1;

    // Form submit for sending messages
    $('#form-message').on('submit', function(event){
        event.preventDefault();
        console.log("Form submitted!")
        send();
    });

    setInterval(function() {
        console.log("CHECK UPDATE")
        sync();
    }, 3000);

    // AJAX
    function send() {
        console.log("LAUNCHED: form-message")
        $.ajax({
             url : "/messages/conversation/send",
             type : "POST",
             data : {   room_id : $('#returntoken').val(),
                        message : $('#inputMessage').val(),
                    },

             // Successful response
             success : function(json) {
                 $('#inputMessage').val(''); // removes the value from the input
                 sync();
                 console.log(json); // log returned json to console
                 console.log("success"); // another sanity check
             },

             // Non-successful response
             error : function(xhr,errmsg,err) {
                 $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                     " <a href='#' class='close'>&times;</a></div>");
                 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
             }
         });
    };

    function receive() {
        console.log("LAUNCHED: receive")
        $.ajax({
             url : "/messages/conversation/receive",
             type : "POST",
             data : {   room_id : $('#returntoken').val(), },

             // Successful response
             success : function(data) {
                 $('.messages').append(data);
                 //console.log(data); // log returned json to console
                 out.scrollTop = out.scrollHeight - out.clientHeight;
                 update_scroll();
                 console.log("SUCCESS: receive"); // another sanity check
             },

             // Non-successful response
             error : function(xhr,errmsg,err) {
                 $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                     " <a href='#' class='close'>&times;</a></div>");
                 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
             }
         });
    };

    function sync() {
        //console.log("LAUNCHED: sync")
        var num_messages = minMaxId('.message');
        var latest_message_pk = num_messages['max']

        $.ajax({
             url : "/messages/conversation/sync",
             type : "POST",
             data : {   room_id : $('#returntoken').val(),
                        last_id: (latest_message_pk),
                    },

             // Successful response
             success : function(data) {
                 check_scroll();
                 $('.messages').append(data);
                 update_scroll();
                 //console.log(data); // log returned json to console
                 //console.log("SUCCESS: receive"); // another sanity check
             },

             // Non-successful response
             error : function(xhr,errmsg,err) {
                 $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                     " <a href='#' class='close'>&times;</a></div>");
                 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
             }
         });
    };

    function minMaxId(selector) {
        var min=null, max=null;
        $(selector).each(function() {
            var id = parseInt(this.id, 10);
            if ((min===null) || (id < min)) { min = id; }
            if ((max===null) || (id > max)) { max = id; }
        });
        return {min:min, max:max};
    };

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    function check_scroll(){
        isScrolledToBottom = out.scrollHeight - out.clientHeight <= out.scrollTop + 1;
    };

    function update_scroll() {
        if(isScrolledToBottom){
            out.scrollTop = out.scrollHeight - out.clientHeight;
        }
    };

    //On launch, get messages
    receive()

    // launch msg
    console.log("LOADED: custom.js")
});
