$(document).ready(function(){
    $('#id_department').change(function(){
      var department_id = $(this).val();
      $.ajax({
        url: '/load_courses/',
        data: {'department_id': department_id},
        dataType: 'json',
        success: function(data){
          var options = '<option value="">Select Course</option>';
          for(var i=0; i<data.length; i++){
            options += '<option value="' + data[i].id + '">' + data[i].course + '</option>';
          }
          $('#id_course').html(options);
        }
      });
    
    });
  });