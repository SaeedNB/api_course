<?php
header('Access-Controll-Allow-Origin: *');
header('Content-Type: application/json');
include_once('../../config/Database.php');
include_once('../../model/book.php');
$database = new Database();
$db = $database->connect();
$book = new Book($db);
$id = $_GET['id'];
$request_body = file_get_contents("php://input");
$data = json_decode($request_body);

$res = $book->update($id, $data-> {"name"}, $data-> {"author"});
if ($res == TRUE){
    echo json_encode(array("message"=> "Post updated"));
}else {
    echo json_encode(array("message" => "error"));
}
?>