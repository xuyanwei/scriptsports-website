function shrink1()
{if($("#h3-1").children("a").html()=='∧'){$("#h3-1").children("a").html("∨");$("#l-vidoe-1").hide()} else {$("#h3-1").children("a").html("∧");$("#l-vidoe-1").show()}}
function shrink2()
{if($("#h3-2").children("a").html()=='∧'){$("#h3-2").children("a").html("∨");$("#1-vidoe-2").hide()} else {$("#h3-2").children("a").html("∧");$("#1-vidoe-2").show()}}		
function exp()
{if($("#safeexp").css('display')=="none"){$("#safeexp").css('display','block')} else {$("#safeexp").css('display','none')}}
function exp2()
{ if($(".r-vidoe").css("display")=="none"){$(".r-vidoe").show()}}
function light()
{if($("#lgi").html()=='关灯'){$("#lgi").html("开灯");$(".kaiguan").css('background-color','#000')} else {$("#lgi").html("关灯");$(".kaiguan").css('background-color','#fff')}}
