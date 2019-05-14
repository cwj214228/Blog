function Article() {
    this.progressGroup = $("#progress-group");
}

Article.prototype.initUEditor = function () {
    window.ue = UE.getEditor('editor',{
        'initialFrameHeight': 400,
        'serverUrl': '/ueditor/upload/',
        initialFrameWidth:"100%"
    });
};

Article.prototype.listenQiniuUploadFileEvent = function () {
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
                        mimeType: ['image/png','image/jpeg','image/gif','video/x-ms-wmv']
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

Article.prototype.handleFileUploadProgress = function (response) {
    var total = response.total;
    var percent = total.percent;
    var percentText = percent.toFixed(0)+'%';
    // 24.0909，89.000....
    var progressGroup = Article.progressGroup;
    progressGroup.show();
    var progressBar = $(".progress-bar");
    progressBar.css({"width":percentText});
    progressBar.text(percentText);
};

Article.prototype.handleFileUploadError = function (error) {
    window.messageBox.showError(error.message);
    var progressGroup = $("#progress-group");
    progressGroup.hide();
    console.log(error.message);
};

Article.prototype.handleFileUploadComplete = function (response) {
    console.log(response);
    var progressGroup = $("#progress-group");
    progressGroup.hide();

    var domain = 'http://pqm5g053b.bkt.clouddn.com/';
    var filename = response.key;
    var url = domain + filename;
    var thumbnailInput = $("input[name='thumbnail']");
    thumbnailInput.val(url);
};

Article.prototype.listenSubmitEvent = function () {
    var submitBtn = $("#submit-btn");
    submitBtn.click(function (event) {
        event.preventDefault();
        var btn = $(this);
        var pk = btn.attr('data-news-id');

        var title = $("input[name='title']").val();
        var category = $("select[name='category']").val();
        var desc = $("input[name='desc']").val();
        var thumbnail = $("input[name='thumbnail']").val();
        var content = window.ue.getContent();
        var url = '/cms/write_article/';
        var token = $('input[name=csrfmiddlewaretoken]').val();

        console.log(url);
        console.log(title);
        console.log(category);
        console.log(desc);
        console.log(thumbnail);
        console.log(content);
        console.log(pk);

        $.ajax({
            type:"post",
            url: url,
            data: {
                title: title,
                category: category,
                desc: desc,
                thumbnail: thumbnail,
                content: content,
                pk: pk,
                csrfmiddlewaretoken: token
            },
            success: function (result) {
                if(result['code'] === 200){
                    xfzalert.alertSuccess("发布成功！", function () {
                        window.location.reload();
                    })
                }
            }
        });
    });
};


Article.prototype.ListenEditSubmitEvent = function(){
    var editBtn = $("#edit-btn");
    editBtn.click(function (event) {
        event.preventDefault();
        var btn = $(this);
        var article_id = btn.attr('data-news-id');

        var title = $("input[name='title']").val();
        var category = $("select[name='category']").val();
        var desc = $("input[name='desc']").val();
        var thumbnail = $("input[name='thumbnail']").val();

        var content = window.ue.getContent();

        var url = '/cms/edit_article/';
        var token = $('input[name=csrfmiddlewaretoken]').val();

        console.log(url);
        console.log(title);
        console.log(category);
        console.log(desc);
        console.log(thumbnail);
        console.log(content);
        console.log(article_id);

        $.ajax({
            type:"post",
            url: url,
            data: {
                title: title,
                category: category,
                desc: desc,
                thumbnail: thumbnail,
                content: content,
                article_id: article_id,
                csrfmiddlewaretoken: token
            },
            success: function (result) {
                if(result['code'] === 200){
                    xfzalert.alertSuccess("修改成功！", function () {
                        window.location.reload();
                    })
                }
            }
        });
    });
};

Article.prototype.run = function () {
    var self = this;
    self.initUEditor();
    self.listenQiniuUploadFileEvent();
    self.listenSubmitEvent();
    self.ListenEditSubmitEvent();
};


$(function () {
    var article = new Article();
    article.run();

   Article.progressGroup = $('#progress-group');
});