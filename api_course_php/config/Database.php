<?php
class Database {
    private $host = "localhost";
    private $dbName = "api_course";
    private $username = "root";
    private $password = "";
    private $conn;

public function connect(){
    $this->conn = null;
    try{
         $this->conn = new PDO('mysql:host='.$this->host.';dbname='.$this->dbName, $this->username, $this->password);
         $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch(PDOException $e){
        echo 'connection error: '. $e->getMessage();
    }
    return $this->conn;
}
}
?>