
// script.js

document.addEventListener("DOMContentLoaded", function() {
    var deletionButton = document.querySelectorAll(".deletion");
    var taskToggleButton = document.querySelectorAll(".open-button")
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
    taskToggleButton.forEach
});


function openForm() {
    if (document.getElementById("circleAdd").style.display == "block"){
        document.getElementById("circleAdd").style.display = "none";
    }else{
    document.getElementById("circleAdd").style.display = "block";
    }
    
}
