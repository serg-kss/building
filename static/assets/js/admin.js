document.addEventListener("DOMContentLoaded", function () {

    const messages = document.querySelectorAll(".messagelist li");

    if (messages.length) {

        setTimeout(() => {

            messages.forEach((msg) => {

                msg.style.transition = "opacity 0.4s";
                msg.style.opacity = "0";

                setTimeout(() => {
                    msg.remove();
                }, 400);

            });

        }, 3000); // 3 секунды

    }

});