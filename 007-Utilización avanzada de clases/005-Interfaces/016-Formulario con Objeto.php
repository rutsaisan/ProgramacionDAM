<?php
	
  $cliente = [
  	"nombre" => "Ruth",
    "apellidos" => "Sainz Santos-Olmo",
    "email" => "rutsaisan.code@gmail.com"
  ];
  
  foreach($cliente as $clave=>$valor){
  	echo "<label>".$clave."</label>";
    echo "<input type='text' value='".$valor."'>";
  }

?>