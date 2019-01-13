
function bindclient(c){
    $.ajax({
      url:"clientpriority",
      type:"GET",
      data: {client: c},
      success:function(data){
        var jsonData = JSON.parse(data);

        var options = ""
        for (var i=0; i < jsonData.length; i++)
            options += "<option selected='' value='" + jsonData[i] + "'>" + jsonData[i] +"</option>";
        $("#client_priority")[0].innerHTML = options
      },
      cache:false,
      failure: function(errMsg) {
        console.log(errMsg);
      }
    });
  }

$(document).ready(function (){

  $('#client').change(function(e) {
    var client = this.value;
    bindclient(client);
  });

}); // Closing Ready Event



