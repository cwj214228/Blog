function User() {
    var self = this;
};

User.prototype.initUEditor = function () {
    window.ue = UE.getEditor('editor',{
        'initialFrameHeight': 400,
        'serverUrl': '/ueditor/upload/'
    });
};



User.prototype.run = function () {
    var self = this;
    self.initUEditor();
    // self.listenSubmitEvent();
};


$(function () {
    var user = new User();
    user.run();
});
