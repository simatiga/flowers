<template>
  <div id="app">
    <router-view/>
    <Nav />
    
    <div class="menu">
        <!-- <a>Home</a>
        <a>Products</a>
        <a>About</a>  -->
        <a v-for="a in 메뉴들" :key="a">{{a}}</a>
        <!-- <a v-for="(a, i) in 메뉴들" :key="a">{{i}}. {{a}}</a> -->
    </div>
    
    <Page1 />
  </div>
  <!-- <div>
      <img :src=원룸들[0].image class="room-img">
      <h4 :style="스타일" @click="modalWinOpen=true">{{원룸들[0].title}}</h4>
      <p>{{원룸들[0].price}}원</p>
  </div>
  <div>
      <img :src=원룸들[1].image class="room-img">
      <h4 :style="스타일" @click="modalWinOpen=true">{{원룸들[1].title}}</h4>
      <p>{{원룸들[1].price}}원</p>
  </div> -->


  <!-- <div v-for="(a,i) in 원룸들" :key="i">
      <img :src=원룸들[i].image class="room-img">
      <h4 :style="스타일" @click="modalWinOpen=true">{{원룸들[i].title}}</h4>
      <p>{{원룸들[i].price}}원</p>
  </div> -->
</template>

<script>
// eslint-disable-next-line
/* eslint-disable */

// import data from './data/oneroom.js';
import da_prof_col from './data/da_prof_col.json'
import Nav from './views/nav';
import Page1 from './views/page1.vue'
import Page2 from './views/page2.vue'

export default {
  name: 'App',
  data() {
    return {
      // data 보관함. (중요 변수들 여기 다 만들어놓으면 됨)
      // object 자료형으로.
      // {자료이름 : 자료내용}
        products : ['역삼동원룸', '천호동원룸', '마포구원룸'],
        prices : [13, 23, 29],
        메뉴들 : ['Home', 'Data Profiling Report', 'About'],
        신고수 : [0, 0, 0],
        modalWinOpen : false,
        // 원룸들 : data,
    }
  },

  methods: {
    increase(i){
      this.신고수[i]++;
    }
  },
  
  components: {
    Nav, 
    Page1, 
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.menu{
  background: yellowgreen;
  padding:15px;
  border-radius:5px;
}

.menu a {
  color: Block;
  padding: 10px;
  font-size: 20px;
}

.room-img {
  width: 60%;
  margin-top: 40px;
}

.black-bg {
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.5);
  position: fixed; padding: 20px;
}

.white-bg {
  width: 100%; 
  background: white;
  border-radius: 8px;
  padding: 20px;
}


  /* 반응형 최대크기 */
  #app { margin:0 auto; width:750px; min-height:100%; padding-top:71px; border-left:1px #D8D8D8 solid; border-right:1px #D8D8D8 solid; text-align:center; }

  /* 여백제거 + 드래그방지 */
  body{ padding:0; margin:0; -ms-user-select: none; -moz-user-select: none; -khtml-user-select: none; -webkit-user-select: none; user-select: none; }

  /* 반응형 시작 */
  @media(max-width:750px){
    #app{ width:100%; border-left:0; border-right:0; }
  }

</style>
