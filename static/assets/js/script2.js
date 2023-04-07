scrollers = document.getElementsByClassName("slimScrollBar")
for(const scroll of scrollers){
	
	scroll.addEventListener("mousedown", function(event){
		console.log(event.clientX);
		
	})
}


function selectAll(el, me){
	let els = el.getElementsByClassName("text-center");
	for(const e of els){
		var x = e.children[0];
		
		if(me.checked == true){
			x.checked = true;
		}
		if(me.checked == false){
			x.checked = false;
		}
	}
}

function getEmployees(){
	fetch("/api/v1/getEmployees")
	.then((response) => response.json())
	.then((data) => {
		data =JSON.stringify(data);
		data = JSON.parse(data);
		console.log(data);
	})
}