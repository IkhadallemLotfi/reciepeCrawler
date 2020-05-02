<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use DOMDocument;
use Goutte\Client;
use GuzzleHttp\Client as GuzzleClient;
use Config;
use DomXPath;
use Barryvdh\Debugbar\Facade as Debugbar;
use Log;

class RecetteController extends Controller
{
    public function steal(Request $request){
        DB::table('test')->insert(['etat'=> $request->test]);
    }

    public function crawlRecettes(){
        ini_set('max_execution_time', 0);
        $result = 0;
        $result = shell_exec('python crawl.py');
        Log::info($result);
        $resultData = json_decode($result, true);
        return $resultData;
    }
}