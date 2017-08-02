x1=0;
function timeshow1()
{var time=new Date();var showtime =checkTime(time.getHours()) + "&nbsp;:&nbsp;" + checkTime(time.getMinutes()) + "&nbsp;:&nbsp;" + checkTime(time.getSeconds());
document.getElementById("time").innerHTML = showtime;setTimeout("timeshow1()",1000);
}
function timeshow()
{var dayNames = new Array("星期日","星期一","星期二","星期三","星期四","星期五","星期六");
var time = new Date();var showdate=(time.getMonth() + 1) + "月" + time.getDate() + "日";document.getElementById("date").innerHTML = showdate +""+ dayNames[time.getDay()];timeshow1() }
function checkTime(i)
{if (i<10) {i="0" + i} return i
}

function mobilclick()
{if($(".fr").css('display')=="none"){$(".fr").css('display','block')} else {$(".fr").css('display','none')}}
function newsch(x)
{$.ajax({
        type: 'get',
        url:'newsch/?action='+x,
        dataType: 'text',
        success: function (data) {
            if (data != "") {
                $('.' + 'News-list').html(data);
            }
        },
        error: function (err) {
            //请求数据失败    
            alert("请求数据失败");
        }
    });
}
function changeblx(x)
{if(x==12)
{$.ajax({
        type: 'get',
        url:'video_list/?action='+x1+'&action1='+1,
        dataType: 'text',
        success: function (data) {
            if (data != "") {
                $('#' + 'rep61379').html(data);
            }
        },
        error: function (err) {
            //请求数据失败    
            alert("请求数据失败");
        }
    })}
else
{x1=x;  
$.ajax({
        type: 'get',
        url:'video_list/?action='+x+'&action1='+0,
        dataType: 'text',
        success: function (data) {
            if (data != "") {
                $('#' + 'rep61379').html(data);
            }
        },
        error: function (err) {
            //请求数据失败    
            alert("请求数据失败");
        }
    })}
}

function changeblx1(x)
{if(x==12)
{$.ajax({
        type: 'get',
        url:'?action='+x1+'&action1='+1,
        dataType: 'text',
        success: function (data) {
            if (data != "") {
                $('#' + 'rep61379').html(data);
            }
        },
        error: function (err) {
            //请求数据失败    
            alert("请求数据失败");
        }
    })}
	else{  x1=x;  
$.ajax({
        type: 'get',
        url:'?action='+x+'&action1='+0,
        dataType: 'text',
        success: function (data) {
            if (data != "") {
                $('#' + 'rep61379').html(data);
            }
        },
        error: function (err) {
            //请求数据失败    
            alert("请求数据失败");
        }
    });}
}

function showch(x)
{$.ajax({
        type: 'get',
        url:'showch/?showch='+x,
        dataType: 'text',
        success: function (data) {
            if (data != "") {
                $('.' + 'Calendar-box').html(data);
            }
        },
        error: function (err) {
            //请求数据失败    
            alert("请求数据失败");
        }
    })}

function livech(x)
{/*$.ajax({
        type: 'get',
        url:'/?showch='+x,
        dataType: 'text',
        success: function (data) {
            if (data != "") {
                $('.' + 'Calendar-box').html(data);
            }
        },
        error: function (err) {
            //请求数据失败    
            alert("请求数据失败");
        }
    })*/
}

function showdata_det(x)
{
$.ajax({
        type: 'get',
        url:'?datateam='+x,
        dataType: 'text',
		contentType: "application/x-www-form-urlencoded; charset=utf-8",
        success: function (data) {
            if (data != "") {
                $('.' + 'data-exp1').html(data);$('.data-exp1').show();$('.hideserch').hide();
            }
        },
        error: function (err) {    
            alert("请求数据失败");
        }
    })
}
function gamemanshow(x)
{$('#'+x).show();}
function gamemanhide(x)
{$('#'+x).hide();}

function gamemanshowl(x)
{$('.'+x).show();}
function gamemanhidel(x)
{$('.'+x).hide();}

