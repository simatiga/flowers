<template>
    <div id="page2">
        <div id="page2-head">
            PAGE 2 top 
        </div>
        <br>
        <br>
        page2 middle
    </div>
</template>

<script>
    import $ from 'jquery';
    export default {
        name: "page2",
        mounted(){
            /* Nav 처리 */
            $(".nav-box-circle").removeClass("nav-box-selected");
            for(var x=0;x<$(".nav-box-circle").length;x++){
                if(!$(".nav-box-circle").eq(x).hasClass("nav-box-default")){
                    $(".nav-box-circle").eq(x).addClass("nav-box-default")
                }
            }
            $(".nav-box-circle").eq(0).removeClass("nav-box-default");
            $(".nav-box-circle").eq(0).addClass("nav-box-selected");
        }
    }
</script>

<style scoped>
    #page2{ width:inherit; height:3000px; position:relative; }
    #page2-head{ width:inherit; border-bottom:1px #D8D8D8 solid; height:70px; position:fixed; z-index:10; top:0;
        left:50%; transform: translateX(-50%); background-color:white; color:black; text-align:center; line-height:70px; font-size:30px; font-weight:bold; }
</style>