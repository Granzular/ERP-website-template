window.addEventListener("load",registerEvents,false);

function registerEvents(e){
/* the below block of code displays the framex that shows the profile pic in full screen*/    document.querySelector("#profile-pic").addEventListener("click",(e)=>{
        const framex = document.getElementById("framex");
        framex.style.display="block";
        
    },false);
  /* the below code reverses the profile pic fullscreen effect*/  document.querySelector("#menubar-return").addEventListener("click",(e)=>{
        const framex = document.getElementById("framex");
        framex.style.display="none";
    },false);
    
    /* code that controls editing profile pic */
     document.querySelector("#edit-profile-pic").addEventListener('click',(e)=>{ 
e.preventDefault();
             const fd = document.querySelector("#fileupload");
             fd.click()
             fd.addEventListener("input",(e)=>{
                     document.querySelector("#profile_pic_form").submit();
             })
     },false);
        
        
}