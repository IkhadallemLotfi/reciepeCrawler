<template>
    <div class="container">
        <div class="row col-md-12">
            <transition name="fadeDown">
                <div v-if="show" style="animation-duration: 1.5s" class="container-logo">
                    <img :src="logo">
                </div>
            </transition>
        </div>

        <div class="container-row-images row col-md-12">
            <div v-bind:style="{'padding-left' : padding1+'cm'}" ></div>
            <div v-bind:style="{'margin-left' : margin1+'cm'}" id="carousel"
            class="transition" @mouseover="endHover(1)" @mouseleave="resumeHover(1)"   >
                <a v-for="(destination,index) in recettes1" :href="destination.link" :key="index+'car1'"  
                target="_blank" class="col-md-1" :id="index" @click="this.endHover(1);this.endHover(2);this.endHover(3)" >
                    <img class="image-recette" :src="destination.src"> 
                </a>
                <a class="col-md-1" style="animation-duration: 2s" id="loading1">
                    <div class="image-waiting" :style="{'background-color': getBGColor()}">
                        <grid-loader :loading="true" color="white" 
                        style="margin-left:auto;margin-right:auto;padding-top:1.2cm"></grid-loader>
                    </div>
                </a>
            </div>
        </div>

        <div class="container-row-images row col-md-12">
            <div v-bind:style="{'padding-left' : padding2+'cm'}" ></div>
            <div v-bind:style="{'margin-left' : margin2+'cm'}" id="carousel2" 
                class="transition"  >
                <a v-for="(destination,index) in recettes2" :href="destination.link" :key="index+'car2'" 
                @mouseover="endHover(2)" @mouseleave="resumeHover(2)"
                target="_blank" class="col-md-1" :id="index" >
                    <img class="image-recette" :src="destination.src">
                </a>
                <transition name="fade">
                    <a class="col-md-1" v-if="loading2" style="animation-duration: 2s">
                        <div class="image-waiting" :style="{'background-color': getBGColor()}">
                            <grid-loader :loading2="true" color="white" 
                            style="margin-left:auto;margin-right:auto;padding-top:1.2cm"></grid-loader>
                        </div>
                    </a>
                </transition>
            </div>
        </div>

        <div class="container-row-images row col-md-12">
            <div v-bind:style="{'padding-left' : padding3+'cm'}" ></div>
            <div v-bind:style="{'margin-left' : margin3+'cm'}" id="carousel3" 
            class="transition"  >
                <a v-for="(destination,index) in recettes3" :href="destination.link" :key="index+'car3'" 
                @mouseover="endHover(3)" @mouseleave="resumeHover(3)" 
                target="_blank" class="col-md-1" :id="index" >
                    <img class="image-recette" :src="destination.src">
                </a>
                <transition name="fade">
                    <a class="col-md-1" v-if="loading3" style="animation-duration: 2s">
                        <div class="image-waiting" :style="{'background-color': getBGColor()}">
                            <grid-loader :loading3="true" color="white" 
                            style="margin-left:auto;margin-right:auto;padding-top:1.2cm"></grid-loader>
                        </div>
                    </a>
                </transition>
                
            </div>
        </div>
        <br>
    </div>
</template>

