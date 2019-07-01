function Banners() {
    var self = this;
    var img;
};

Banners.prototype.ListenAddBannerEvent = function(){
    var self = this;
    var addbtn = $('#add-banner-btn');
    addbtn.click(function () {
        var tpl = template("banner-item");
        var bannerListGroup = $(".banner-list-group");
        bannerListGroup.prepend(tpl);
        var bannerItem = bannerListGroup.find(".banner-item:first");
        self.addImageSelectEvent(bannerItem);
        self.RemoveImageBannerEvent(bannerItem);
        self.addSaveBannerEvent(bannerItem);
    });
};

Banners.prototype.addImageSelectEvent = function(bannerItem){
    var self = this;
    var image = bannerItem.find('.thumbnail');
    img = image;
    var imageInput = bannerItem.find('.image-input');
    image.click(function () {
        imageInput.click();
    });
    imageInput.change(function () {
       var file = this.files[0];
       $.ajax({
           type: "get",
           url:  '/cms/qntoken/',
           success: function (result) {
                if(result['code'] === 200){
                    var token = result['data']['token'];
                    console.log(result);

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
       })
    });
};

Banners.prototype.handleFileUploadProgress = function (response) {

};

Banners.prototype.handleFileUploadError = function (error) {
    window.messageBox.showError(error.message);
    console.log(error.message);
};

Banners.prototype.handleFileUploadComplete = function (response) {
    var self = this;
    var domain = 'http://myheartsky.com/';
    var filename = response.key;
    var url = domain + filename;
    img.attr('src',url);
};

Banners.prototype.RemoveImageBannerEvent = function(bannerItem){
    var removeBtn = bannerItem.find(".close-btn");
    var bannerId = bannerItem.attr('data-banner-id');
    var token = $('input[name=csrfmiddlewaretoken]').val();
    removeBtn.click(function () {
        if (bannerId) {
            xfzalert.alertConfirm({
                'text': '您确定要删除这个轮播图吗？',
                'confirmCallback': function () {
                    $.ajax({
                        type: "post",
                        url: "/cms/delete_banner/",
                        data: {
                            banner_id: bannerId,
                            csrfmiddlewaretoken: token
                        },
                        success: function (result) {
                            if(result['code']===200){
                                bannerItem.remove();
                                window.messageBox.showSuccess("删除成功！");
                            }else {
                                window.messageBox.showError("删除失败！")
                            }
                        }
                    })
                }
            })
        } else {
            bannerItem.remove();
        }
    });
};

Banners.prototype.addSaveBannerEvent = function(bannerItem){
    var saveBtn = bannerItem.find('.save-btn');
    var imageTag = bannerItem.find('.thumbnail');
    var priorityTag = bannerItem.find("input[name='priority']");
    var linktoTag = bannerItem.find("input[name='link_to']");
    var prioritySpan = bannerItem.find("span[class='priority']");
    var banner_id = bannerItem.attr('data-banner-id');


    saveBtn.click(function () {
        console.log(banner_id);
        var image_url = imageTag.attr("src");
        var priority = priorityTag.val();
        var link_to = linktoTag.val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        console.log(banner_id);
        var post_url = '';
        if (!banner_id){
            post_url = "/cms/add_banner/";
            $.ajax({
            type: "post",
            url: post_url,
            data:{
                priority:priority,
                image_url:image_url,
                link_to:link_to,
                csrfmiddlewaretoken: token
            },
            success:function (result) {
                if(result['code']===200){
                    var bannerId = result['data']['banner_id'];
                    prioritySpan.text("优先级："+bannerId);
                    window.messageBox.showSuccess("轮播图添加完成！")
                }
            }
        })
        } else {
            post_url = "/cms/edit_banner/";
            console.log(priority);
            console.log(image_url);
            console.log(link_to);
            console.log(banner_id);
            $.ajax({
                type: "post",
                url: post_url,
                data: {
                    priority: priority,
                    image_url: image_url,
                    link_to: link_to,
                    banner_id: banner_id,
                    csrfmiddlewaretoken: token
                },
                success: function (result) {
                    console.log(result);
                    if (result['code'] === 200) {
                        var bannerId = result['data']['banner_id'];
                        prioritySpan.text("优先级：" + bannerId);
                        window.messageBox.showSuccess("轮播图修改完成！")
                    }
                }
            })
        }
    });
};

Banners.prototype.loadData = function(){
    var self = this;
    $.ajax({
        type:"get",
        url: "/cms/banner_list/",
        success: function (result) {
            if(result['code']===200){
                var banners = result.data;
                for(var i=0; i<banners.length; i++){
                    var banner = banners[i];
                    var tpl = template("banner-item", {"banner":banner});
                    var bannerListGroup = $(".banner-list-group");
                    bannerListGroup.append(tpl);
                    var bannerItem = bannerListGroup.find(".banner-item:last");
                    self.addImageSelectEvent(bannerItem);
                    self.RemoveImageBannerEvent(bannerItem);
                    self.addSaveBannerEvent(bannerItem);
                }
            }
        }
    })
};

// Banners.prototype.EditBannerEvent = function(){
//
// };


Banners.prototype.run = function () {
    this.ListenAddBannerEvent();
    this.loadData();
};

$(function () {
   var banners = new Banners();
   banners.run();
});