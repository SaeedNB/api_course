package main

import (
     "encoding/json"
     "log"
     "net/http"
     "fmt"
     "io/ioutil"
     "github.com/gorilla/mux"
)

type book struct {
	ID     string  `json:"ID"`
	Name   string  `json:"Name"`
	Author string  `json:"Author"`
}

type allBooks []book

var books = allBooks {
	{
	    ID : "1",
            Name: "Learn Api",
	    Author: "SomeBody",
	},
}


func getAll(w http.ResponseWriter, r *http.Request){
	json.NewEncoder(w).Encode(books)
}

func getOneBook(w http.ResponseWriter, r *http.Request) {
        bookID := mux.Vars(r)["id"]
	for _, singleBook := range books{
	    if singleBook.ID == bookID{
	        json.NewEncoder(w).Encode(singleBook)
	    }
	}
}

func createNewBook(w http.ResponseWriter, r *http.Request){
        var newBook book
	reqBody, err :=ioutil.ReadAll(r.Body)
	if err != nil {
	      fmt.Fprintf(w, "Please insert correct book info")
	}
	json.Unmarshal(reqBody, &newBook)
	books = append(books, newBook)
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(newBook)

}

func updateBook(w http.ResponseWriter, r *http.Request){
       bookID := mux.Vars(r)["id"]
       var newBook book
       reqBody, err := ioutil.ReadAll(r.Body)
       if err != nil{
	       fmt.Fprintf(w, "Please insert correct book info")
       }
       json.Unmarshal(reqBody, &newBook)
       for i , singleBook := range books {
               if singleBook.ID == bookID{
	       singleBook.Name = newBook.Name
	       singleBook.Author = newBook.Author
	       books = append(books[:i], singleBook)
	       json.NewEncoder(w).Encode(singleBook)
	       }
       }

}

func deleteBook(w http.ResponseWriter, r *http.Request){
        bookID := mux.Vars(r)["id"]
	for i, singleBook := range books {
	   if bookID == singleBook.ID {
		   books = append(books[:i], books[i+1:]...)
	   }
	}
}


func main(){
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/books", getAll).Methods("GET")
	router.HandleFunc("/books/{id}", getOneBook).Methods("GET")
	router.HandleFunc("/books", createNewBook).Methods("POST")
	router.HandleFunc("/books/{id}", updateBook).Methods("PUT")
	router.HandleFunc("/books/{id}", deleteBook).Methods("DELETE")
	log.Fatal(http.ListenAndServe(":8080", router))
}
