$().ready(function(){
	//user guide to select a group
	$("#J_GroupCateList .cate-item").each(function(){
		$(this).click(function(){
			//alert(this.innerHTML)
			$(".cate-item").removeClass("active")
			$(this).addClass("active")
			//var dataid = $(this).attr("data-id")
			var rel = $(this).attr("rel")
			
			$("#J_GroupsPanel .cate-group-list").each(function(){
				if(this.id == rel){
					$(".cate-group-list").removeClass("active")
					$(this).addClass("active")
				}
			});
		})
	});
	
	$.ajaxSetup({
	  data: {csrfmiddlewaretoken: csrf_token  },
	});
	
	var groupnum = 0
	$(".group-item span").click(function(){
		var groupToJoin = $(this).attr("data-id")
		var span = $(this)
		if(currentUser == "AnonymousUser"){
			art.dialog({
				lock: true,
				content: "尚未登录,去登录<br/><a href='/group/login'>登录</a>",
				id: 'EF893L',
				ok: function () {
					
				}
			});
			return false;
		}
		
		var jqxhr = $.post("/group/join",{ user: currentUser, group: groupToJoin })
					.done(function(data) {
						//alert("success"+data);
						if(data == '-1'){
							$(span).html("已经是小组成员了")
						}
						if (data == '0'){
							$(span).html("已加入")
							groupnum++
						}
						$("#J_StartGroup").addClass("active")
						$("#J_JoinedGroupsNum").html(groupnum)
					});
		//alert($(this).attr("data-id"))
	});
	
});
