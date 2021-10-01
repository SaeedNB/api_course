const express = require('express');
const app = express();
const port = 3000;
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

let books = [];

app.get('/books', (req, res)=> {
	res.json(books);
});

app.get('/books/:book_id', (req, res)=> {
        const book_id = req.params.book_id;
        for (let book of books){
	    if (book_id ===book.ID){
	        res.json(book);
		return;
	    }
	}
        res.status(404).send("book not found!")
});

app.post('/books', (req,res)=>{
        const book = req.body;
	books.push(book)
	res.send("new book added");
});
app.put('/books/:book_id', (req,res)=> {
    const book_id = req.params.book_id;
    const new_book = req.body;
    for (let i = 0; i<books.length; i++){
        book = books[i];
	if (book.ID === book_id){
		books[i] = new_book;
	}
    }
    res.send("book is updated");
});



app.delete('/books/:book_id', (req, res)=> {
    const book_id = req.params.book_id;
    books = books.filter(i => {
        if (i.ID !== book_id){
	    return true;
	}
	    return false;
    });
	res.send("book is deleted")
});

app.listen(port, ()=> console.log('Welcome! I listen to port 3000'));
