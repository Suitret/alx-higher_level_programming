$(document).ready(function() {
  // Wait for the DOM to be ready

  // Attach a click event handler to the DIV#red_header element
  $('#red_header').click(function() {
    // Add the class 'red' to the <header> element
    $('header').addClass('red');
  });
})

