function toggleDropdown() {
    var dropdown = document.getElementById("dropdown");
    if (dropdown.style.display === "block") {
      dropdown.style.display = "none";
    } else {
      dropdown.style.display = "block";
    }
  }

 // JavaScript to handle modal functionality
 const modal = document.getElementById('modal');
 const closeModalBtn = document.getElementById('close-modal');
 const surpriseBtn = document.querySelector('.surprise-btn');

 surpriseBtn.addEventListener('click', () => {
   modal.style.display = 'flex';
 });

 closeModalBtn.addEventListener('click', () => {
   modal.style.display = 'none';
 });


 
  