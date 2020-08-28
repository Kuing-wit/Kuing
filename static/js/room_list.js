$(document).ready(function(){
     $("input:radio[name='show_list']").click(function(){
          var temp = $("input:radio[name='show_list']:checked").val();
          if (temp == 'all'){
            $("#one_div").show();
            $("#two_div").hide();
            $("#three_div").hide();
            $("#label_one").addClass('click_label').removeClass('unclick_label');
            $("#label_two").addClass('unclick_label').removeClass('click_label');
            $("#label_three").addClass('unclick_label').removeClass('click_label');
          }else if (temp == 'use'){
            $("#one_div").hide();
            $("#two_div").show();
            $("#three_div").hide();
            $("#label_one").addClass('unclick_label').removeClass('click_label');
            $("#label_two").addClass('click_label').removeClass('unclick_label');
            $("#label_three").addClass('unclick_label').removeClass('click_label');
          }else if (temp == 'empty'){
            $("#one_div").hide();
            $("#two_div").hide();
            $("#three_div").show();
            $("#label_one").addClass('unclick_label').removeClass('click_label');
            $("#label_two").addClass('unclick_label').removeClass('click_label');
            $("#label_three").addClass('click_label').removeClass('unclick_label');
          }
    });
});