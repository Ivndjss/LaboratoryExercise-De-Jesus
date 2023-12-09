# LaboratoryExercise-De-Jesus
Application Development Laboratory Exercise


## Laboratory Exercise
Using the string below:

myString =""To understand the need for creating a class let us consider an example: Let us
say that you wanted to track the number of dogs which may have different attributes like
breed, and age. If a list is used, the first element could be the dog’s breed while the second
element could represent its age. Let's suppose there are 100 different dogs, then how would
you know which element is supposed to be which? What if you wanted to add other 
properties to these dogs? This lacks organization and it’s the exact need for classes. ””

##What to do:

**a) import Counter from collections**
**b) split the string by words**
**c) get and display the counts for each words**

**e.g.**

*string = "How many times does each word show up in in this sentence of word string”*

*Counter({'How':1,'many':1,"times':2,'does':1, 'each':4, 'word':2, 'show':1, 'up':1, 'in':2, 'this':1, 
'sentence’:1, 'of':1, ‘string':1}]*

1) Display the number of the word occurrences and the first 5 tapmost common words mentioned
in myString.
2) Display the total number of words in myString
3) Display all the items sets (keywords and values) of all words in myString
4) Display the count of a specific word from myString

     Example. In: [('word')]
              Out: 2

5) Create a script in Python using your Jupyter Notebook and display the output needed.

Steps: import datetime

        given data:
              t1 = datetime.time(4, 20, 1)
              t2 = datetime.time(6, 20, 1)

Show the different components of object t1
          Output:
        
              04:20:02
              hour : 4
              minute: 20
              second: 1
              microsecond: 0
              tzinfo: None

6) Using the ***combine*** method get the time difference of the time given below from the
Start time until End time:

 

          **Input:**
                 #set Start time
                      d1 = datetime.time(8,0,0)
                      print('Start time......', d1)
                 #set End time
                      d2 = datetime.time(12,0,0)
                      print('End time .......',d2)
          
          **Output:**
                 Start time...... 08:00:00
                 End time ....... 12:00:00
                 
                 Time difference: 4:00:00

7) Create a class with the name **Candidate**. with the following instance attributes/states:
***name, Position.*** To run add class attribute **votes** to record all the votes of candidates,
Create a **setVotes** method, to enter data into the object you are to instantiate. Create
another method name **getVotes** to access the vote of the candidates and another
method to serve as **interface**: follow the program structure set below

         class Candidate(object):
     
             #class attribute
             #contructor/initialization of class Candidate
             #method to set votes data
             #method to get votes data
                   
             #method for interface
                        
             #instantiate objects of Candidates
                        
             for x in range(10}:
                  dispCandid()
                  voteCast = int(input('Enter code to cast your vote'))
          
             #set vote
             candi1.setVotes(voteCast)
          
             #get vote
             candi1.getVotes()
             d = dict(Counter(Candidate.votes))







# Documentation for the Laboratory Exercise

**1) Display the number of the word occurrences and the first 5 tapmost common words mentioned in myString.**

**2) Display the total number of words in myString.**

**3) Display all the items sets (keywords and values) of all words in myString.**

**4) Display the count of a specific word from myString.**


### myString.py
     from collections import Counter
     
     myString = "To understand the need for creating a class let us consider an example: Let us say that you wanted to track the number of dogs which may have different attributes like breed, and age. If a list is used, the first element could be the dog’s breed while the second element could represent its age. Let's suppose there are 100 different dogs, then how would you know which element is supposed to be which? What if you wanted to add other properties to these dogs? This lacks organization and it’s the exact need for classes."

     words = myString.split()
     word_counts = Counter(words)

### Display the number of the word occurrences and the first 5 most common words mentioned in myString.
     print(word_counts.most_common(5))

### Display the total number of words in myString
     print(len(words))

### Display all the items sets (keywords and values) of all words in myString
     print(word_counts.items())

### Display the count of a specific word from myString
     print(word_counts['word'])
