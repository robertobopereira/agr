<?php
$host = "banco";
$database = "usuario";
$username = "usuario";
$password = "123456";



$conexao = mysqli_connect($host, $username, $password, $database);


if (!$conexao) {

    die("Não foi possível conectar: " . mysqli_connect_error());

}

echo "Conexão realizada com sucesso!";

mysqli_close($conexao);
?>
