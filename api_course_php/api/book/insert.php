<?php
header('Access-Controll-Allow-Origin: *');
header('Content-Type: application/json');
include_once('../../config/Database.php');
include_once('../../model/book.php');
$database = new Database();
$db = $database->connect();
$book = new Book($db);
$request_body = file_get_contents("php://input");
$data = json_decode($request_body);
$res = $book->insert($data-> {"name"}, $data-> {"author"});
if ($res == TRUE){
    echo json_encode(array("message"=> "Post inserted"));
}else {
    echo json_encode(array("message" => "error"));
}
?>