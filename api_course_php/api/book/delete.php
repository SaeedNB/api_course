<?php
header('Access-Controll-Allow-Origin: *');
header('Content-Type: application/json');
include_once('../../config/Database.php');
include_once('../../model/book.php');
$database = new Database();
$db = $database->connect();
$book = new Book($db);
$id = $_GET['id'];
$res = $book->delete($id);
if ($res == TRUE){
    echo json_encode(array("message"=> "Post deleted"));
}else {
    echo json_encode(array("message" => "error"));
}
?>