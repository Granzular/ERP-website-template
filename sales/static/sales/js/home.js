function handleAlert(type,msg,elID){                           const alertbox = document.getElementById(elID);                                              alertbox.innerHTML = `
                        <div class="alert alert-${type}" role="alert">                                                      ${msg}                                            </div>                                            `                                         }

Dropzone.autoDiscover = false;
	var myDropzone = new Dropzone("#myDropzone",{
		url:"/sales/upload_csv/",
		paramName:"file",
		maxFilesize:1,
		acceptFiles:".csv",
		params: {csrfmiddlewaretoken:document.getElementsByName('csrfmiddlewaretoken')[0].value}
	});
		myDropzone.on("success",()=>{handleAlert("success","file uploaded","dz-alert-box")});

		myDropzone.on("error",(file,errmsg)=>{handleAlert("danger","An error occured: "+errmsg,"dz-alert-box")});
		

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
		e.preventDefault();
		const name = document.getElementById("id_name").value;                                              const remark = document.getElementById("id_remark").value;                                          const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
		const formdata = new FormData();
		formdata.append('name',name);
		formdata.append('remark',remark);
		formdata.append('image',img.src);
		formdata.append('csrfmiddlewaretoken',csrf);

		$.ajax(
			{
				type:'POST',
				url:'/reports/save/',
				data:formdata,
				success:(r)=>{handleAlert("success","Report Created Successfully","alert-box")},
				error:(r)=>{handleAlert("danger","an error occured","alert-box")},
				processData:false,
				contentType:false

			}
		)

	}
	,false);

},false);
