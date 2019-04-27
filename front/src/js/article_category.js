function ArticleCategory() {

}

ArticleCategory.prototype.listenAddCategoryEvent = function () {
    var addBtn = $('#add-btn');
    addBtn.click(function () {
    xfzalert.alertOneInput({
            'title': '添加文章分类',
            'placeholder': '请输入文章分类',
            'confirmCallback': function (inpuValue) {
                xfzajax.post({
                    'url': '/cms/add_article_category/',
                    'data': {
                        'name': inpuValue
                    },
                    'success': function (result) {
                        if(result['code'] === 200){
                            console.log(result);
                            window.location.reload();
                        }else{
                            xfzalert.close();
                        }
                    }
                });
            }
        });
    });
};

ArticleCategory.prototype.DeleteArticleCategoryEvent = function(){
  var deleteBtn = $('.delete-btn');
  deleteBtn.click(function () {
      var currentBtn = $(this);
        var tr = currentBtn.parent().parent();
        var pk = tr.attr('data-pk');
        xfzalert.alertConfirm({
            'title': '您确定要删除这个分类吗？',
            'confirmCallback': function () {
                xfzajax.post({
                    'url': '/cms/delete_article_category/',
                    'data': {
                        'pk': pk
                    },
                    'success': function (result) {
                        if(result['code'] === 200){
                            window.location.reload();
                        }
                    }
                });
            }
        });
  });
};

ArticleCategory.prototype.EditArticleCategoryEvent = function(){
    var editBtn = $('.edit-btn');
    editBtn.click(function () {
        var currentBtn = $(this);
        var tr = currentBtn.parent().parent();
        var pk = tr.attr('data-pk');
        var name = tr.attr('data-name');
        xfzalert.alertOneInput({
            'title': '修改分类名称',
            'placeholder': '请输入新的分类名称',
            'value': name,
            'confirmCallback': function (inputValue) {
                xfzajax.post({
                    'url': '/cms/edit_article_category/',
                    'data': {
                        'pk': pk,
                        'name': inputValue
                    },
                    'success': function (result) {
                        if(result['code'] === 200){
                            window.location.reload();
                        }else{
                            xfzalert.close();
                        }
                    }
                });
            }
        });
    })
};

ArticleCategory.prototype.run = function(){
    var self =this;
    self.listenAddCategoryEvent();
    self.DeleteArticleCategoryEvent();
    self.EditArticleCategoryEvent();
};

$(function () {
    var category = new ArticleCategory();
    category.run();
});
