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
      $("#Adam").slideToggle("slow");
  });
  $("#B2").click(function(){
      $("#Daryl").slideToggle("slow");
  });
  $("#B3").click(function(){
      $("#Jay").slideToggle("slow");
  });
  $("#B4").click(function(){
      $("#James").slideToggle("slow");
  });
  $("#B5").click(function(){
      $("#Levian").slideToggle("slow");
  });
});
