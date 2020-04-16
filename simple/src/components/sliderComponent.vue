<template>
    <div class='slider-warapper' @mouseover="clearInv" @mouseout="runInv">
        <div v-show="index === nowIndex" v-for="(imgUrl,index) in sliderImgList" :key="index" class="slider-item item1" v-bind:class="['item'+index]">
            <a href="">
                <img v-bind:src=imgUrl alt="">
            </a>
        </div>
        <!-- dots -->
        <ul class="slider-dots">
            <li>&lt;</li>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>&gt;</li>
        </ul>
    </div>
</template>
    

<script>
export default {
    data() {
        return {
            nowIndex:0,
            sliderImgList : [require('../assets/111.jpg'),require('../assets/222.jpg'),require('../assets/333.jpg'),require('../assets/444.jpg'),]
        }
    },
    methods: {
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
    right: 50px;
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
</style>
