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
            <div v-bind:style="{'padding-left' : rows[0].padding+'cm'}" ></div>
            <div v-bind:style="{'margin-left' : rows[0].margin+'cm'}" id="carousel0"  
            class="transition" @mouseover="endHover(0)" @mouseleave="resumeHover(0)"   >
                <a v-for="(destination,index) in rows[0].recettes" :href="destination.link" :key="index+'car0'"
                target="_blank" class="col-md-1" :id="index" @click="endHover(0);endHover(1);endHover(2)" >
                    <img class="image-recette" :src="destination.src"> 
                </a>
                <a class="col-md-1" style="animation-duration: 2s" id="loading0">
                    <div class="image-waiting" :style="{'background-color': getBGColor()}">
                        <grid-loader :loading="true" color="white" 
                        style="margin-left:auto;margin-right:auto;padding-top:1.2cm"></grid-loader>
                    </div>
                </a>
            </div>
        </div>
        <div class="container-row-images row col-md-12">
            <div v-bind:style="{'padding-left' : rows[1].padding+'cm'}" ></div>
            <div v-bind:style="{'margin-left' : rows[1].margin+'cm'}" id="carousel1" 
            class="transition" @mouseover="endHover(1)" @mouseleave="resumeHover(1)"   >
                <a v-for="(destination,index) in rows[1].recettes" :href="destination.link"  :key="index+'car1'"  
                target="_blank" class="col-md-1" :id="index" @click="endHover(0);endHover(1);endHover(2)" >
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
            <div v-bind:style="{'padding-left' : rows[2].padding+'cm'}" ></div>
            <div v-bind:style="{'margin-left' : rows[2].margin+'cm'}" id="carousel2"  
            class="transition" @mouseover="endHover(2)" @mouseleave="resumeHover(2)"   >
                <a v-for="(destination,index) in rows[2].recettes" :href="destination.link" :key="index+'car2'"
                target="_blank" class="col-md-1" :id="index" @click="endHover(0);endHover(1);endHover(2)" >
                    <img class="image-recette" :src="destination.src"> 
                </a>
                <a class="col-md-1" style="animation-duration: 2s" id="loading2">
                    <div class="image-waiting" :style="{'background-color': getBGColor()}">
                        <grid-loader :loading="true" color="white" 
                        style="margin-left:auto;margin-right:auto;padding-top:1.2cm"></grid-loader>
                    </div>
                </a>
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
            key2 : Number(0),
            key3 : Number(0),
            rows : [
                {
                    recettes : [],
                    margin : 0,
                    savedMargin : 0,
                    padding : 0,
                    ready : false,
                    loading : false,
                    running : true,
                },
                {
                    recettes : [],
                    margin : 0,
                    savedMargin : 0,
                    padding : 0,
                    ready : false,
                    loading : false,
                    running : true,
                },
                {
                    recettes : [],
                    margin : 0,
                    savedMargin : 0,
                    padding : 0,
                    ready : false,
                    loading : false,
                    running : true,
                }
            ],

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
            console.log('end hover row :   '+row)
            if(this.rows[row].ready){
                var boxOne = document.getElementById('carousel'+row)
                this.rows[row].running = false;
            }
            if(boxOne != null){
                this.rows[row].savedMargin = this.rows[row].margin

                var computedStyle = window.getComputedStyle(boxOne),
                marginLeft = computedStyle.getPropertyValue('margin-left');
                boxOne.style.marginLeft = marginLeft;
                
                boxOne.classList.remove('transition');
            }
        },
        launch(row){
            console.log('launch row :   '+row)
            if(this.rows[row].margin == 0){
                setInterval(() => {
                    if(this.rows[row].running ){
                        var totalWidth =  $(window).width()
                        var nbImage = Math.round(totalWidth / 230) ;
                        if(this.rows[row].recettes.length < nbImage +5 ){
                            this.crawlRecettes(row,false)
                        }
                    }
                },1000)
                setInterval(() =>{
                    if(this.rows[row].running && this.rows[row].ready){
                        this.rows[row].margin -= 6.2
                    }
                },10000)
                setInterval(() => {
                    var nodes = document.getElementById('carousel'+row).childNodes
                    if( nodes != null && nodes.length > 2 && nodes[1].getBoundingClientRect().x < 0){
                        this.rows[row].recettes.splice(0,1)
                        this.rows[row].padding += 6.3 ;
                        if(this.rows[row].running ){
                            var totalWidth =  $(window).width()
                            var nbImage = Math.round(totalWidth / 230) ;
                            if(this.rows[row].recettes.length < nbImage +5 ){
                                this.crawlRecettes(row,false)
                            }
                        }
                    }
                    var totalWidth =  $(window).width()
                    // check if loading screen has arrived
                    if ( this.rows[row].ready && document.getElementById('loading'+row).getBoundingClientRect().right < totalWidth ){
                        this.rows[row].ready = false;
                        var boxOne = document.getElementById('carousel'+row)
                        var computedStyle = window.getComputedStyle(boxOne),
                        marginLeft = computedStyle.getPropertyValue('margin-left');
                        boxOne.classList.remove('transition');
                        boxOne.style.marginLeft = marginLeft;
                    }
                },250)
                var boxOne = document.getElementById('carousel'+row)
                boxOne.classList.add('transition')
                this.rows[row].margin -= 6.2
            }
            
        },
        resumeHover(row){
            console.log('resume hover row :   '+row)
            var previouStateRun = this.rows[row].running
            this.rows[row].running = true
            var boxOne = document.getElementById('carousel'+row)
            boxOne.classList.add('transition')
            if(this.rows[row].ready && previouStateRun == false){
                this.rows[row].margin = this.rows[row].savedMargin - 0.001;
                this.rows[row].margin = this.rows[row].savedMargin + 0.001;
            }
        },
        crawlRecettes(row,start){
            
            axios.get('/crawlRecettes')
            .then((response)=>{
                console.log(response.data.src)
                if(response.data.src != null ){
                    var totalWidth =  $(window).width()
                    var nbImage = Math.round(totalWidth / 230) ;
                    console.log(this.rows[row].running)
                    if(this.rows[row].running ){
                        this.rows[row].recettes.push(response.data);
                        
                        if(this.rows[row].recettes.length >= nbImage){
                            if(this.rows[row].ready == false){
                                this.rows[row].ready= true;
                                this.launch(row)
                            }
                        }else{
                            
                            this.crawlRecettes(row,true)
                        }
                    }
                }
            },(error)=>{
                console.log(error);
            });

        },
    },

    
    beforeMount(){
        // taille de l'image 226.76678
        var totalWidth =  $(window).width()
        var nbImage = Math.round(totalWidth / 230) ;
        
        setTimeout( ()=>{
            this.show = true;
            setTimeout( () =>{
                for (let index = 0; index < nbImage +2; index++) {
                    this.crawlRecettes(0,true);
                    this.crawlRecettes(1,true);
                    this.crawlRecettes(2,true);
                }
            },1000)
        },500)
        
        $(window).focus( $.proxy(function(){
            this.resumeHover(0)
        },this));

        $(window).blur( $.proxy(function(){
            this.endHover(0)
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
