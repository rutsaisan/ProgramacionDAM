<?php
  $cliente = [];
  $cliente['nombre'] = "Ruth";
  $cliente['apellidos'] = "Sainz Santos-Olmo";
  $cliente['email'] = "rutsaisan@gmail.com";

  $json = json_encode($cliente);
  echo $json;
  
  
?>