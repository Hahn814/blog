const sidebarId = 'sidebar';
const sidebarToggleId = 'toggle-sidebar';

// Add event listeners to the toggle button and container
const sidebar = document.getElementById(sidebarId);
const button = document.getElementById(sidebarToggleId);

function assignIcon(){
  // Adjust the button icon based on whether the sidebar is collapsed
  if(sidebar.classList.contains('collapsed')) {
    button.innerHTML = '<ion-icon name="chevron-back-outline"></ion-icon>';
  } else {
    button.innerHTML = '<ion-icon name="chevron-forward-outline"></ion-icon>';
  }
}

assignIcon()  // Assign the default icon on page load.
button.addEventListener('click', _ => {
  console.log("HERE");
  sidebar.classList.toggle('collapsed');
  assignIcon();
});