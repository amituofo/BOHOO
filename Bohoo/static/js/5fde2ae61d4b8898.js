
Do(function(){
  var popup;var nav=$("#db-global-nav");var more=nav.find(".bn-more");nav.delegate(".bn-more, .top-nav-reminder .lnk-remind","click",function(c){c.preventDefault();var a=$(this);var b=a.parent();if(popup){popup.parent().removeClass("more-active");if($.contains(b[0],popup[0])){popup=null;return false}}b.addClass("more-active");popup=b.find(".more-items");popup.trigger("moreitem:show");return false});$(document).click(function(a){if($(a.target).closest(".more-items").length){return}if(popup){popup.parent().removeClass("more-active");popup=null}});
});

var login_url = 'http://www.douban.com/accounts/guide_login';
var reg_url = 'http://www.douban.com/accounts/guide_reg';

;(function() {
  var mask;
  var popup;
  var current = '';
  var popup_mark = 'g_reg'

  var init_popup = function() {
    mask = $('<div class="popup-reg-mask"></div>').appendTo('body');
    mask.css('height', $(document).height());
    popup = $('#g-popup-reg');
    popup.find('.lnk-close').click(function(e) {
        e.preventDefault();
        popup.hide();
        mask.hide();
        if (window.POPUP_REG) {
          window.name = popup_mark;
        }
    });
    if ($.browser.msie && ($.browser.version|0) === 6) {
        var win = $(window).scroll((function() {
            var timer;
            var doc = document.body;
            return function() {
                if (timer) {
                    window.clearTimeout(timer);
                }
                timer = window.setTimeout(function() {
                    popup.css({
                      top: (doc.scrollTop + win.height()/2 - popup.height()/2) + 'px'
                    });
                }, 20);
            };
        })()).trigger('scroll');
    }
  };

  var show_popup = function() {
    if (popup) {
      popup.show();
      mask.show();
    } else {
      $('#g-popup-reg').show();
      init_popup();
    }
  };

  
  Douban.init_show_register = function (e) {
    var node = $(e);
    node.click(function(e) {
      e.preventDefault();
      show_popup();
      if (current !== 'register') {
        popup.find('iframe').attr('src', reg_url);
      }
      current = 'register';
    });
  };

  Douban.init_show_login = function (e) {
    var node = $(e);
    node.click(function(e) {
      e.preventDefault();
      show_popup();
      if (current !== 'login') {
        popup.find('iframe').attr('src', login_url);
      }
      current = 'login';
    });
  };


  // 有些页面会自动弹注册框
  if (window.POPUP_REG && !window.name) {
    $(function() {
      show_popup();
      popup.find('iframe').attr('src', reg_url);
      current = 'register';
    });
  }

})();
