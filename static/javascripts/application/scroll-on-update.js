$(function() {
    console.log("LOAD: scroll-on-update") // sanity check

    var out = document.getElementById("auto-scroll");
    var isScrolledToBottom = out.scrollHeight - out.clientHeight <= out.scrollTop + 1;
    out.scrollTop = out.scrollHeight - out.clientHeight;
    update_scroll();

    function add_message() {
        console.log("New Message")
        var newElement = document.createElement("li");
        newElement.innerHTML = c++;
        check_scroll();
        out.appendChild(newElement);
        update_scroll();
    }

    function check_scroll(){
        isScrolledToBottom = out.scrollHeight - out.clientHeight <= out.scrollTop + 1;
    }

    function update_scroll() {
        if(isScrolledToBottom){
            out.scrollTop = out.scrollHeight - out.clientHeight;
        }
    }

});
