const storedScheme = localStorage.getItem('as-scheme');

const darkSwitch = document.getElementById('dark-mode-button');
const contentSection = document.querySelectorAll('.content-section');
const taskColumn = document.querySelector('.task-column');

darkSwitch.addEventListener('click', () => {
  for(i = 0; i < contentSection.length; i++){
    contentSection[i].classList.toggle('darkmode');
  };
  if (taskColumn) {
    taskColumn.classList.toggle('darkmode');
  }
  if (storedScheme == 'dark') {
    localStorage.setItem('as-scheme', 'light');
  } else {
    localStorage.setItem('as-scheme', 'dark');
  };
});

if (storedScheme == 'dark') {
  if (taskColumn) {
    taskColumn.classList.toggle('darkmode');
  }
  darkSwitch.checked = true
  for (i = 0; i < contentSection.length; i++) {
    contentSection[i].classList.toggle('darkmode');
  };
  
};
