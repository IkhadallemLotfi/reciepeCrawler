<?php


Route::get('/', function () {
    return view('welcome');
});

Route::get('/crawlRecettes','RecetteController@crawlRecettes');