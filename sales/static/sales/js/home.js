const img = document.getElementById("img");
const reportBtn = document.getElementById("report-btn");
const modalBody = document.getElementById("modal-body");

reportBtn.addEventListener('click',
	(e)=>{
		img.setAttribute("class","w-100");
		modalBody.prepend(img);
	}
	,false);
