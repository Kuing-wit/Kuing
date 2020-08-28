$(document).ready(function(){
     $("input:radio[name='show_list']").click(function(){
          var temp = $("input:radio[name='show_list']:checked").val();
          if (temp == 'all'){
            $("#one_div").show();
            $("#two_div").hide();
            $("#three_div").hide();
          }else if (temp == 'use'){
            $("#one_div").hide();
            $("#two_div").show();
            $("#three_div").hide();
          }else if (temp == 'empty'){
            $("#one_div").hide();
            $("#two_div").hide();
            $("#three_div").show();
          }
    });
});