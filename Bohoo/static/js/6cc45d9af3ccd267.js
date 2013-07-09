
    Do(function() {
      // 不再提醒
      Douban.init_delete_reply_notify=function(b){var a=function(g){g.preventDefault();var c=$(g.target);var h=c[0].href.split("#")[1];$.get("/j/accounts/remove_notify?id="+h);var d=c.closest(".item-req");if($.contains($(".top-nav-reminder")[0],d[0])){d=d.parent();var f=d.siblings().length;d.fadeOut(function(){d.remove()});if(f===0){d.closest(".bd").find(".no-new-notis").show()}}else{d.fadeOut()}};if(b.type==="click"){a(b)}else{$(b).click(a)}};
      Douban.init_discard_notify=function(b){var a=function(i){i.preventDefault();var c="/j/notification/discard";var f=$(i.target);var d=f[0].name;$.post_withck(c,{id:d},function(e){},"json");var g=f.closest(".item-req");if($.contains($(".top-nav-reminder")[0],g[0])){g=g.parent();var h=g.siblings().length;g.fadeOut(function(){g.remove()});if(h===0){g.closest(".bd").find(".no-new-notis").show()}}else{g.fadeOut()}};if(b.type==="click"){a(b)}else{$(b).click(a)}};
      var notimenu = $('#top-nav-notimenu');
      notimenu.bind('moreitem:show', function() {
        $.ajax({
          url: 'http://www.douban.com/j/notification/nav_pop',
          data: { ck: get_cookie('ck'),
                  k: '50655334:7ed469c01cbbee42e990db8a0321d3aa55223915'
                },
          dataType: 'jsonp',
          success: function(e) {
            if (e.r) {
              return;
            }
            notimenu.html(e.s);
            if (e.n === 0) {
              $('#db-global-nav .top-nav-reminder .num').remove();
            } else {
              $('#db-global-nav .top-nav-reminder .num span').html(e.n);
            }
            if (window.load_event_monitor) {
              load_event_monitor($('#db-global-nav'));
            }
          }
        });
      });
    });
    
Do(function(){
  var popup;var nav=$("#db-global-nav");var more=nav.find(".bn-more");nav.delegate(".bn-more, .top-nav-reminder .lnk-remind","click",function(c){c.preventDefault();var a=$(this);var b=a.parent();if(popup){popup.parent().removeClass("more-active");if($.contains(b[0],popup[0])){popup=null;return false}}b.addClass("more-active");popup=b.find(".more-items");popup.trigger("moreitem:show");return false});$(document).click(function(a){if($(a.target).closest(".more-items").length){return}if(popup){popup.parent().removeClass("more-active");popup=null}});
});
