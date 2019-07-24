Product name : AI vocabulary book

Team name    : AI vocabulary book

Date         : July 22nd, 2019 

# System Test scenarios

## Sprint 1

### User story 1
"As a user, I want a login system to get into the site to access the vocabulary book."

#### scenario 1. 
1. Connect AI vocabulary book website; click 'sign up'; type 
- Name = "jae"
- Password = "jaejae1498"
- Password confirmation = "jaejae1498"
- Click "sign up" button
- User should see text area in redirected web page

#### scenario 2. 
1. Connect to AI vocabulary book website; click "log in" 
2. User should see id, password submit box
3. Type:
- name = "admin"
- password = "aivoc"
- User should see text area in redirected web page

## Sprint 2

### User story 1
"As a user, I want to input texts to see the frequencies of the words in the text."

#### scenario 1.
1. Connect AI vocabulary book website
2. Click 'log in'
3. Type
- name = 'admin'
- password = 'aivoc'
- User should see text area in redirected web page
4. Copy CNN articles which I am reading and paste it into the text area
4. Click 'frequency words'
5. User should see at most 17 words list under the text area

## Sprint 3

### User story 1
"As a user, I want to review my unknwon words, so that I can see what words were previously unknown (they still might be unfamiliar)."

#### scenario 1.
1. Connect AI vocabulary book website and click 'log in'
2. Type 
- Name = 'admin'
- Password = 'aivoc'
- User should see 'Recommendations' button under the text area
3. Click 'Recommendations' button - the user should see a list of their unfamiliar words.



# Unit Tests
### Refer to Testing.md

We have 3 models User, Vocabulary and Ability. And make test code to check whether they work properly.
