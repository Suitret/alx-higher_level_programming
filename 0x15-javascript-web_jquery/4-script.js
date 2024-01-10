$(document).ready(function() {
  // Wait for the DOM to be ready

  // Attach a click event handler to the DIV#toggle_header element
  $('#toggle_header').click(function() {
    // Toggle the class 'red' and 'green' on the <header> element
    $('header').toggleClass('red green');
  });
});

