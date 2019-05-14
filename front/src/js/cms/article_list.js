function Article() {
};

Article.prototype.DeleteArticleEvent = function(){
  var deleteBtn = $('.delete-btn');
  deleteBtn.click(function () {
      var currentBtn = $(this);
        var tr = currentBtn.parent().parent();
        var pk = tr.attr('data-pk');
        var category_id = tr.attr('data-name');
        xfzalert.alertConfirm({
            'title': '您确定要删除这篇文章吗？',
            'confirmCallback': function () {
                xfzajax.post({
                    'url': '/cms/article_delete/',
                    'data': {
                        'article_id': pk,
                        'category_id': category_id
                    },
                    'success': function (result) {
                        console.log(result);
                        if (result['code'] === 200) {
                            window.location.reload();
                        }
                    }
                });
            }
        });
  });
};

Article.prototype.EditArticleEvent = function(){
  var editBtn = $(".edit-btn");
  var box_body = $(".box-body");
  editBtn.click(function () {
      var tr = editBtn.parent().parent();
      var pk = tr.attr('data-pk');
      var user_pk = box_body.attr("user-id");
      var token = $('input[name=csrfmiddlewaretoken]').val();
      $.ajax({
          tpye:"get",
          url:'/cms/edit_article/',
          data:{
              user:user_pk,
              article_id:pk,
              csrfmiddlewaretoken: token
          },
          success: function (result) {
           // window.location.href="/cms/write_article/";
          }
      });
  })
};

Article.prototype.run = function(){
    var self =this;
    self.DeleteArticleEvent();
    // self.EditArticleEvent();
};

$(function () {
    var article = new Article();
    article.run();
});
