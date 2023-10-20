
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("navbar").style.boxShadow = " rgba(0, 0, 0, 0.04) 0px 3px 5px";
    } else {
        document.getElementById("navbar").style.boxShadow = "rgba(0, 0, 0, 0) 0px 0px 0px";
    }
}