$(document).ready(function() {
  // Wait for the DOM to be ready

  // Attach a click event handler to the DIV#red_header element
  $('#red_header').click(function() {
    // Update the text color of the <header> element to red
    $('header').css('color', '#FF0000');
  });
});

