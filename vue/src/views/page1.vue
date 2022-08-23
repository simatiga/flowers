<template>
    <div id="page1">
        <div id="page1-head">
            page1 ------- Data Profiling Report
        </div>
        <br>
        <div>
            <table>
                <thead>
                    <tr>
                        <th class="pin">Table Name</th>
                        <th>Column Name</th>
                        <th>Null Rate</th>
                        <th>Empty Rate</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(a,i) in da결과" :key="i">
                        <td>{{da결과[i].tab_nm}}</td>
                        <td>{{da결과[i].col_nm}}</td>
                        <td>{{da결과[i].rate_null}}%</td>
                        <td>{{da결과[i].rate_empty}}%</td>
                    </tr>
                </tbody>
            </table>
        </div>

        
        <!-- <div v-for="(a,i) in da결과" :key="i">
            <h4 :style="스타일" @click="modalWinOpen=true">{{da결과[i].tab_nm}}</h4>
            <p>{{da결과[i].col_nm}}</p> / null비율 : {{da결과[i].rate_null}}%, empty비율 : {{da결과[i].rate_empty}}%
        </div> -->
        
    </div>
</template>

<script>
    import $ from 'jquery';
    import da_prof_col from './../data/da_prof_col.json'
    import css from './style.css'
    // $('table').DataTable();

    // app.use(BootstrapVue3)

    export default {
        name: 'page1',
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
        }, 
        data() {
            return {
                da결과 : da_prof_col,
            }
        },
        // methods: {
        // },
        components: {
        },
        directives: { 
        },
    }
   
</script>

<style scoped>
    #page1{ width:inherit; height:3000px; position:relative; }
    #page1-head{ width:inherit; border-bottom:1px #D8D8D8 solid; height:70px; position:fixed; z-index:10; top:0;
        left:50%; transform: translateX(-50%); background-color:white; color:black; text-align:center; line-height:70px; font-size:30px; font-weight:bold; }
</style>