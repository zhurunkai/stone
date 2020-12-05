jQuery(document).ready(function () {
	var accordionsMenu = $('.cd-accordion-menu');

	if (accordionsMenu.length > 0) {

		accordionsMenu.each(function () {
			var accordion = $(this);
			//detect change in the input[type="checkbox"] value
			accordion.on('change', 'input[type="checkbox"]', function () {
				var checkbox = $(this);
				console.log(checkbox.prop('checked'));
				(checkbox.prop('checked')) ? checkbox.siblings('ul').attr('style', 'display:none;').slideDown(300): checkbox.siblings('ul').attr('style', 'display:block;').slideUp(300);
			});
		});
	}
});

$("label").click(function (e) {
	let iframe = document.getElementById("iframe")
	switch (this.innerText) {
		case "用户管理":
			iframe.src = "/manage/user_manage/"
			break;
		case "社区管理" || "帖子":
			iframe.src = "/manage/forum_task/"
			break;
		case "待审核":
			iframe.src = "/manage/forum_task/"
			break;
		case "系统管理":
			iframe.src = "/manage/system_state/"
			break;
		case "反馈与建议":
			iframe.src = "/manage/feedback/"
			break;
	}
})