<script>
export default {
    data(){
        return{ 
            logo: require('../../../public/img/logo.png'),
            show : Boolean(false),
            key1 : Number(0),
            recettes1:[],
            recettes2:[],
            recettes3:[],

            ready1 : Boolean(false),
            ready2 : Boolean(false),
            ready3 : Boolean(false),

            margin1 : Number(0),
            savedMargin1 : Number(0),
            margin2 : Number(0),
            margin3 : Number(0),

            padding1 : Number(0),
            padding2 : Number(0),
            padding3 : Number(0),

            running1 : Boolean(true),
            running2 : Boolean(true),
            running3 : Boolean(true),

            loading1 : Boolean(false),
            loading2 : Boolean(false),
            loading3 : Boolean(false),
        }
    },
    methods:{
        getBGColor(){
            var number = Math.round(Math.random() * 10)
            switch (number) {
                case 0:
                    return "#1a1a23";
                    break;
                case 1:
                    return "#98bec8"
                    break
                case 2:
                    return "#e8c3b9"
                    break
                case 3:
                    return "#7290a4"
                    break
                case 4:
                    return "#2b2f3c"
                    break
                case 5:
                    return "#45383c"
                    break
                default :
                    return "#314964";                
                    break;
            }
        },
        endHover(row){
            switch (row) {
                case 1:
                    if(this.ready1){
                        var boxOne = document.getElementById('carousel')
                        this.running1 = false;
                    }
                    break;
                
                case 2:
                    if(this.ready2){
                        var boxOne = document.getElementById('carousel2')
                        this.running2 = false;
                    }
                    break;

                case 3:
                    if(this.ready3){
                        var boxOne = document.getElementById('carousel3')
                        this.running3 = false;
                    }
                    break;
            }
            if(boxOne != null){
                switch (row) {
                    case 1:
                        this.savedMargin1 = this.margin1
                        break;
                    case 2:
                        
                        break;
                    case 3:
                        
                        break;
                }
                var computedStyle = window.getComputedStyle(boxOne),
                marginLeft = computedStyle.getPropertyValue('margin-left');
                boxOne.style.marginLeft = marginLeft;
                
                boxOne.classList.remove('transition');
            }
            
        },
        launch(row){
            this.margin1 -= 6.2
            console.log('lol')
            setInterval(() => {
                if(this.running1 ){
                    var totalWidth =  $(window).width()
                    var nbImage = Math.round(totalWidth / 230) ;
                    if(this.recettes1.length < nbImage +5 ){
                        this.crawlRecettes(1)
                    }
                }
            },1000)
            setInterval(() =>{
                if(this.running1 && this.ready1){
                    console.log('test');
                    this.margin1 -= 6.2
                }
            },10000)
            setInterval(() => {
                var nodes = document.getElementById('carousel').childNodes
                if( nodes != null && nodes.length > 2 && nodes[1].getBoundingClientRect().x < 0){
                    this.recettes1.splice(0,1)
                    this.padding1 += 6.3 ;
                    if(this.running1 ){
                        var totalWidth =  $(window).width()
                        var nbImage = Math.round(totalWidth / 230) ;
                        if(this.recettes1.length < nbImage +5 ){
                            this.crawlRecettes(1)
                        }
                    }
                }
                var totalWidth =  $(window).width()
                if ( this.ready1 && document.getElementById('loading1').getBoundingClientRect().right < totalWidth ){
                    this.ready1 = false;
                    var boxOne = document.getElementById('carousel')
                    var computedStyle = window.getComputedStyle(boxOne),
                    marginLeft = computedStyle.getPropertyValue('margin-left');
                    boxOne.classList.remove('transition');
                    boxOne.style.marginLeft = marginLeft;
                }
            },250)
        },
        resumeHover(row){
            switch (row) {
                case 1:
                    var previouStateRun = this.running1
                    this.running1 = true
                    var boxOne = document.getElementById('carousel')
                    boxOne.classList.add('transition')
                    if(this.ready1 && previouStateRun == false){
                        this.margin1 = this.savedMargin1 - 0.001;
                        this.margin1 = this.savedMargin1 + 0.001;
                    }
                    break;
                
                case 2:
                    var boxOne = document.getElementById('carousel2')
                    this.running2 = true;
                    break;

                case 3:
                    var boxOne = document.getElementById('carousel3')
                    this.running3 = true;
                    break;
            }
        },
        crawlRecettes(row){
            if(this.loading1 == false){
                this.loading1 = true;
                axios.get('/crawlRecettes')
                .then((response)=>{
                    var totalWidth =  $(window).width()
                    var nbImage = Math.round(totalWidth / 230) ;
                    this.loading1 = false;
                    switch (row) { 
                        case 1:
                            if(this.running1 ){
                                this.recettes1.push(response.data);
                                this.key1 ++;
                                if(this.recettes1.length >= nbImage){
                                    if(this.ready1 == false){
                                        this.ready1= true;
                                        this.launch(1)
                                    }
                                }
                            }
                            break;
                        case 2:
                            if(this.running2 ){
                                this.recettes2.push(response.data);
                                if(this.recettes2.length >= nbImage){
                                    this.ready2= true;
                                    
                                }
                            }
                            break;
                        case 3:
                            if(this.running3 ){
                                this.recettes3.push(response.data);
                                if(this.recettes3.length >= nbImage){
                                    this.ready3= true;
                                }
                            }
                            break;
                    }
                },(error)=>{
                    console.log(error);
                });
            }
        },
        getMore(nb){
            for (let index = 0; index < nb; index++) {
                this.crawlRecettes(1);
            }
        }
    },

    
    beforeMount(){
        // taille de l'image 226.76678
        var totalWidth =  $(window).width()
        var nbImage = Math.round(totalWidth / 230) ;
        
        setTimeout( ()=>{
            this.show = true;
            setTimeout( () =>{
                this.getMore(nbImage +1);
            },1000)
        },500)
        
        $(window).focus( $.proxy(function(){
            this.resumeHover(1)
            this.resumeHover(2)
            this.resumeHover(3)
        },this));

        $(window).blur( $.proxy(function(){
            this.endHover(1)
            this.endHover(2)
            this.endHover(3)
        },this));

    },

}
</script>

<style>
    .image-waiting{
        width: 6cm;
        height: 4.3cm;
        border-radius: 6px;
        transition: transform 0.3s ease;
        transform: scale(1);
        object-fit: cover;
        display: block;
    }
    
    .container{
        width: 100%;
    }

    .container-row-images{ 
        width: 100%;
        margin: .2cm auto;
        height: auto;
        overflow-x: hidden;
        overflow-y: hidden;
        display: flex;
        flex-direction: row;
    }
    .container-row-images div:nth-child(2) {
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
    }

    .transition { /***10s au départ puis 30s  */
        -webkit-transition: all 10s linear;
        -moz-transition: all 10s linear;
        -ms-transition: all 10s linear;
        -o-transition: all 10s linear;
        transition: all 10s linear;
    }
    .container-row-images a {
        margin-right: .3cm;
        border-radius: 6px;
    }
    .container-row-images img{
        width: 6cm;
        height: 4.3cm;
        border-radius: 6px;
        transition: transform 0.3s ease;
        transform: scale(1);
        object-fit: cover;
        display: block;
    }
    .container-row-images img:hover{
        transform: scale(1.05);
        border-radius: 6px;
    }

    .container-logo{
        width: 5cm;
        margin-left: auto;
        margin-right: auto;
    }
    .container-logo img{
        width: 100%;
        height: auto;
        
    }

</style>
