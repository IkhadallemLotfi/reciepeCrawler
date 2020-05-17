<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>DinnerSeek</title>
        <script src="{{ asset('js/app.js') }}" defer></script>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <meta name="csrf-token" content="{{ csrf_token() }}">
    </head>
    <body>
        <div  id="app">
            <user></user>
        </div>
        <div  id="footer">
            <foot></foot>
        </div>
    </body>
</html>

<style>
    body {
        margin : 0 !important;
    }
    #app{
        background-color : rgba(255,255,255,.7)
    }
</style>