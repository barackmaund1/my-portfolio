$(document).ready(function(){
    $('form').submit(function(event){
      event.preventDefault()
      form = $("form")
  
      $.ajax({
        'url':'/ajax/newsletter/',
        'type':'POST',
        'data':form.serialize(),
        'dataType':'json',
        'success': function(data){
          Swal.fire(
            '',
            data['success'],
            'success'
          )
        },
      })// END of Ajax method
      $('#id_name').val('')
      $("#id_email").val('')
      $("#id_subject").val('')
      $("#id_message").val('')
    }) // End of submit event
  
  }) // End of document ready function