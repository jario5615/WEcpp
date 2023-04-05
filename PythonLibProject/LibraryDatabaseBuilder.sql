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

INSERT INTO Author (AuthorId, FirstName, LastName, Gender, DateOfBirth, DateOfDeath) 
			VALUES(5, 'George', 'Orwell', 'M', '1903-6-25', '1950-1-21');

INSERT INTO Author (AuthorId, FirstName, LastName, Gender, DateOfBirth, DateOfDeath) 
			VALUES(6, 'Agatha', 'Christie', 'F', '1890-9-15', '1976-1-12');

INSERT INTO Author (AuthorId, FirstName, LastName, Gender, DateOfBirth)
			VALUES (7, 'Margaret', 'Atwood', 'F', '1939-11-18');
            
INSERT INTO Author (AuthorId, FirstName, LastName, Gender, DateOfBirth)
			VALUES (8, 'Haruki', 'Murakami', 'M', '1949-01-12');
            
INSERT INTO Author (AuthorId, FirstName, LastName, Gender, DateOfBirth)
			VALUES(9, 'Neil', 'Gaiman', 'M', '1960-11-10');

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
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES(15, 5, 3, 'Nineteen Eighty-Four', 'follows the life of Winston Smith, a low ranking member of \'the Party\', 
            who is frustrated by the omnipresent eyes of the party, and its ominous ruler Big Brother. 
            \'Big Brother\' controls every aspect of people\'s lives.', '1949-6-8');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES(16, 5, 6, 'Down and Out in Paris and London', 'Down and Out reflects the author\'s preoccupation with social inequality and the 
            conditions that create homelessness. The book begins by describing the protagonist\'s stay in Paris, where he works as a dishwasher, 
            before he moves back to England to explore life on the margins in London.', '1933-1-9');
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES(17, 6, 4, 'Murder on the Orient Express', '"Murder on the Orient Express" by Agatha Christie is a classic whodunit novel 
            set on a luxurious train journey through Europe. Follow detective Hercule Poirot as he attempts to solve a murder with a cast of colorful 
            characters and clever clues that will keep you guessing until the very end.', '1934-1-1');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES (18, 6, 4, 'And Then There Were None', 'Ten strangers are lured to an island by an unknown host, only to find themselves trapped and killed off one by one.
			As the tension and suspicion grows, they must solve the mystery before they all meet their demise. A thrilling and suspenseful
			classic mystery novel by Agatha Christie.', '1939-11-6');
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES (19, 6, 4, 'The Murder of Roger Ackroyd', 'In this classic whodunit, a wealthy man is found dead, and all clues point to his widow. But is she really guilty?
			Detective Hercule Poirot sets out to solve the mystery in a suspenseful and unpredictable tale that will keep readers guessing
			until the very end.', '1926-6-19');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES (20, 1, 1, 'Pet Sematary', 'In Stephen King\'s horror novel "Pet Sematary," a family moves to a rural town in Maine and discovers a cursed burial ground
			that has the power to bring the dead back to life. As the family\'s tragedies unfold, they become entangled in the supernatural forces
			that haunt the land.' , '1983-11-14');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES (21, 7, 2, 'The Handmaid''s Tale', 'In a dystopian future, fertile women are forced to bear children for wealthy families. Follow Offred, a Handmaid,
			 as she navigates life under a repressive regime.', '1985-09-01');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES (22, 7, 2, 'Alias Grace', 'Based on a true story, Alias Grace tells the tale of a young woman convicted of murder in 19th century Canada. But was she really guilty?
			 Dr. Simon Jordan is hired to find out.', '1996-09-01');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES (23, 7, 5, 'The Edible Woman', 'Marian feels like she is losing her identity as she tries to fit into society''s expectations of women. Can she break free from the mold
			 and find her true self?', '1969-01-01');
            
INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES (24, 8, 2, 'Kafka on the Shore', 'A boy named Kafka Tamura runs away from home to escape his father''s curse and seeks refuge in a library in Takamatsu. Meanwhile,
			 an old man named Nakata experiences strange phenomena and sets out on a journey to find Kafka. Their paths intersect in unexpected ways.', '2002-01-01');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES (25, 8, 3, 'Hard-Boiled Wonderland and the End of the World', 'A man known only as the "Narrator" is employed as a "Calcutec" by the System, a vast network of computers
			 that manage society. His job is to read encoded messages from the System''s mainframe, but he soon finds himself drawn into a surreal underworld
			 of dreamlike proportions.', '1985-01-01');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES (26, 8, 6, 'What I Talk About When I Talk About Running', 'A memoir about the author''s experience with long-distance running, Murakami reflects on his career
			 as a novelist and how running has influenced his life and writing. It also explores his philosophy on the importance of discipline, perseverance, and the journey over
			 the destination.', '2007-01-01');
             
INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES(27, 9, 2, 'American Gods', 'Ex-convict Shadow Moon becomes embroiled in a battle between gods of the old world and the new, led by Mr. Wednesday,
            in this sweeping tale of magic and myth set across America.', '2001-6-19');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES(28, 9, 1, 'The Sandman Vol. 1: Preludes and Nocturnes', 'The first volume of Gaiman\'s critically acclaimed graphic novel series "The Sandman", in which the lord of dreams
			 is captured and held prisoner for seventy years, leading to a quest for his freedom and restoration of his realm.', '1991-1-1');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES(29, 9, 2, 'Stardust', 'Young Tristan Thorn embarks on a perilous journey through Faerie to retrieve a fallen star for his beloved, encountering witches, sky pirates,
			 and other magical creatures along the way.', '1999-10-1');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES(30, 9, 3, 'Neverwhere', 'When London resident Richard Mayhew helps an injured girl on the street, he is plunged into the dangerous and fantastical world of "London Below",
			 where the people and places exist outside of ordinary reality.', '1996-9-16');

INSERT INTO Book (BookId, AuthorId, GenreId, Title, Synopsis, PublicationDate)
			VALUES(31, 9, 1, 'The Ocean at the End of the Lane', 'A middle-aged man returns to his childhood home and the memories of a terrifying and otherworldly experience that occurred there,
			 involving a family of witches and a dark force from beyond the universe.', '2013-6-18');
