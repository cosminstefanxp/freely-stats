function newSelection(name){
	$("#text-main").hide();
	$("#text-tech").hide();
	$("#text-analysis").hide();
	$($(this).attr("data-target")).fadeIn();
}