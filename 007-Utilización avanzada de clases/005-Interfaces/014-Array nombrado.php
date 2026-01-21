<?php
	
  $campos_cliente = [
  	"nombre"=> "Ruth",
    "apellidos" => "Sainz Santos-Olmo",
    "email" => "rutsaisan.code@gmail.com"
  ];
  
  foreach($campos_cliente as $campo){
  	echo '<input type="text" placeholder="'.$campo.'"><br>';
  }

?>