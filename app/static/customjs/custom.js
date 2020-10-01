window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.getElementById("navTop").style.background = "white";
    document.getElementById("navTop").style.boxShadow  = "0 8px 6px -6px rgba(0, 0, 0, 0.664)";
    document.getElementById("navTop").style.webkitBoxShadow  = "0 8px 6px -6px rgba(0, 0, 0, 0.603)";
    document.getElementById("navTop").style.mozBoxShadow  = "0 8px 6px -6px rgba(0, 0, 0, 0.678)";
    document.getElementById("navTop").style.zIndex  = "99";
    document.getElementById("navTop").style.transition ="background 0.4s"
  } else {
    document.getElementById("navTop").style.background = "transparent";
    document.getElementById("navTop").style.boxShadow  = "0 8px 0px 0px rgba(0, 0, 0, 0.664)";
    document.getElementById("navTop").style.webkitBoxShadow  = "0 0px 0px 0px rgba(0, 0, 0, 0.603)";
    document.getElementById("navTop").style.mozBoxShadow  = "0 0px 0px 0px rgba(0, 0, 0, 0.678)";
    
  }
}