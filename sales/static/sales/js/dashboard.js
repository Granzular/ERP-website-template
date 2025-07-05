window.addEventListener("load",registerEvents,false);

function registerEvents(e){

    const sidebarBtn = document.querySelector('.sidebar-btn');
    document.querySelector(".frame1").append(sidebarBtn);
    document.querySelector(".sidebar-btn").addEventListener("click",(e)=>{
        
       let sidebar = document.querySelector(".sidebar");
       if (sidebar.classList.contains("hidden")){
        sidebar.classList.remove("hidden");
         document.getElementsByClassName("sidebar-icon")[0].src = "/media/icon/closeicon.png"
       }
       else{
        sidebar.classList.add("hidden");
         document.getElementsByClassName("sidebar-icon")[0].src = "/media/icon/menuicon.png"
       }
    },false);

    
}