window.addEventListener('load',(e)=>{
	const img = document.getElementById("img");
const reportBtn = document.getElementById("report-btn");
const modalBody = document.getElementById("modal-body");
const reportForm= document.getElementById("report-form");

	reportBtn.addEventListener('click',
	(e)=>{
		img.setAttribute("class","w-100");
		modalBody.prepend(img);
	}
	,false);
	reportForm.addEventListener("submit",(e)=>{
		const name = document.getElementById("id_name").value;                                              const remark = document.getElementById("id_remark").value;                                          const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
		e.preventDefault();
		const formdata = new FormData();
		formdata.append('name',name);
		formdata.append('remark',remark);
		formdata.append('image',img.src);
		formdata.append('csrfmiddlewaretoken',csrf);
		function handleAlert(type,msg){
			const alertbox = document.getElementById("alert-box");
			alertbox.innerHTML = `
			<div class="alert alert-${type}" role="alert">
			${msg}
			</div>
			`
		}
		$.ajax(
			{
				type:'POST',
				url:'/reports/save/',
				data:formdata,
				success:(r)=>{handleAlert("success","Report Created Successfully")},
				error:(r)=>{handleAlert("danger","an error occured")},
				processData:false,
				contentType:false,

			}
		)

	}
	,false);

},false);
