function User() {
    var self = this;
};

User.prototype.listenSubmitEvent = function () {
    var submitBtn = $("#submit-btn");
    var starttimeInput = $(".box-body input[name='starttime']");
    var endtimeInput = $(".box-body input[name='endtime']");
    var positionInput = $(".box-body input[name='position']");
    var work1Input = $(".box-body input[name='work1']");
    var work2Input = $(".box-body input[name='work2']");
    var work3Input = $(".box-body input[name='work3']");
    var work4Input = $(".box-body input[name='work4']");
    var work5Input = $(".box-body input[name='work5']");
    var skill1Input = $(".box-body input[name='skill1']");
    var skill2Input = $(".box-body input[name='skill2']");
    var skill3Input = $(".box-body input[name='skill3']");
    var skill4Input = $(".box-body input[name='skill4']");
    var skill5Input = $(".box-body input[name='skill5']");
    var box_body = $(".box-body");


    submitBtn.click(function () {
        start_time = starttimeInput.val();
        end_time = endtimeInput.val();
        position = positionInput.val();
        work_one = work1Input.val();
        work_two = work2Input.val();
        work_three = work3Input.val();
        work_four = work4Input.val();
        work_five = work5Input.val();

        work_skill_one = skill1Input.val();
        work_skill_two = skill2Input.val();
        work_skill_three = skill3Input.val();
        work_skill_four = skill4Input.val();
        work_skill_five= skill5Input.val();

        user_pk = box_body.attr("user-id");

        var token = $('input[name=csrfmiddlewaretoken]').val();
        console.log('6666666666666666666666666666666666');
        $.ajax({
            type:"post",
            url:'/cms/work_experience/'+user_pk+'/',
            data:{
                'start_time':start_time,
                end_time:end_time,
                position:position,
                work_one:work_one,
                work_two:work_two,
                work_three:work_three,
                work_four:work_four,
                work_five:work_five,
                work_skill_one:work_skill_one,
                work_skill_two:work_skill_two,
                work_skill_three:work_skill_three,
                work_skill_four:work_skill_four,
                work_skill_five:work_skill_five,
                csrfmiddlewaretoken: token
            },
            success: function (result) {
                console.log(result);
                if(result['code'] === 200) {
                    xfzalert.alertSuccess('修改成功！', function () {
                        window.location.reload();
                    });
                }
            }
        });
    });
};

User.prototype.run = function () {
    var self = this;
    self.listenSubmitEvent();
};

$(function () {
    var user = new User();
    user.run();
});