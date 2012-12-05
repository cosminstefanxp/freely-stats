
function on_select(name) {
	// Remove this event handler to avoid double click
	$(this).off('click');
	// Remove element
	$(this).fadeOut('normal', function() {
		$(this).remove();
	});
	// Add a new element to the selected area
	newEntry = $("<div class='select-entry'>" + $(this).text() + "</div>");
	newEntry.hide().appendTo($("#selected-list")).fadeIn('normal');
	newEntry.click(on_deselect);
	
	// Add the element to the form
	$("#select-form").append(
			"<input type='text' name='"+$("#select-form").attr("data-filter")+"' class='hidden' value='" + $(this).text() +"']/>");
}

function on_deselect(){
	// Remove this event handler to avoid double click
	$(this).off('click');
	// Remove element
	$(this).fadeOut('normal', function() { $(this).remove(); });
	// Add a new element to the selected area
	newEntry=$("<div class='select-entry'>"+$(this).text()+"</div>");
	newEntry.hide().prependTo($("#selection-cloud")).fadeIn('normal');
	newEntry.click(on_select);
	// Find and remove the element from the form
	inputElem=$("#select-form input[value='"+$(this).text()+"']");
	inputElem.remove();
}