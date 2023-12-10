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

## What to do:

**a) import Counter from collections**

**b) split the string by words**

**c) get and display the counts for each words**

**e.g.**

*string = "How many times does each word show up in in this sentence of word string”*

*Counter({'How':1,'many':1,'times':1,'does':1, 'each':1, 'word':2, 'show':1, 'up':1, 'in':2, 'this':1, 
'sentence':1, 'of':1, 'string':1}]*

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
     ivndjss = Counter(words)

#### Display the number of the word occurrences and the first 5 most common words mentioned in myString.
     print(ivndjss.most_common(5))

#### Display the total number of words in myString
     print(len(words))

#### Display all the items sets (keywords and values) of all words in myString
     print(ivndjss.items())

#### Display the count of a specific word from myString
     print(ivndjss['word'])

#### The Result
    myString.py
     [('the', 6), ('to', 4), ('you', 3), ('element', 3), ('need', 2)]
     95
     dict_items([('To', 1), ('understand', 1), ('the', 6), ('need', 2), ('for', 2), ('creating', 1), ('a', 2), ('class', 1), ('let', 1), ('us', 2), ('consider', 1), ('an', 1), ('example:', 1), ('Let', 1), ('say', 1), ('that', 1), ('you', 3), ('wanted', 2), ('to', 4), ('track', 1), ('number', 1), ('of', 1), ('dogs', 1), ('which', 2), ('may', 1), ('have', 1), ('different', 2), ('attributes', 1), ('like', 1), ('breed,', 1), ('and', 2), ('age.', 2), 
     ('If', 1), ('list', 1), ('is', 2), ('used,', 1), ('first', 1), ('element', 3), ('could', 
     2), ('be', 2), ('dog’s', 1), ('breed', 1), ('while', 1), ('second', 1), ('represent', 1), ('its', 1), ("Let's", 1), ('suppose', 1), ('there', 1), ('are', 1), ('100', 1), ('dogs,', 1), ('then', 1), ('how', 1), ('would', 1), ('know', 1), ('supposed', 1), ('which?', 1), ('What', 1), ('if', 1), ('add', 1), ('other', 1), ('properties', 1), ('these', 1), ('dogs?', 1), ('This', 1), ('lacks', 1), ('organization', 1), ('it’s', 1), ('exact', 1), ('classes.', 1)])
     0


### Datetime_1.py (5)

#### Import the datetime module
          import datetime

#### Create two time objects, t1 and t2, using the time() function from the datetime module
#### The time() function returns a time object with hour, minute, and second
          t1 = datetime.time(4, 20, 1)
          t2 = datetime.time(6, 20, 1)

#### Print the time object t1
          print(t1)

#### Print the hour part of the time object t1
          print('hour :', t1.hour)

#### Print the minute part of the time object t1
          print('minute:', t1.minute)

#### Print the second part of the time object t1
          print('second:', t1.second)

#### Print the microsecond part of the time object t1
          print('microsecond:', t1.microsecond)

#### Print the tzinfo (time zone information) of the time object t1
#### By default, this is None as no time zone is specified
          print('tzinfo:', t1.tzinfo)


This script creates two `datetime.time` objects, `t1` and `t2`, with the specified hours, minutes, and seconds. It then prints the `t1` object and its components (hour, minute, second, microsecond, and tzinfo). The `datetime.time` function returns a time object initialized with the given arguments. If tzinfo (time zone info) is not provided, it is set to `None`. The `print` statements display the time object and its components. Note that the `tzinfo` attribute is `None` because no time zone information was provided when creating `t1` and `t2`. If you want to work with time zones, you'll need to use `datetime`'s `timezone` or `tzinfo` objects.


### Datetime_2.py (6)
#### Import the datetime module
     import datetime

#### Create two datetime objects, d1 and d2, using the combine() function from the datetime module
#### The combine() function returns a datetime object with the specified date and time
#### datetime.date.today() returns the current local date
#### datetime.time(8,0,0) and datetime.time(12,0,0) return time objects with the specified hours, minutes, and seconds
     d1 = datetime.datetime.combine(datetime.date.today(), datetime.time(8,0,0))
     d2 = datetime.datetime.combine(datetime.date.today(), datetime.time(12,0,0))

#### Print the time part of the datetime object d1
     print('Start time......', d1.time())

#### Print the time part of the datetime object d2
     print('End time .......',d2.time())

#### Calculate the time difference between d2 and d1 in hours, minutes, and seconds
#### The difference (d2-d1) returns a timedelta object
#### The seconds attribute of a timedelta object returns the number of seconds
#### Use integer division (//) and modulus (%) to convert seconds to hours, minutes, and seconds
     print('Time difference:', (d2-d1).seconds//3600, ':', ((d2-d1).seconds//60)%60, ':', (d2-d1).seconds%60)

This script creates two `datetime.datetime` objects, `d1` and `d2`, with the current date and specified times (8:00:00 and 12:00:00, respectively). It then prints the time components of `d1` and `d2`. Finally, it calculates and prints the time difference between `d2` and `d1` in hours, minutes, and seconds. The `datetime.datetime.combine()` function returns a datetime object with the specified date and time. The `datetime.date.today()` function returns the current local date. The `datetime.time()` function returns a time object with the specified hours, minutes, and seconds. The difference between two datetime objects returns a `datetime.timedelta` object, which represents a duration. The `seconds` attribute of a timedelta object returns the number of seconds in the duration. The script uses integer division (`//`) and modulus (`%`) to convert the number of seconds to hours, minutes, and seconds.


### Voting.py

#### Import the Counter class from the collections module
     from collections import Counter

#### Define a class named Candidate
     class Candidate(object):
#### Initialize an empty list named votes
#### This list will hold the votes for each Candidate object
         votes = []

#### The __init__ method is the constructor for the class
#### It initializes a new Candidate object with a name and a position
     def __init__(self, name, position):
          self.name = name
          self.position = position

#### the setVotes method adds a vote to the votes list
    def setVotes(self, vote):
        self.votes.append(vote)

#### The getVotes method returns a dictionary with the count of each vote
#### It uses the Counter class to count the votes and then converts the Counter object to a dictionary
    def getVotes(self):
        return dict(Counter(self.votes))

#### Create a Candidate object named candi1 with the name 'John Doe' and the position 'President'
     candi1 = Candidate('John Doe', 'President')

#### Use a for loop to get 10 votes from the user
#### The user is asked to enter a code to cast their vote
#### The code is converted to an integer and then added to the votes list of the candi1 object
     for x in range(10):
         voteCast = int(input('Enter code to cast your vote'))
         candi1.setVotes(voteCast)

#### Print the count of each vote for the candi1 object
     print(candi1.getVotes())


This script defines a `Candidate` class with methods for setting and getting votes. An instance of the `Candidate` class, `candi1`, is created with the name 'John Doe' and the position 'President'. The script then prompts the user to enter a vote code 10 times. Each vote code is added to the `votes` list of the `candi1` object. Finally, the script prints a dictionary with the count of each vote for `candi1`. The `Counter` class from the `collections` module is used to count the votes. The `Counter` object is then converted to a dictionary and returned by the `getVotes` method. Note that the `votes` list is a class variable and will be shared by all instances of the `Candidate` class. If you want each `Candidate` object to have its own `votes` list, you should move the `votes = []` line to the `__init__` method.
