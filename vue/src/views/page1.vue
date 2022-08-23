<template>
    <div id="page1">
        <div id="page1-head">
            Data Profiling Report
            <b-button>Button</b-button>
        </div>
        <br>
        <div>
            <b-table-simple hover small caption-top responsive>
                <b-thead head-variant="dark">
                    <b-tr>
                        <b-th colspan="2">Table Name</b-th>
                        <b-th colspan="2">Column Name</b-th>
                        <b-th colspan="2">Null Rate</b-th>
                        <b-th colspan="2">Empty Rate</b-th>
                    </b-tr>
                </b-thead>
                <b-tbody>
                    <b-tr v-for="(a,i) in da결과" :key="i">
                        <b-th colspan="2">{{da결과[i].tab_nm}}</b-th>
                        <b-th colspan="2">{{da결과[i].col_nm}}</b-th>
                        <b-th colspan="2">{{da결과[i].rate_null}}%</b-th>
                        <b-th colspan="2">{{da결과[i].rate_empty}}%</b-th>
                    </b-tr>
                </b-tbody>
            </b-table-simple>
        </div>
        <!-- <div v-for="(a,i) in da결과" :key="i">
            <h4 :style="스타일" @click="modalWinOpen=true">{{da결과[i].tab_nm}}</h4>
            <p>{{da결과[i].col_nm}}</p> / null비율 : {{da결과[i].rate_null}}%, empty비율 : {{da결과[i].rate_empty}}%
        </div> -->
        
    </div>
</template>

<script>
    import da_prof_col from './../data/da_prof_col.json'

    export default {
        name: 'page1',
        data() {
            return {
                da결과 : da_prof_col,
            }
        },
    }
    // methods: {
    // },
    
    // components: {
    // }

    
</script>

<style scoped>
    #page1{ width:inherit; height:3000px; position:relative; }
    #page1-head{ width:inherit; border-bottom:1px #D8D8D8 solid; height:70px; position:fixed; z-index:10; top:0;
        left:50%; transform: translateX(-50%); background-color:white; color:black; text-align:center; line-height:70px; font-size:30px; font-weight:bold; }
</style>