const user_type_widgets = document.getElementsByName('user_type');
const public_key_widget = document.getElementsByName('public_key')[0];
const public_key_div = document.querySelector('#public_key_div ');


[...user_type_widgets].map((w)=>{w.addEventListener('click',(e)=>{
	if (e.target.value == "staff"){
		public_key_widget.setAttribute("required",true);
		public_key_widget.value = '';
		public_key_div.removeAttribute("hidden");
		
		
	}
	else{
		public_key_widget.value = '123456789'
			public_key_widget.required = false
		public_key_div.setAttribute("hidden","true");
		
	;
		
		
	}
	
},false);})


