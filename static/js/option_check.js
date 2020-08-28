$(document).ready(function(){
    // 모든 약관 동의 확인

    $('#checkout').click(function(){
        $("input:radio[name='day_of_the_week']").prop("checked",false)
        $("input:radio[name='floor']").prop("checked",false)
    });
});