function Index() {
    var self = this;
    self.category_id = 0;
}

Index.prototype.listenCategorySwitchEvent = function () {
    var self = this;
    var tabGroup = $("#blogtab");
    tabGroup.children().click(function () {
        // this：代表当前选中的这个li标签
        var li = $(this);
        var category_id = li.attr("data-category");
        xfzajax.get({
            'url': '/article/list/',
            'data': {
                'category_id': category_id
            },
            'success': function (result) {
                if(result['code'] === 200){
                    var artlcles = result['data'];
                    var tpl = template("article-item",{"artlcles":artlcles});
                    // empty：可以将这个标签下的所有子元素都删掉
                    var newsListGroup = $(".list-inner-group");
                    newsListGroup.empty();
                    newsListGroup.append(tpl);
                    self.category_id = category_id;
                    li.addClass('active').siblings().removeClass('active');
                }
            }
        });
    });
};

Index.prototype.run = function () {
    var self = this;
    self.listenCategorySwitchEvent();
};

$(function () {
    var index = new Index();
    index.run();
});