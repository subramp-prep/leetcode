!function(e){"function"==typeof define&&define.amd?define(["jquery"],e):"object"==typeof exports?e(require("jquery")):e(jQuery)}(function(v){var i=/\+/g;function x(e){return l.raw?e:encodeURIComponent(e)}function k(e,o){var n=l.raw?e:function(e){0===e.indexOf('"')&&(e=e.slice(1,-1).replace(/\\"/g,'"').replace(/\\\\/g,"\\"));try{return e=decodeURIComponent(e.replace(i," ")),l.json?JSON.parse(e):e}catch(e){}}(e);return v.isFunction(o)?o(n):n}var l=v.cookie=function(e,o,n){if(void 0!==o&&!v.isFunction(o)){if("number"==typeof(n=v.extend({},l.defaults,n)).expires){var i=n.expires,r=n.expires=new Date;r.setTime(+r+864e5*i)}return document.cookie=[x(e),"=",(t=o,x(l.json?JSON.stringify(t):String(t))),n.expires?"; expires="+n.expires.toUTCString():"",n.path?"; path="+n.path:"",n.domain?"; domain="+n.domain:"",n.secure?"; secure":""].join("")}for(var t,c,u=e?void 0:{},a=document.cookie?document.cookie.split("; "):[],d=0,f=a.length;d<f;d++){var p=a[d].split("="),s=(c=p.shift(),l.raw?c:decodeURIComponent(c)),m=p.join("=");if(e&&e===s){u=k(m,o);break}e||void 0===(m=k(m))||(u[s]=m)}return u};l.defaults={},v.removeCookie=function(e,o){return void 0!==v.cookie(e)&&(v.cookie(e,"",v.extend({},o,{expires:-1})),!v.cookie(e))}});

!function(o,t){var n=function(){o("#cong button").click(function(){o.cookie("cong","dismissed")})};o(document).ready(function(){t.isAuthenticated&&t.congratulation&&"dismissed"!==o.cookie("cong")&&o("#cong").removeClass("hide"),n(),o(window).scroll(function(){100<o(this).scrollTop()?o("#go-top").fadeIn("fast"):o("#go-top").fadeOut("fast")}),o("#go-top").click(function(){o("html, body").stop().animate({scrollTop:0},500,function(){o("#go-top").fadeOut("fast")})})})}(jQuery,pageData);
