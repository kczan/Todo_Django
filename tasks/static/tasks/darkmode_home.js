const storedScheme = localStorage.getItem('as-scheme')

const darkSwitch = document.getElementById('dark-mode-button');
const mainPageContent = document.querySelector('.main-page-content');
const personalInfoBlock = document.querySelector('.personal-info-block');
const projectsMainTitle = document.querySelector('.projects-main-title');
const projectsBlock = document.querySelector('.projects-block');


darkSwitch.addEventListener('click', () => {
  mainPageContent.classList.toggle('darkmode');
  personalInfoBlock.classList.toggle('darkmode');
  projectsMainTitle.classList.toggle('darkmode');
  projectsBlock.classList.toggle('darkmode');
  if(storedScheme == 'dark'){
    localStorage.setItem('as-scheme', 'light');
  }else{
    localStorage.setItem('as-scheme', 'dark');
  };
})

if(storedScheme == 'dark'){
  mainPageContent.classList.toggle('darkmode');
  personalInfoBlock.classList.toggle('darkmode');
  projectsMainTitle.classList.toggle('darkmode');
  projectsBlock.classList.toggle('darkmode');
  darkSwitch.checked = true
}