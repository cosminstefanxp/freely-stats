
function on_select() {
	// Remove this event handler to avoid double click
	$(this).off('click');
	// Remove element
	$(this).fadeOut('normal', function() {
		$(this).remove();
	});
	// Add a new element to the selected area
	newEntry = $("<div class='job-entry'>" + $(this).text() + "</div>");
	newEntry.hide().prependTo($("#job-selected-cloud")).fadeIn('normal');
	newEntry.click(on_deselect);
	
	// Add the element to the form
	$("#select-jobs-form").append(
			"<input type='text' name='job' hidden value='" + $(this).text() +
			"' data-trend='"+$(this).text()+"']/>");
}

function on_deselect(){
	// Remove this event handler to avoid double click
	$(this).off('click');
	// Remove element
	$(this).fadeOut('normal', function() { $(this).remove(); });
	// Add a new element to the selected area
	newEntry=$("<div class='job-entry'>"+$(this).text()+"</div>");
	newEntry.hide().prependTo($("#job-cloud")).fadeIn('normal');
	newEntry.click(on_select);
	// Find and remove the element from the form
	// find all divs that have custom:attr
	inputElem=$("#select-jobs-form input[data-trend='"+$(this).text()+"']");
	inputElem.remove();
}