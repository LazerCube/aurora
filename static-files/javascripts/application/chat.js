$(function() {
    var out = document.getElementById("auto-scroll");
    var isScrolledToBottom = out.scrollHeight - out.clientHeight <= out.scrollTop + 1;

    // Form submit for sending messages
    $('#form-message').on('submit', function(event){
        event.preventDefault();
        //console.log("Form submitted!")
        send();
    });

    $('.on-enter').keydown(function (event) {
        var keypressed = event.keyCode || event.which;
        if (keypressed == 13) {
            event.preventDefault();
            send();
        }
    });

    // AJAX
    function send() {
        //console.log("LAUNCHED: form-message")
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
        //console.log("LAUNCHED: receive")
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

    function sync() {
        //console.log("LAUNCHED: sync")
        var num_messages = minMaxId('.message');
        var latest_message = num_messages['max']

        $.ajax({
             url : "/messages/conversation/sync",
             type : "POST",
             data : {   room_id : $('#returntoken').val(),
                        last_id: (latest_message),
                    },

             // Successful response
             success : function(data) {
                 check_scroll();
                 $('.messages').append(data);
                 update_scroll();
                 setTimeout(sync, 3000) // Scheldules the next request when the currnet one's completes
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
    console.log("LOADED: chat.js")

    //Start first sync
    setTimeout(sync, 5000)

});
