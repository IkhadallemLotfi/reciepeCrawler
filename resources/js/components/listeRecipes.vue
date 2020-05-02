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
            class="transition"  >
                <a v-for="(destination,index) in recettes1" :href="destination.link" :key="index+'car1'"  
                @mouseover="endHover(1)" @mouseleave="resumeHover(1)"
                target="_blank" class="col-md-1" :id="index" >
                    <img class="image-recette" :src="destination.src"> 
                </a>
                <transition name="fade">
                    <a class="col-md-1" v-if="loading" style="animation-duration: 2s">
                        <div class="image-waiting" :style="{'background-color': getBGColor()}">
                            <grid-loader :loading="true" color="white" 
                            style="margin-left:auto;margin-right:auto;padding-top:1.2cm"></grid-loader>
                        </div>
                    </a>
                </transition>
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
            recettes1:[],
            recettes2:[],
            recettes3:[],

            ready1 : Boolean(false),
            ready2 : Boolean(false),
            ready3 : Boolean(false),

            margin1 : Number(0),
            margin2 : Number(0),
            margin3 : Number(0),

            padding1 : Number(0),
            padding2 : Number(0),
            padding3 : Number(0),

            running1 : Boolean(true),
            running2 : Boolean(true),
            running3 : Boolean(true),

            loading : Boolean(false),
            loading2 : Boolean(false),
            loading3 : Boolean(false),
        }
    },
    watch: {
        ready1 : function (old, val){
            if(this.ready1){
                setInterval(() => {
                    var totalWidth =  $(window).width()
                    var nbImage = Math.round(totalWidth / 230) ;
                    if(this.running1 && this.recettes1.length < nbImage+1 ){
                        this.crawlRecettes(1) 
                    }
                }, 500);
            }
        },

        ready2 : function (old, val){
            if(this.ready2){
                setInterval(() => {
                    var totalWidth =  $(window).width()
                    var nbImage = Math.round(totalWidth / 230) ;
                    if(this.running2 ){
                        this.crawlRecettes(2) 
                    }
                }, 500);
            }
        },

        ready3 : function (old, val){
            if(this.ready3){
                setInterval(() => {
                    var totalWidth =  $(window).width()
                    var nbImage = Math.round(totalWidth / 230) ;
                    if(this.running3 ){
                        this.crawlRecettes(3) 
                    }
                }, 500);
            }
        },

        recettes1 : function(val){
            if(this.recettes1.length > 2){
                var nodes = document.getElementById('carousel').childNodes
                if(nodes[1].getBoundingClientRect().x < 0 ){
                    nodes[0].parentNode.removeChild(nodes[0])
                    this.padding1 += 6.3 ;
                }
            }
        },

        recettes2 : function(val){
            if(this.recettes2.length > 2){
                var nodes = document.getElementById('carousel2').childNodes
                if(nodes[1].getBoundingClientRect().x < 0 ){
                    nodes[0].parentNode.removeChild(nodes[0])
                    this.padding2 += 6.3 ;
                }
            }
        },

        recettes3 : function(val){
            if(this.recettes3.length > 2){
                var nodes = document.getElementById('carousel3').childNodes
                if(nodes[1].getBoundingClientRect().x < 0 ){
                    nodes[0].parentNode.removeChild(nodes[0])
                    this.padding3 += 6.3 ;
                }
            }
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
                var computedStyle = window.getComputedStyle(boxOne),
                marginLeft = computedStyle.getPropertyValue('margin-left');
                boxOne.style.marginLeft = marginLeft;
                
                boxOne.classList.remove('transition');
            }
            
        },

        resumeHover(row){
            switch (row) {
                case 1:
                    this.running1 = true
                    var boxOne = document.getElementById('carousel')
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
            boxOne.classList.add('transition')
        },


        crawlRecettes(row){
            axios.get('/crawlRecettes')
            .then((response)=>{
                var totalWidth =  $(window).width()
                var nbImage = Math.round(totalWidth / 230) ;
                switch (row) {
                    case 1:
                        if(this.running1 ){
                            this.recettes1.push(response.data);
                            if(this.recettes1.length >= nbImage){
                                this.margin1 -= 6.2
                                this.ready1= true;
                            }
                        }
                        break;
                    case 2:
                        if(this.running2 ){
                            this.recettes2.push(response.data);
                            if(this.recettes2.length >= nbImage){
                                this.margin2 -= 6.2
                                this.ready2= true;
                            }
                        }
                        break;
                    case 3:
                        if(this.running3 ){
                            this.recettes3.push(response.data);
                            if(this.recettes3.length >= nbImage){
                                this.margin3 -= 6.2
                                this.ready3= true;
                            }
                        }
                        break;
                }
            },(error)=>{
                console.log(error);
            });
        },
        getMore(nb){
            for (let index = 0; index < nb; index++) {
                this.crawlRecettes(1);
                this.crawlRecettes(2);
                this.crawlRecettes(3);
            }
        }
    },

    
    beforeMount(){
        // taille de l'image 226.76678
        var totalWidth =  $(window).width()
        var nbImage = Math.round(totalWidth / 230) ;
        
        setTimeout( ()=>{
            this.show = true;
            this.getMore(nbImage +1);
            setTimeout( () =>{
                this.loading = true;
                this.loading2 = true;
                this.loading3 = true;
            },1000)
        },500)
        
        
        setTimeout( ()=>{
            document.getElementById('carousel').style.transitionDuration = "30s";
            document.getElementById('carousel2').style.transitionDuration = "30s";
            document.getElementById('carousel3').style.transitionDuration = "30s";
        },25000)
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
        -webkit-transition: all 15s linear;
        -moz-transition: all 15s linear;
        -ms-transition: all 15s linear;
        -o-transition: all 15s linear;
        transition: all 15s linear;
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
