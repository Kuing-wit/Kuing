$(document).ready(function(){
    // 모든 약관 동의 확인

    $('#checkout').click(function(){
        $("input:radio[name='day_of_the_week']").prop("checked",false)
        $("input:radio[name='floor']").prop("checked",false)
            $("#mon_label").addClass('day_box').removeClass('click_day_box');
            $("#tue_label").addClass('day_box').removeClass('click_day_box');
            $("#wed_label").addClass('day_box').removeClass('click_day_box');
            $("#thu_label").addClass('day_box').removeClass('click_day_box');
            $("#fri_label").addClass('day_box').removeClass('click_day_box');
            $("#all_label").addClass('floor_box').removeClass('click_floor_box');
            $("#one_label").addClass('floor_box').removeClass('click_floor_box');
            $("#two_label").addClass('floor_box').removeClass('click_floor_box');
            $("#three_label").addClass('floor_box').removeClass('click_floor_box');

    });

    $("input:radio[name='day_of_the_week']").click(function(){
          var temp = $("input:radio[name='day_of_the_week']:checked").val();
          if (temp == 'mon'){
            $("#mon_label").addClass('click_day_box').removeClass('day_box');
            $("#tue_label").addClass('day_box').removeClass('click_day_box');
            $("#wed_label").addClass('day_box').removeClass('click_day_box');
            $("#thu_label").addClass('day_box').removeClass('click_day_box');
            $("#fri_label").addClass('day_box').removeClass('click_day_box');
          }else if (temp == 'tue'){
            $("#mon_label").addClass('day_box').removeClass('click_day_box');
            $("#tue_label").addClass('click_day_box').removeClass('day_box');
            $("#wed_label").addClass('day_box').removeClass('click_day_box');
            $("#thu_label").addClass('day_box').removeClass('click_day_box');
            $("#fri_label").addClass('day_box').removeClass('click_day_box');
          }else if (temp == 'wed'){
            $("#mon_label").addClass('day_box').removeClass('click_day_box');
            $("#tue_label").addClass('day_box').removeClass('click_day_box');
            $("#wed_label").addClass('click_day_box').removeClass('day_box');
            $("#thu_label").addClass('day_box').removeClass('click_day_box');
            $("#fri_label").addClass('day_box').removeClass('click_day_box');
          }else if (temp == 'thu'){
            $("#mon_label").addClass('day_box').removeClass('click_day_box');
            $("#tue_label").addClass('day_box').removeClass('click_day_box');
            $("#wed_label").addClass('day_box').removeClass('click_day_box');
            $("#thu_label").addClass('click_day_box').removeClass('day_box');
            $("#fri_label").addClass('day_box').removeClass('click_day_box');
          }else if (temp == 'fri'){
            $("#mon_label").addClass('day_box').removeClass('click_day_box');
            $("#tue_label").addClass('day_box').removeClass('click_day_box');
            $("#wed_label").addClass('day_box').removeClass('click_day_box');
            $("#thu_label").addClass('day_box').removeClass('click_day_box');
            $("#fri_label").addClass('click_day_box').removeClass('day_box');
          }
    });
        $("input:radio[name='floor']").click(function(){
          var temp = $("input:radio[name='floor']:checked").val();
          if (temp == 'all'){
            $("#all_label").addClass('click_floor_box').removeClass('floor_box');
            $("#one_label").addClass('floor_box').removeClass('click_floor_box');
            $("#two_label").addClass('floor_box').removeClass('click_floor_box');
            $("#three_label").addClass('floor_box').removeClass('click_floor_box');
          }else if (temp == '1'){
            $("#all_label").addClass('floor_box').removeClass('click_floor_box');
            $("#one_label").addClass('click_floor_box').removeClass('floor_box');
            $("#two_label").addClass('floor_box').removeClass('click_floor_box');
            $("#three_label").addClass('floor_box').removeClass('click_floor_box');
          }else if (temp == '2'){
            $("#all_label").addClass('floor_box').removeClass('click_floor_box');
            $("#one_label").addClass('floor_box').removeClass('click_floor_box');
            $("#two_label").addClass('click_floor_box').removeClass('floor_box');
            $("#three_label").addClass('floor_box').removeClass('click_floor_box');
          }else if (temp == '3'){
            $("#all_label").addClass('floor_box').removeClass('click_floor_box');
            $("#one_label").addClass('floor_box').removeClass('click_floor_box');
            $("#two_label").addClass('floor_box').removeClass('click_floor_box');
            $("#three_label").addClass('click_floor_box').removeClass('floor_box');
          }
    });
});