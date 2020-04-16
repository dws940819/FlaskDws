<template>
  <div class="index-wrapper">
    <div class="index-left">
      <div class="index-left-block all-products">
        <h2>全部产品</h2>
        <template v-for='product in productList'>
          <h3>{{ product.title }}</h3>
          <ul>
            <li v-for="(item, ite) in product.list" :key="ite">
              <a v-bind:href='item.url'>{{ item.title }}</a>
              <span v-if="item.hot" class='hot-tag'>HOT</span>
            </li>
          </ul>
          <hr v-if='!product.last' />
        </template>

        <!-- <ul>
                    <li v-for='item in productList.pc.list'>
                        <a v-bind:href="item.url">{{ item.title}}</a>
                    </li>
        </ul>-->
      </div>
      <div class="index-left-block lastest-news">
        <h2>最新消息</h2>
          <ul>
            <!-- <li v-for='u in newXi'>
              <a v-bind:href="u.url">{{u.text}}</a>
              
              </li> -->
              <li v-for="(news, si) in newsList" :key="si">
            <a v-bind:href="news.url">{{ news.title }}</a>
          </li>
          </ul>
        
      </div>
    </div>
    <div class="index-rigt">
        <slider-component></slider-component>
        <div class='index-board-list'>
            <div class="index-board-item" v-for="(lis, li) in boardList" :key="li">
                <div class="index-board-item-inner">
                    <h2>{{lis.title}}</h2>
                    <p>{{lis.description}}</p>
                    <div class="index-board-button"><a v-bind:href='lis.url'></a>{{lis.saleout}}</div>
                </div>
            </div>

        </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import SliderComponent from './sliderComponent'

export default {
  components:{
    SliderComponent
    },
  mounted() {
    axios.get("api/getNewsList")
      .then((response) => {
        // handle success
        console.log(response);
        this.newsList = response.data.list
      })
      .catch((error) => {
        // handle error
        console.log(error);
      });
      axios.get('api/getProductList')
      .then((response) => {
        console.log(response);
        this.productList = response.data
      })
      .catch((error) => {
        console.log(error);
      });
      axios.get('api/getBoardList')
      .then((response) => {
        console.log(response);
        this.boardList = response.data
      })
      .catch((error) => {
        console.log(error);
      });
    
  },
  data() {
    return {
      newsList: [],
      productList:null,
      boardList:null
    }
  }
};
</script>

<style scoped>
.index-wrapper {
  width: 1200px;
  margin: 0 auto;
  display: flex;
}
.index-left {
  width: 300px;
}
.index-right {
  width: 900px;
}
.index-left-block {
  margin: 15px;
  background: #ffffff;
  box-shadow: 0 0 1px #ddd;
  border-radius: 0 0 10px 10px;
}
.index-left-block h2 {
  color: #ffffff;
  background: #4fc08d;
  padding: 10px 15px;
  margin-bottom: 15px;
}
.all-products h3 {
  padding: 0 15px 5px 15px;
  font-weight: bolder;
  color: #000;
}
.index-left-block ul {
  padding: 10px 15px;
}
.index-left-block li {
  padding: 5px;
}
.hot-tag{
    color: white;
    background: rgb(209, 93, 194);
    font-size: 8px;
}
.index-board-list{
    margin-top: 30px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
.index-board-item{
    width: 460px;
    background:#fff;
    box-shadow: 0 0 1px #ddd;
    margin-bottom: 20px;
    padding-top: 20px;
}
.index-board-item-inner{
    height: 125px;
    padding-left: 120px;
    background-image: url(../assets/logo.png);
    background-repeat: no-repeat;
    background-size: 18%;
    background-position: 18px;
}
.index-board-item-inner h2{
    font-size: 18px;
    font-weight: bolder;
    color: #000000;
    margin-bottom: 15px;
}
.index-board-item-inner p{
    margin-bottom: 15px;
}
.index-board-button{
    width: 60px;
    height: 30px;
    line-height: 30px;
    color: #fff;
    background: limegreen;
    border-radius: 5px;
    text-align: center;
    
}
</style>

