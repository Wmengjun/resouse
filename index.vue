<template>
<div style="text-align: left;height:100%">
  <div class="divtwo">
    <span style="display:block;margin-bottom: inherit;">关键字:</span>
    <div v-for="(row,index) in num" style="display: inline;" @mouseover="subover()" @mouseout="subout()">
      <textarea v-model="data[index]" style="height:5%;" />
      <div v-show="!subhover" style="display: inline;" @click="subkey(index)" class="subimg">
        <button style="height:30px;width:30px;background-color: transparent;border: none;" />
      </div>
      <div v-show="subhover" style="display: inline;" @click="subkey(index)" class="subimg">
        <img src="@/assets/sub.png" style="height:30px;width:30px">
      </div>
    </div>
    <div style="display: inline;" @click="addkey()">
      <img src="@/assets/add.png" style="height:30px;width:30px">
    </div>
    <div style="display: inline;" @click="change()">
      <img src="@/assets/right.png" style="height:30px;width:30px">
    </div>
    <br><span style="display:block">正则表达：</span>
    <textarea class="textareastyle" v-model="regx"></textarea>
    <br><span style="display:block">命令显示：</span>
    <textarea class="textareastyle" v-model="mmlvalue"></textarea>
    <hr style="height:1px;border:none;border-top:1px dashed #0066CC;" />
    <br><span>                                                                                   </span>
    <select v-model='selected'>
          <option v-for="option in options" v-bind:value="option.value">
            {{ option.text }}
          </option>
        </select>
    <span>{{ selected }}</span>
    <div v-show="selected==='ADD SIPFLTSET'">
      <span>SIP适配集名称：</span>
      <input type="text" v-model="sfn">
      <span>远端ip地址</span>
      <input type="text" v-model="rip">
      <button type="button" name="button" @click="newsipfl()">生成</button>
    </div>
    <div v-show="selected==='ADD SIPRGEXFLT'">
      <span>正则表达式适配名称：</span>
      <input type="text" name="" value="">
      <span>SIP适配集名称：</span>
      <input type="text" name="" value="">
    <br><span>消息类型：</span>
      <select class="" name="">
        <option value="">请选择</option>
      </select>
      <span>消息方法：</span>
      <input type="text" name="" value="">
      <br><span>正则表达式：</span>
        <select class="" name="">
          <option value="">请选择</option>
        </select>
        <span>适配类型：</span>
        <input type="text" name="" value="">
        <br><span>适配组号：</span>
          <select class="" name="">
            <option value="">请选择</option>
          </select>
          <span>适配参数值：</span>
          <input type="text" name="" value="">
      <button type="button" name="button">生成</button>
    </div>
    <!-- <div style="border: 1px solid #d8caca;height: 100px;width:80%;margin-left:5%">
命令生成操作区域。。。待定
</div> -->
  </div>
</div>
</template>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      selected: 'ADD SIPFLTSET',
      options: [
        { text: 'ADD SIPFLTSET', value: 'ADD SIPFLTSET' },
        { text: 'ADD SIPRGEXFLT', value: 'ADD SIPRGEXFLT' },
        { text: 'MOD SIPTG', value: 'MOD SIPTG' }
      ],
      sfn: '',
      rip: '',
      row: 0,
      index: 0,
      num: 1,
      data: [],
      regx: '',
      mmlvalue: '',
      creat: '命令生成操作区域。。。待定',
      subhover: false,
      ipAdress: [{
        value: ''
      }, {
        value: ''
      }, {
        value: ''
      }, {
        value: ''
      }]
    }
  },
  methods: {
    newsipfl () {
      this.mmlvalue = this.mmlvalue + this.selected + ':SFN=' +`${this.sfn},` +'RIP=' + `${this.rip};\n`
    },
    subover () {
      this.subhover = true
    },
    subout () {
      this.subhover = false
    },
    addkey () {
      if (this.num < 3) {
        this.num = this.num + 1
      } else {
        window.alert('行数已达上限')
      };
    },
    subkey (index) {
      if (this.num !== 1) {
        this.num = this.num - 1
      };
      for (var i = 0; i < this.data.length; i++) {
        var temp = this.data[i]
        if (!isNaN(index)) {
          temp = i
        }
        if (temp === index) {
          for (var j = i; j < this.data.length; j++) {
            this.data[j] = this.data[j + 1]
          }
          this.datalength = this.data.length - 1
        }
      }
    },
    change () {
      var newdata = {}
      var a = /.*\\d+.*/
      var keyword = 'key'
      for (var i = 0; i < this.data.length; i++) {
        newdata[keyword + i] = this.data[i].split('\n')
      }
      console.log(newdata)
      var sumtem = ''
      for (var item in newdata) {
        var tem = ''
        for (var k = 0; k < newdata[item].length; k++) {
          if (a.test(newdata[item][k])) {} else {
            tem = tem + newdata[item][k] + '.*\\s'
          }
        }
        sumtem = sumtem + tem + '\n'
      }
      this.regx = sumtem
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

.divtwo {
  background-color: beige;
  margin: 10px 0px 10px 20%;
  padding: 20px;
  width: 60%;
  height: 100%;
}

</style>
