DROP DATABASE IF EXISTS LibraryDatabase;
CREATE DATABASE LibraryDatabase;
USE LibraryDatabase;

CREATE TABLE Author(
	AuthorId INT PRIMARY KEY NOT NULL,
    FirstName VARCHAR(25) NOT NULL,
    MiddleName VARCHAR(25),
    LastName VARCHAR(50) NOT NULL,
    Gender VARCHAR(1),
    DateOfBirth DATETIME NOT NULL,
    DateOfDeath DATETIME
);

CREATE TABLE Genre(
	GenreId INT PRIMARY KEY NOT NULL,
    GenreName VARCHAR(25) NOT NULL
);

CREATE TABLE Book(
	BookId INT PRIMARY KEY NOT NULL,
    AuthorId INT NOT NULL,
    GenreId INT NOT NULL,
    Title VARCHAR(100) NOT NULL,
    Synopsis VARCHAR(500),
    PublicationDate DATETIME,
    FOREIGN KEY (AuthorId) REFERENCES Author(AuthorId) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (GenreId) REFERENCES Genre(GenreId) ON DELETE CASCADE ON UPDATE CASCADE
);
# Adding genres
INSERT INTO GENRE VALUES(1, 'Horror'), (2, 'Fantasy'), (3, 'Science Fiction'), (4, 'Mystery'), (5, 'Romance'), (6, 'Non-Fiction');

# Adding Authors
INSERT INTO Author (AuthorId, FirstName, MiddleName, LastName, Gender, DateOfBirth) 
			VALUES(1, 'Stephen', 'Edwin', 'King', 'M', '1947-9-21');
            
INSERT INTO Author (AuthorId, FirstName, MiddleName, LastName, Gender, DateOfBirth, DateOfDeath) 
			VALUES(2, 'John', 'Ronald Reuel', 'Tolkien', 'M', '1892-1-3', '1973-9-2');

INSERT INTO Author (AuthorId, FirstName, LastName, Gender, DateOfBirth) 
			VALUES(3, 'Joanne', 'Rowling', 'F', '1965-7-31');
            
INSERT INTO Author (AuthorId, FirstName, LastName, Gender, DateOfBirth, DateOfDeath) 
			VALUES(4, 'Jane', 'Austen', 'F', '1775-12-16', '1817-7-18');

# Adding Books
INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES(1, 4, 5, 'Pride and Prejudice', 'Follows the turbulent relationship between Elizabeth Bennet,
            the daughter of a country gentleman, and Fitzwilliam Darcy, a rich aristocratic landowner. 
            They must overcome the titular sins of pride and prejudice in order to fall in love and marry.',  '1813-1-28');
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title)
			VALUES(2, 4, 5, 'Sense and Sensibility');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, PublicationDate)
			VALUES(3, 1, 1, 'IT', '1986-9-15');
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES(4, 1, 1, 'The Shining', 'Danny is only five years old, but he is a \'shiner\', aglow with psychic voltage. 
            When his father becomes caretaker of the Overlook Hotel, Danny\'s visions grow out of control. 
            As winter closes in cuts them off, the hotel seems to develop a life of its own.', '1977-1-28');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis)
			VALUES(5, 1, 2, 'The Green Mile', 'In 1932 the newest resident on death row is John Coffey, 
            a giant black man convicted of the brutal murder of two little girls. But nothing is as it seems with John Coffey,
            and around him unfolds a bizarre and horrifying story.');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES(6, 2, 2, 'The Lord of the Rings', 'In the Shire, young Frodo Baggins finds himself faced with an immense task, 
            as the Ring is entrusted to his care. He must leave his home and make a perilous journey across Middle-earth to the Crack of Doom, 
            deep inside the territories of the Dark Lord.', '1954-7-29');
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES(7, 2, 2, 'The Hobbit', 'The Hobbit is set in Middle-earth and follows Bilbo Baggins, the titular hobbit, who joins the wizard 
            Gandalf and thirteen dwarves that make up Thorin Oakenshield\'s Company, on a quest to reclaim the dwarves\' 
            home and treasure from the dragon Smaug.', '1937-9-21');
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title, PublicationDate)
			VALUES(8, 3, 2, 'Harry Potter and the Philosopher\'s Stone', '1997-6-26');
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title, PublicationDate)
			VALUES(9, 3, 2, 'Harry Potter and the Chamber of Secrets', '1998-7-2');
		
INSERT INTO Book (BookId, AuthorId, GenreId, Title, PublicationDate)
			VALUES(10, 3, 2, 'Harry Potter and the Prisoner of Azkaban', '1999-7-8');
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title, PublicationDate)
			VALUES(11, 3, 2, 'Harry Potter and the Goblet of Fire', '2000-7-8');
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title, PublicationDate)
			VALUES(12, 3, 2, 'Harry Potter and the Order of the Phoenix', '2003-6-21');
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title, PublicationDate)
			VALUES(13, 3, 2, 'Harry Potter and the Half-Blood Prince', '2005-7-16');
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title, PublicationDate)
			VALUES(14, 3, 2, 'Harry Potter and the Deathly Hallows', '2007-7-21');

            
