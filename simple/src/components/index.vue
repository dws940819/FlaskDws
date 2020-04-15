<template>
  <div class="index-wrapper">
    <div class="index-left">
      <div class="index-left-block all-products">
        <h2>全部产品</h2>
        <template v-for='product in productList'>
          <h3>{{ product.title }}</h3>
          <ul>
            <li v-for="item in product.list" :key="item">
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
        <template v-for='x in newXi'>
            <ul v-for='u in x.newX'>
                <li><a v-bind:href='x.url'>{{u.text}}</a></li>
            </ul>
        </template>
        
      </div>
    </div>
    <div class="index-rigt">
        <div style="font-size:80px;text-align:center;line-height:300px;width:1031.8px;height:300px;background:red;margin:0 auto;">
            slider
        </div>
        <div class='index-board-list'>
            <div class="index-board-item" v-for="lis in lists" :key="lis">
                <div class="index-board-item-inner">
                    <h2>{{lis.title}}</h2>
                    <p>{{lis.text}}</p>
                    <div class="index-board-button"><a v-bind:href='lis.url'></a>{{lis.texts}}</div>
                </div>
            </div>

        </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      productList: {
        pc: {
          title: "PC产品",
          list: [
            {
              title: "数据统计",
              url: "http://starcraft.com"
            },
            {
              title: "数据预测",
              url: "http://warcraft.com"
            },
            {
              title: "流量分析",
              url: "http://overwatch.com",
              hot: true
            },
            {
              title: "广告发布",
              url: "http://hearstone.com"
            }
          ]
        },
        app: {
          last:true,
          title: "手机应用类",
          list: [
            {
              title: "91助手",
              url: "http://weixin.com"
            },
            {
              title: "产品助手",
              url: "http://weixin.com",
              hot:true
            },
            {
              title: "智能地图",
              url: "http://maps.com"
            },
            {
              title: "语音助手",
              url: "http://phone.com",
              hot:true
            }
          ]
        }
      },
      newXi:{
        newA:{
        url:'http://baidu.com',
        newX:[
            {
            text:'央视直播为湖北带货 一晚卖出6100万元'
            },
            {
            text:'美国暂停资助世卫'
            },
            {
            text:'三个疫苗获批试验'
            },
            {
            text:'联想暂停招聘'
            },
            {
            text:'美国确诊超60万'
            },
            {
            text:'最年轻亿万富翁'
            },
            ]
        }
      },
      lists:[
            {
            title:'华硕电脑',
            text:'华硕，坚为磐石！',
            texts:'立即购买',
            url:'http://baidu.com'
            },
            {
            title:'方正电脑',
            text:'方正，方方正正！',
            texts:'立即购买',
            url:'http://tengxun.com'
            },
            {
            title:'惠普电脑',
            text:'惠普，普惠天下！',
            texts:'立即购买',
            url:'http://ali.com'
            },
            {
            title:'华为电脑',
            text:'华为，我是水军！',
            texts:'立即购买',
            url:'http://huawei.com'
            },
        ]
    };
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

