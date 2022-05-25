/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }

$(document).ready(function(){
  $("#B1").click(function(){
      $("#One").slideToggle("slow");
  });
  $("#B2").click(function(){
      $("#Two").slideToggle("slow");
  });
  $("#B3").click(function(){
      $("#Three").slideToggle("slow");
  });
});
