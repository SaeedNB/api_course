<?php
header('Access-Controll-Allow-Origin: *');
header('Content-Type: application/json');
include_once('../../config/Database.php');
include_once('../../model/book.php');
$database = new Database();
$db = $database->connect();
$book = new Book($db);
$result = $book->read();
$num = $result->rowCount();
if ($num>0){
    $book_arr = array();
    $book_arr['data'] = array();
    while($row= $result->fetch(PDO::FETCH_ASSOC)){
        extract($row);
        $book_item = array(
            'id'=> $id,
            'name'=> $name,
            'author'=> $author
        );
    array_push($book_arr['data'], $book_item);
    }
    echo json_encode($book_arr);
}else {
    echo json_encode(array("message"=> "No book found"));
}
?>