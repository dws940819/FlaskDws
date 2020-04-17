<template>
    <div class='slider-warapper' @mouseover="clearInv" @mouseout="runInv">
        <!-- 轮播图区 -->
        <div v-show="index === nowIndex" v-for="(item,index) in sliderImgList" :key="index" class="slider-item item1" v-bind:class="['item'+[index+1]]">
            <a href="">
                <img v-bind:src=item.imgUrl alt="">
            </a>
        </div>
        <!-- 图片标题 -->
            <h2 class="slider-title"> {{ sliderImgList[nowIndex].title }} </h2>
        <!-- 上一张下一张 -->
        <a v-on:click="preHandler" class="btn pre-btn" href="javascript:void(0)">&lt;</a>
        <a v-on:click="nextHandler" class="btn next-btn" href="javascript:void(0)">&gt;</a>
        <!-- dots -->
        <ul class="slider-dots">
            <li v-on:click="clickDots(index)" v-for="(item,index) in sliderImgList" :key="index" >{{ index+1 }} </li>
        </ul>
    </div>
</template>
    

<script>
export default {
    data() {
        return {
            nowIndex:0,
            sliderImgList : [
                {
                    imgUrl:require('../assets/111.jpg'),
                    title:'第一张'
                },
                {
                    imgUrl:require('../assets/222.jpg'),
                    title:'第二张'
                },
                {
                    imgUrl:require('../assets/333.jpg'),
                    title:'第三张'
                },
                {
                    imgUrl:require('../assets/444.jpg'),
                    title:'第四张'
                },

                ]
        }
    },
    methods: {
        clickDots(index){
            this.nowIndex = index
        },
        preHandler(){
            this.nowIndex--;
            if(this.nowIndex < 0){
                this.nowIndex = 3
            }
        },
        nextHandler(){
            this.autoPlay()
        },
        autoPlay(){
            this.nowIndex++;
            if(this.nowIndex == 4){
                this.nowIndex = 0
            }
        },
        runInv(){
            this.invId = setInterval(
                this.autoPlay,1000)
        },
        clearInv(){
            clearInterval(this.invId)
        },

    },
    created() {
        this.runInv()
    },
}
</script>


<style scoped>
.slider-warpper{
    width: 900px;
    height: 500px;
    /* overflow: hidden; */
    position: absolute;
}
.slider-item{
    width: 900px;
    height: 500px;
}
.item1{
    z-index: 100;
}
.item2{
    z-index: 90;
}
.item3{
    z-index: 80;
}
.item4{
    z-index: 70;
}
.slider-dots{
    position: absolute;
    right: 220px;
    bottom: 20px;
    z-index: 200;
}
.slider-dots li{
    width: 20px;
    height: 20px;
    border-radius: 50%;
    text-align: center;
    line-height: 20px;
    background: #000;
    float: left;
    color: antiquewhite;
    opacity: 0.6;
    margin: 0 10px;
}
.btn{
    width: 42px;
    height: 50px;
    background: #000;
    color: #ffffff;
    position: absolute;
    z-index: 300;
    top:50%;
    margin-top: 12px;
    font-size: 40px;
    text-align: center;
    line-height: 50px;
    opacity: 0.6;
}
.pre-btn{
    left: 260px;
}
.next-btn{
    right: 220px;
}
.slider-title{
    position: absolute;
    z-index: 400;
    bottom: 10px;
    font-size: 18px;
    color: #ffffff;
    background: #000;
    opacity: 0.6;
    border-radius: 80%;
}
</style>
