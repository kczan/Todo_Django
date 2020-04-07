const storedScheme = localStorage.getItem('as-scheme')

const darkSwitch = document.getElementById('dark-mode-button');
const newTaskColumn = document.querySelector('.new-task-column');
const taskColumn = document.querySelector('.task-column');

darkSwitch.addEventListener('click', () => {
  newTaskColumn.classList.toggle('darkmode');
  taskColumn.classList.toggle('darkmode');
  if (storedScheme == 'dark') {
    localStorage.setItem('as-scheme', 'light');
  } else {
    localStorage.setItem('as-scheme', 'dark');
  };
});

if (storedScheme == 'dark') {
  newTaskColumn.classList.toggle('darkmode');
  taskColumn.classList.toggle('darkmode');
  darkSwitch.checked = true
}