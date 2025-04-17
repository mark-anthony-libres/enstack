from fastapi import APIRouter, Depends
from .models import LoginClass, Letter, LetterInput
from database import get_db
from sqlalchemy.orm import Session
from typing import List, Set
import random

router = APIRouter()



@router.post("/login", description="""
a. **POST /api/login**
             
b. Inputs are `username` and `password` in JSON.
             
c. Case insensitively validates usernames with at least 4 letters and the letters "a", "b", and "c" are in the username in that order. Please see the examples below:
    
             i. `abacca` is validated
    
             ii. `Cabbie` is not validated since there is no `c` that comes after `ab`
    
             iii. `Acaiberrycake` is valid

d. Password will be valid if it is equal to the reverse of the username.
""")
def login(request : LoginClass):
    return f"Successfully login as {request.username}"




@router.get("/letters", 
summary="List letters",
description="""
a. GET /api/letters  
             
b. Seed your database with the following data (you may use an in memory data or  use a third party database application. If you do use an external database, make   sure that it is included in the submission by submitting a docker image)  

             i. {“letter”:”A”, “value”:1, “strokes”:2, “vowel”:true},{“letter”:”B”, “value”:2,  “strokes”:1, “vowel”:false}
              
             ii. You may represent the data in your database however you like as long as  
             the expected API outputs are met  

c. This should return a json of all unique letters in the database sorted by value in ascending order. Given the seed data, this should return {“letters”:[“A”, “B”]}
             
""")
def get_letters(db: Session = Depends(get_db)):
    letters = db.query(Letter).order_by(Letter.value).all()
    return {"letters": [letter.letter for letter in letters]}



@router.post("/letter/add", 
summary="Add letter",
description="""
a. POST /api/letter/add

b. Input is a json object containing the following fields:

        i. Letter: string

        ii. Value: int - any random value

        iii. Strokes: int - any number that is not equal to value

        iv. Vowel: bool - if the letter is treated as a vowel or not

c. Letters must be unique and not limited to the latin alphabet

i. Hence a request with {“letter”:”A”, “value”:1, “strokes”:2, “vowel”:true} will fail

d. Return {‘status”:0} if the letter was added to the database otherwise return {“status”:1}          
""")
def post_add_letters(data: LetterInput, db: Session = Depends(get_db)):
   existing_letter = db.query(Letter).filter(Letter.letter == data.letter).first()
   if existing_letter:
        return {"status" : 1}
   
   new_letter = Letter(**data.model_dump())
   
   db.add(new_letter)
   db.commit()
   return {"status": 0}




@router.get("/letter/{letter}", 
summary="Get letter",
description="""
a. GET /api/letter/<letter:str>

b. Returns the details of the letter in the URL

    i. /api/letter/A will return {“letter”:”A”, “value”:1, “strokes”:2, “vowel”:true}  
""")
def get_specifying_letter(letter: str, db: Session = Depends(get_db)):
    found = db.query(Letter).filter(Letter.letter == letter).first()
    
    if not found:
        return {}
    
    return found  


"""
fastAPI sees /letter/shuffle and matches it to /letter/{letter} — because from FastAPI perspective, 
"shuffle" is just a string that could be the {letter} parameter. so i add 's' in the 'letter' part of the route
"""

@router.get(path="/letters/shuffle",
summary="Shuffle letters",
description="""
a. GET /api/letter/shuffle

b. Returns a string containing all the letters in the database without repetition but in a random order

c. Plus points will be given for implementing your own shuffle function
"""
)
def shuffle_letters(db: Session = Depends(get_db)):

    def custom_shuffle(value : List):
        n = len(value)
        for i in range(n):
            j = random.randint(i, n - 1)
            value[i], value[j] = value[j], value[i]

        return value

    letters: Set[str] = {row.letter for row in db.query(Letter).all()}

    if not letters:
        return {"shuffled": ""}

    result = custom_shuffle(list(letters).copy())

    return "".join(result)
   


@router.get(path="/letter/filter/{val}",
summary="Filter letters",
description="""
a. GET /api/letter/filter/<val:int>

b. Returns a list of letters whose value field is less than or equal to val ordered by when they were added to the database

    i. On the original set, accessing /api/letter/filter/1 this should return {“letters”:[“A”]}
"""
)
def filter_litters(val : int, db: Session = Depends(get_db)):

    results = (
        db.query(Letter)
        .filter(Letter.value <= val)
        .order_by(Letter.id.asc()) 
        .all()
    )

    return {"letters": [per.letter for per in results]}


    pass