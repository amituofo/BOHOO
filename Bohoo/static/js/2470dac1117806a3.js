
Do(function(){
  var popup;var nav=$("#db-global-nav");var more=nav.find(".bn-more");nav.delegate(".bn-more, .top-nav-reminder .lnk-remind","click",function(c){c.preventDefault();var a=$(this);var b=a.parent();if(popup){popup.parent().removeClass("more-active");if($.contains(b[0],popup[0])){popup=null;return false}}b.addClass("more-active");popup=b.find(".more-items");popup.trigger("moreitem:show");return false});$(document).click(function(a){if($(a.target).closest(".more-items").length){return}if(popup){popup.parent().removeClass("more-active");popup=null}});
});

	Do = (typeof Do === 'undefined')? $ : Do;
	Do(function(){
      var reportDiv = "#link-report".concat("");
      $("body").delegate(reportDiv, 'mouseenter mouseleave', function(e){

        switch (e.type) {
          case "mouseenter":
            $(this).find(".report").css('visibility', 'visible');
            break;
          case "mouseleave":
            $(this).find(".report").css('visibility', 'hidden');
            break;
        }
      });
      $(reportDiv).delegate(".report a", 'click', function(e){
          e.preventDefault();
          var auditUrl = "http://www.douban.com/misc/audit_report?url=",
              opt = "";
          var obj = $(e.target).closest(reportDiv);
          var id = obj.length != 0 ? obj.data("id") : undefined;
          var params = (opt&&id) ? '?'.concat(opt, '=', id) : '';
          var url = "http://www.douban.com/group/topic/38131596/".concat(params);
          generate_report_dialog({report_url: url});
      });

      $(reportDiv).append('<div class="report"><a rel="nofollow" href="javascript:void(0)">举报</a></div>');
  });

        (typeof Do === 'function' ? Do : $).call(null, function(){
                if (typeof hasInitFavBtn !== 'undefined') {
                    return;
                }
                var fav_type = 'fav_note'; 
                var fav_url = 'http://www.douban.com/group/topic/38131596/?type=like#sep'; 
                hasInitFavBtn = 1;
                $('html').delegate('.btn-fav', 'click', function(e) {
                    e.preventDefault();
                    var self = $(e.currentTarget),
                        hasFav = self.hasClass('fav-cancel') ? 1 : 0,
                        paras = {
                            tid: self.data('tid'),
                            tkind: self.data('tkind'),
                            ck: get_cookie('ck') 
                        };

                    if (self.hasClass('stat-processing')) {
                        return;
                    }

                    self.addClass('stat-processing');

                    $.ajax({
                        type: hasFav ? 'delete' : 'post',
                        url: '/j/like',
                        data: paras,
                        success: function (o) {
                            self.removeClass('stat-processing');
                            if (o.r === 0) {
                                if (hasFav) {
                                    self.removeClass('fav-cancel').addClass('fav-add').attr('title', '标为喜欢?');
                                    updateFavNum(self, -1);
                                } else {
                                    self.removeClass('fav-add').addClass('fav-cancel').attr('title', '取消喜欢?');
                                    updateFavNum(self, 1);
                                }
                            }
                        },
                        dataType: 'json'
                    });
                });

                
var api_userlist = 'http://www.douban.com/j/like',
$win = $(window),
updateFavNum = function(node, n) {
  var p = node.parent(), favNum = p.find('.fav-num'), num;

  if (favNum.length === 0) {
  // 日记的情况
    favNum = p.find('.fav-num-note');
  }

  $('#fav-userlist').hide();
  if (favNum.length === 0) {
    favNum = $(['<span class="fav-num" data-tkind="', node.data('tkind'),'" data-tid="', node.data('tid'),'"><a href="' + fav_url + '">0人</a>喜欢</span>'].join(''));
    p.prepend(favNum);
  }

  num = parseInt(favNum.find('a').text(),10) + n;
  if (num === 0) {
    favNum.remove();
    return;
  }
  favNum.find('a').text(num + '人');
},
renderUserList = function(node, da) {
  if (!$.isArray(da)) {
    $('#fav-userlist').hide();
    return;
  }

  var i = 0, o, pos, h, htmlstr = ['<ul>'];
  if (da.length > 0){
      for (; o = da[i++]; ) {
        htmlstr.push([
         '<li>',
         '<a href="http://www.douban.com/people/', o.uid, '" target="_blank" class="pic"><img src="', o.icon_avatar,'" width="24" height="24"></a>',
         '<a href="http://www.douban.com/people/', o.uid, '" target="_blank">', o.screen_name,'</a>',
         '</li>'
        ].join(''));
      }
      htmlstr.push('</ul>');
  } else {
      htmlstr = ['<span>啊哦…喜欢这个的人都不愿意露脸</span>'];
  }


  node.removeClass('arrow-bottom').find('.bd').css({
    height: i > 9 ? 220 : 'auto',
    overflow: i > 9 ? 'auto' : 'hidden'
  }).html(htmlstr.join(''));

  pos = node.offset();
  h = node.height();

  if (pos.top - $win.scrollTop() + h > $win.height() - 40) {
    node.addClass('arrow-bottom').css('top', pos.top - h - 55);
  }
};

$('html').bind('click', function(e) {
  var list = $('#fav-userlist');
  if (list.length === 0 ||
      list.css('display') === 'none' ||
      e.target.tagName === 'A') {
    return;
  }
  if (!$.contains(list[0], e.target)) {
    list.hide();
  }
});

$('html').delegate('.fav-num a', 'click', function(e) {
  if (fav_type !== 'default') {
    return;
  }
  e.preventDefault();
  var el = $(e.currentTarget),
  pos = el.offset(),
  params = el.parent().data(),
  dataId = [params.tkind, params.tid].join(''),
  fav_user_list = $('#fav-userlist');

  if (fav_user_list.length === 0) {
    fav_user_list = $([
    '<div id="fav-userlist" class="fav-userlist">',
    '<div class="hd"><a href="" class="btn-close">X</a></div>',
    '<div class="bd">',
    '</div><i class="arrow"></i>',
    '</div>'
    ].join('')).appendTo('body');
    fav_user_list.find('.btn-close').click(function(e){
      e.preventDefault();
      fav_user_list.hide();
    });
  }

  fav_user_list.removeClass('arrow-bottom').
      find('.bd').
      css('height', 'auto').
      html('加载中...');

  fav_user_list.css({
    top: pos.top + 22,
    'margin-left': (function(con){
      return -1 * Math.floor(con.width()/2 - pos.left + con.offset().left) -10;
    })($('#content'))
  }).show();

  $.get(api_userlist,
  {
      tkind: params.tkind,
      tid: params.tid,
      alt: 'xd'
  },
  function(e){
    renderUserList(fav_user_list, e);
  }, 'jsonp');
});

            });
        
    Do = (typeof Do === 'undefined')? $ : Do;
    var div = ".operation_div";
    function addReportLink(){
      $.each($("#comments .comment-item ".concat(div)), function(i, el){
          if ($(el).find(".comment-report").length==0){
            $(el).append('<div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div>');
          }
      });
    };
    Do(function(){
        $("#comments").delegate(".comment-item", 'mouseenter mouseleave', function (e) {
          switch (e.type) {
            case "mouseenter":
              $(this).find(".comment-report").css('visibility', 'visible');
              break;
            case "mouseleave":
              $(this).find(".comment-report").css('visibility', 'hidden');
              break;
          }
        });
        $("#comments").delegate(".comment-report a", 'click', function (e) {
        e.preventDefault();
        var auditUrl = "http://www.douban.com/misc/audit_report?url=",
            opt = "comment_id";
        var obj = $(e.target).closest('.comment-item');
        var cid = obj.data("cid");
        var url = "http://www.douban.com/group/topic/38131596/?".concat(opt, '=', cid);
        generate_report_dialog({report_url: url});
        });
    addReportLink();
    });
