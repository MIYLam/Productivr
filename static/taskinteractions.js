
// script.js

document.addEventListener("DOMContentLoaded", function() {
    var deletionButton = document.querySelectorAll(".deletion");
    
    // Loop through each button and add an event listener
    deletionButton.forEach(function(button) {
        button.addEventListener("click", function() {
            // Find the closest parent element with an ID
            var parentDiv = button.closest("[id]");
            
            if (parentDiv) {
                var parentId = parentDiv.id;
                const parent_element = document.getElementById(parentId);
                parent_element.remove();
            }
        });
    });
});


function openForm() {
    document.getElementById("taskAdd").style.display = "block";
  }
  
function closeForm() {
    document.getElementById("taskAdd").style.display = "none";
}