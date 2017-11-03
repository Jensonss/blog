/**
 * Created by jenson on 2017/11/2.
 */
$(document).ready(
    function () {
        var isShow = false;
        $(".reply-label").click(function () {
            if (isShow) {
                $("#reply-div").remove();
                isShow = !isShow;
            } else {
                var reply = "<div id='reply-div'>" +
                    "<textarea id='reply-area'></textarea>" +
                    "<div><button id='reply-btn'>回复</button>" +
                    "<button id='reply-cancel'>取消</button></div>" +
                    "</div>";
                $(this).next().append(reply);
                isShow = !isShow;
            }
        })
    }
)


