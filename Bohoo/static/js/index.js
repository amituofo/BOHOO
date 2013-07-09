$().ready(function(){
	//complete user info @category @image
	/*if(category == '' || image == ''){
		art.dialog({
			lock: true,
			content: document.getElementById('completeDialog'),
			id: 'EF893L',
			ok: function () {
				
			}
		});
	}*/
	
	$(".bn-post1").click(function(event){
		event.preventDefault();
		if ($("#canspeak").attr("data-id") == '-1'){
			art.dialog({
			title:"只有加入小组才能发言",
			width:180,
			height:50,
			content: document.getElementById('join-group'),
			id: 'EF893L',
			ok: function () {
				
			}
		});
		}else if($("#canspeak").attr("data-id") == '0'){
			location.href = $(".bn-post1").attr("href")
		}
	});

});
