<template>
    <div class="footer">
        <div class="content">
            <div class="nous-contacter row col-md-12">
                <div class="container-logo-footer col-md-2">
                    <v-lazy-image :src="logo" />
                </div>
                <div class="text col-md-10">
                    <p>
                        DinnerSeek est un catalog de recettes choisies aléatoirement parmis une multitude de sitesweb 
                        dédiés à la cuisine. La recherche des recettes se fait dynamiquement et pendant votre 
                        visite de notre siteweb via un robot qui va récolter de façon aléatoire des recettes sur 
                        une dizaine de sites.
                    </p>
                    <center>
                        <p>
                            Toutes vos remarques ou intérrogations sont les bienvenues sur <b>dl_ikhadallem@esi.dz</b>
                        </p>
                    </center>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                logo: require('../../../public/img/logo.png'),
            }
        },
    }
</script>

<style>
    @import url('https://fonts.googleapis.com/css?family=Roboto');
    .v-lazy-image {
        transform: translate3d(50% ,0 ,0);
        opacity: 0;
        transition: all 0.5s ;
    }
    .v-lazy-image-loaded {
        opacity: 1;
        transform: translate3d(0 ,0 ,0);
    }
    .nous-contacter .container-logo-footer{
        width: 3.5cm;
    }
    .nous-contacter img{
        width: 100%;
        height: auto;
        margin-top: .5cm;
    }
    .footer{
        width: 100%;
        background-color: #222;
        bottom: 0;
        display: flex;
        flex-direction: row;
        color: white;
        font-family: 'Roboto';
        padding-left: 0 ;
        padding-right: 0 ;
    }
    .footer .content{
        display: flex;
        flex-direction: row;
        margin-left: auto;
        margin-right: auto;
    }
    .nous-contacter{
        display: flex;
        flex-direction: row;
    }
    .nous-contacter .text{
        text-align: left;
        padding: .4cm 0 0 1cm ;
    }

    @media(min-width : 992px){
        .footer .content{
            width: 95%;
        }
    }

    
</style>