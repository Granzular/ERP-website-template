const navlist = document.querySelectorAll('.nav-link');
const current_page_href = window.location.href;

for (i of navlist){
    if (i.href == current_page_href){
        i.classList.add('active');
    }
    else{
        i.classList.remove('active');
    }
}

