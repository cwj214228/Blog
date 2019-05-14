function User() {
    var self = this;
};

User.prototype.initUEditor = function () {
    var self = this;
    window.ue = UE.getEditor('editor',{
        'initialFrameHeight': 400,
        'serverUrl': '/ueditor/upload/',
        initialFrameWidth:"100%"
    });
};


User.prototype.listenSubmitEvent = function () {
    console.log('ssssss')
    var submitBtn = $("#submit-btn");
    var usernameInput = $(".box-body input[name='username']");
    var ageInput = $(".box-body input[name='age']");
    var emailInput = $(".box-body input[name='email']");
    var githubInput = $(".box-body input[name='github']");
    var head_image = $(".box-body input[name='thumbnail']");
    var box_body = $(".box-body");


    submitBtn.click(function () {
        var options=$(".select-sex option:selected");
        var option = options.val();
        var editorInput = window.ue.getContent();
        username = usernameInput.val();
        age = ageInput.val();
        email = emailInput.val();
        console.log(email)
        github = githubInput.val();
        user_pk = box_body.attr("user-id");
        imge = head_image.val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        console.log(imge)
        $.ajax({
            type:"post",
            url:'/cms/write_basicinformation/'+user_pk+'/',
            data:{
                user:user_pk,
                age:age,
                email:email,
                github:github,
                introduction:editorInput,
                sex:option,
                head_image:imge,
                csrfmiddlewaretoken: token
            },
            success: function (result) {
                console.log(result);
                if(result['code'] === 200) {
                    xfzalert.alertSuccess('修改成功！', function () {
                        window.location.reload();
                    });
                }
                else {
                    if(result.message.age){
                        xfzalert.alertErrorToast(result.message.age);
                    }
                    else if(result.message.email){
                        xfzalert.alertErrorToast(result.message.email);
                    }
                    else if(result.message.github){
                        xfzalert.alertErrorToast(result.message.github);
                    }
                    else if(result.message.head_image){
                        xfzalert.alertErrorToast(result.message.head_image);
                    }

                }
            }
        });
    });
};

User.prototype.run = function () {
    var self = this;
    self.initUEditor();
    self.listenSubmitEvent();
};

$(function () {
    var user = new User();
    user.run();
});