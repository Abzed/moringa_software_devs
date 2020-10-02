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
    document.getElementById("navTop").style.background = "linear-gradient(90deg, rgba(213,213,227,0.8883928571428571) 70%, rgba(231,240,234,0.804359243697479) 96%)";
    document.getElementById("navTop").style.boxShadow  = "0 8px 0px 0px rgba(0, 0, 0, 0.664)";
    document.getElementById("navTop").style.webkitBoxShadow  = "0 0px 0px 0px rgba(0, 0, 0, 0.603)";
    document.getElementById("navTop").style.mozBoxShadow  = "0 0px 0px 0px rgba(0, 0, 0, 0.678)";
    
  }
}