function seach()
{
$.ajax({
        type: 'get',
        url:'?search='+encodeURI($('#search').val()),
        dataType: 'text',
        success: function (data) {
            if (data != "") {
                $('.' + 'hideserch').html(data);$('.' + 'hideserch').show();
				$('.data-exp1').hide()
            }
        },
        error: function (err) {    
			$('.' + 'hideserch').html('没找到符合要求的项');$('.data-exp1').hide()
        }
    })
	}

function checknull(){
 if(document.loginform_Li.ss_username.value==""){
  alert("用户名不能为空!");
  return false;
 }
 if(document.loginform_Li.passwordi.value==""){
  alert("密码不能为空!");
  return false;
 }
 if(document.loginform_Li.passwordk.value==""){
  alert("请确认密码!");
  return false;
 }
 if(document.loginform_Li.passwordi.value!=document.loginform_Li.passwordk.value){
  alert("2次密码不一致!");
  return false;
 }
 if(document.loginform_Li.email.value==""){
  alert("请输入您的电子邮件!");
  return false;
 }
 return true;
}

function checksharing(x)
{
/*if(x==null||x=="")
{alert('请先登陆!');return false;
}
else{*/
 if(document.bbs_sharing.bbs_sharing1.value==""){
  alert("标题不能为空!");
  return false;
 }
 if(document.bbs_sharing.bbs_sharing2.value==""){
  alert("地址不能为空!");
  return false;
 }
 if((document.bbs_sharing.bbs_sharing2.value).length<11){
  alert("请输入正确的地址!");
  return false;
 }
 if((document.bbs_sharing.bbs_sharing2.value).substr(0,7)!="http://")
 {alert("请输入正确的地址!");
  return false;  
  }
  return true;

}

function checktalk(x)
{
/*if(x==null||x=="")
{alert('请先登陆!');return false;
}
else{*/
 if(document.bbs_ttalk.bbs_ttalk1.value==""){
  alert("话题不能为空!");
  return false;
 }
 if(document.bbs_ttalk.bbs_ttalk2.value==""){
  alert("内容不能为空!");
  return false;
 }
 if((document.bbs_ttalk.bbs_ttalk2.value).length<5){
  alert("内容太少了!!!");
  return false;
 }
  return true;

}

function showdata_detb(x)
{
$.ajax({
        type: 'get',
        url:'?datateam='+x,
        dataType: 'text',
		contentType: "application/x-www-form-urlencoded; charset=utf-8",
        success: function (data) {
            if (data != "") {
                $('.' + 'data-exp1').html(data);$('.data-exp1').show();$('.hideserch').hide();
            }
        },
        error: function (err) {    
            alert("请求数据失败");
        }
    })
}
function bbslist(x)
{if(x=='share')
{$('.bbsshare1').css('color','#F03');
 $('.bbstalk1').css('color','#07d');
 bbstalkchs(x)
}
 else if(x=='talk')
{$('.bbstalk1').css('color','#F03');
 $('.bbsshare1').css('color','#07d');
 bbstalkchs(x)}
}


function add_like(x,n,y)
{if (x=="AnonymousUser"){
 }
 else if(x){

	 }
	}

function bbstalkchs(x)
{
	$.ajax({
        type: 'get',
        url:'',
        dataType: 'text',
		data:{"x":x},
		contentType: "application/x-www-form-urlencoded;charset=utf-8",
        success: function (data) {
            if (data != "") {
                $('.' + 'minbbs2').html(data);
            }
        },
        error: function (err) {    
            alert("请求数据失败");
        }
    })
}

function add_to_favor(type){
	if(type==1){
		var href = 'http://www.scriptsports.com/', title = '欢迎来到脚本体育ScriptSports';	
		try{
			window.external.AddToFavoritesBar(href, title);
		}catch(e){
			try{
				window.external.addFavorite(href, title);
			}catch(e2){
				alert('浏览器不受支持，请按 Ctrl+D把 脚本体育scriptsports 放入收藏夹');
			}
		}
	}
}
function news1234(x)
{$.ajax({
        type: 'get',
        url:'',
        dataType: 'text',
		data:{"x":x},
		contentType: "application/x-www-form-urlencoded;charset=utf-8",
        success: function (data) {
            if (data != "") {
                $('.' + 'news_list').html(data);
            }
        },
        error: function (err) {    
            alert("请求数据失败");
        }
    })}