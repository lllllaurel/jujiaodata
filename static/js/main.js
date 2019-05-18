$(document).ready(function(){
    id_desc = 0
    tablename = "YsArticle"
    //获取阅读量列表
    $(".tablelist").children().click(function(){
        $(".tablelist").children().removeClass("active");
        $(this).addClass("active");
        tablename = $(this).text();
        $.get('/query/',{tablename:tablename, offset:id_desc},function(data){
            $(".query-body").html(data['content']);
        });
    });
    $(".query-body").dblclick(function(){
        id_desc+=1;
        $.get('/query/',{tablename:tablename, offset:id_desc},function(data){
            $(".query-body").html(data['content']);
        });
    });
    $("#runserver").click(function(){
        var filename = $("#filename").val();
        $.get('/handle/',{filename:filename,function:0},function(data){
            $(".pt-layout").html(data);
        });
    });
    $("#catfile").click(function(){
        var filename = $("#filename").val();
        $.get('/handle/',{filename:filename,function:1},function(data){
            content = data;
            $("#textarea-holder").css('display', 'block');
            $("#exampleFormControlTextarea1").text(content);
        });
    });
    $("#submitfile").click(function(){
        var filename = $("#filename").val();
        var editedFile = $("#exampleFormControlTextarea1").val();
        $.get('/handle/',{filename:filename,function:2,filecontent:editedFile},function(data){
            $("#textarea-holder").css('display', 'none');
            $(".pt-layout").html(data);
        });
    });
})
