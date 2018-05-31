<template>
  <div style="text-align: left;">
    <span>关键字:</span>
    <div v-for="(row,index) in num" style="display: inline;margin-left:5%;height:50px;">
      <textarea
      v-model="data[index]"
      name="name"
      style="height:100%;"
      />
      <div style="display: inline;" @click="subkey(index)">
        <img src="@/assets/sub.png" style="height:30px;width:30px">
      </div>
    </div>

    <div style="display: inline;" @click="addkey()">
      <img src="@/assets/add.png" style="height:30px;width:30px">
    </div>
    <div style="display: inline;" >
      <img src="@/assets/right.png" style="height:30px;width:30px">
    </div>
    <br><span >正则表达：</span>
      <textarea class="textareastyle" v-model="regx"></textarea>
    <br><span>命令显示：</span>
      <textarea class="textareastyle" v-model="mmlvalue" ></textarea>
      <hr style="height:1px;border:none;border-top:1px dashed #0066CC;" />
      <br><span >&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</span>
        <textarea class="textareastyle" v-model="creat"></textarea>
    <!-- <div style="border: 1px solid #d8caca;height: 100px;width:80%;margin-left:5%">
      命令生成操作区域。。。待定
    </div> -->

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      num:1,
      data: [],
      regx: '',
      mmlvalue: '',
      creat:'命令生成操作区域。。。待定'
    }
  },
  methods: {
    addkey () {
      this.num = this.num + 1
    },
    subkey(index) {
      this.num = this.num - 1
      for(var i =0;i <this.data.length;i++){
        var temp = this.data[i];
        if(!isNaN(index)){
          temp=i;
        }
        if(temp == index){
          for(var j = i;j <this.data.length;j++){
            this.data[j]=this.data[j+1];
          }
          this.datalength = this.data.length-1;
        }
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.textareastyle {
  display: inline;
  height: 100px;
  width: 80%;
  margin: 10px;
}
</style>
