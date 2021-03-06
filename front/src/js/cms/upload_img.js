function Image() {
    this.progressGroup = $("#progress-group");
    this.progressGroup = $("#progress-group2");
}

Image.prototype.listenQiniuWechatEvent = function () {
    var self = this;
    var uploadBtn = $('#wechat-btn');
    uploadBtn.change(function () {
        var file = this.files[0];
        xfzajax.get({
            'url': '/cms/qntoken/',
            'success': function (result) {
                if(result['code'] === 200){
                    var token = result['data']['token'];
                    // a.b.jpg = ['a','b','jpg']
                    // 198888888 + . + jpg = 1988888.jpg
                    var key = (new Date()).getTime() + '.' + file.name.split('.')[1];
                    var putExtra = {
                        fname: key,
                        params:{},
                        mimeType: ['image/png','image/jpeg','image/gif']
                    };
                    var config = {
                        useCdnDomain: true,
                        retryCount: 6,
                        region: qiniu.region.z2
                    };
                    var observable = qiniu.upload(file,key,token,putExtra,config);
                    observable.subscribe({
                        'next': self.handleFileUploadProgress2,
                        'error': self.handleFileUploadError2,
                        'complete': self.handleFileUploadComplete2
                    });
                }
            }
        });
    });
};

Image.prototype.listenQiniuUploadFileEvent = function () {
    var self = this;
    var uploadBtn = $('#thumbnail-btn');
    uploadBtn.change(function () {
        var file = this.files[0];
        xfzajax.get({
            'url': '/cms/qntoken/',
            'success': function (result) {
                if(result['code'] === 200){
                    var token = result['data']['token'];
                    // a.b.jpg = ['a','b','jpg']
                    // 198888888 + . + jpg = 1988888.jpg
                    var key = (new Date()).getTime() + '.' + file.name.split('.')[1];
                    var putExtra = {
                        fname: key,
                        params:{},
                        mimeType: ['image/png','image/jpeg','image/gif']
                    };
                    var config = {
                        useCdnDomain: true,
                        retryCount: 6,
                        region: qiniu.region.z2
                    };
                    var observable = qiniu.upload(file,key,token,putExtra,config);
                    observable.subscribe({
                        'next': self.handleFileUploadProgress,
                        'error': self.handleFileUploadError,
                        'complete': self.handleFileUploadComplete
                    });
                }
            }
        });
    });
};

Image.prototype.handleFileUploadProgress = function (response) {
    var total = response.total;
    var percent = total.percent;
    var percentText = percent.toFixed(0)+'%';
    // 24.0909，89.000....
    var progressGroup = Image.progressGroup;
    progressGroup.show();
    var progressBar = $(".progress-bar");
    progressBar.css({"width":percentText});
    progressBar.text(percentText);
};

Image.prototype.handleFileUploadError = function (error) {
    window.messageBox.showError(error.message);
    var progressGroup = $("#progress-group");
    progressGroup.hide();
    console.log(error.message);
};

Image.prototype.handleFileUploadComplete = function (response) {
    console.log(response);
    var progressGroup = $("#progress-group");
    progressGroup.hide();

    var domain = 'http://myheartsky.com/';
    var filename = response.key;
    var url = domain + filename;
    var thumbnailInput = $("input[name='thumbnail']");
    thumbnailInput.val(url);
};

Image.prototype.handleFileUploadProgress2 = function (response) {
    var total = response.total;
    var percent = total.percent;
    var percentText = percent.toFixed(0)+'%';
    // 24.0909，89.000....
    var progressGroup = Image.progressGroup;
    progressGroup.show();
    var progressBar = $(".progress-bar2");
    progressBar.css({"width":percentText});
    progressBar.text(percentText);
};

Image.prototype.handleFileUploadError2 = function (error) {
    window.messageBox.showError(error.message);
    var progressGroup = $("#progress-group2");
    progressGroup.hide();
    console.log(error.message);
};

Image.prototype.handleFileUploadComplete2 = function (response) {
    console.log(response);
    var progressGroup = $("#progress-group2");
    progressGroup.hide();

    var domain = 'http://myheartsky.com/';
    var filename = response.key;
    var url = domain + filename;
    var thumbnailInput = $("input[name='wechat-thumbnail']");
    thumbnailInput.val(url);
};

Image.prototype.run = function () {
    var self = this;
    self.listenQiniuUploadFileEvent();
    self.listenQiniuWechatEvent();
};

$(function () {
    var image = new Image();
    image.run();

   Image.progressGroup = $('#progress-group');
});