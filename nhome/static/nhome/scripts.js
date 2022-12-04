function myFunction() {
    document.getElementById("myProfiles").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("Profile-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

document.addEventListener('DataPageReady', function(event) 
    {
      $( ".YT" ).resizable(
        {
        animate: true, animateEasing: 'swing'
        });
    });


function newLocation() 
  {
    var x = document.getElementById("IPadd");
    var val = x.value;
    if(val) {
      window.location.href="Hosts.html";
  }
    else {alert("Incorrect IP");}
  }


  $(document).ready(function() {
    $(".IP_Holder_Button").click(function(){
       $(".IP_Holder").append("<p>User Interaction Simulation</p>");
    });
});

$( document ).ready(function() {
  console.log( "ready!" );
(function($) {
    
  var allPanels = $('.accordion > dd').hide();
    
  $('.accordion > dt > a').click(function() {
    allPanels.slideUp();
    $(this).parent().next().slideDown();
    return false;
  });

})(jQuery);
});

function openTab(Levt, LName) {
  // Declare all variables
  var i, Ltabcontent, Ltablinks;

  // Get all elements with class="tabcontent" and hide them
  Ltabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < Ltabcontent.length; i++) {
    Ltabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  Ltablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < Ltablinks.length; i++) {
    Ltablinks[i].className = Ltablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(LName).style.display = "block";
  Levt.currentTarget.className += " active";
}
