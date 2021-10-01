<?php
class Book {
    private $conn;
    private $table_name = "books";
    public $id;
    public $name;
    public $author;

    public function __construct($db){
        $this->conn = $db;
    }

    public function read(){
        $query = 'SELECT * from '.$this->table_name ;
        $stmt = $this->conn->prepare($query);
        $stmt->execute();
        return $stmt;
    }

    public function insert($name, $author){
        $query = 'INSERT INTO '.$this->table_name.'(name, author)
        VALUES  ("'.$name.'" ,"'.$author.'")';
        if ($this->conn->query($query) == TRUE){
             return True;
        }else{
             return False;
        }
    }

    public function update($id, $name, $author){
        $query = 'UPDATE '.$this->table_name.' SET name= "'.$name.'", author="'.$author.'" where id= '.$id.'';
        return $this->conn->query($query);
    }

    public function delete($id){
        $query = 'DELETE from '.$this->table_name.' where id='.$id.'';
        return $this->conn->query($query);
    }

}
?>