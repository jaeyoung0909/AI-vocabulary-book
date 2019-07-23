Product name : AI vocabulary book
Team name    : AI vocabulary book
Date         : July. 22. 2019 

# System Test scenarios

## Sprint 1

### User story 1
"As a user , I want a login system to get into the site to access the vocabulary book."

#### scenario 1. 
1. Connect AI vocabulary book website; click 'sign up'; type 
- name = "jae"
- password = "jaejae1498"
- password confirmation = "jaejae1498"
- click 'sign up' button
- User should see text area in redirected web page

#### scenario 2. 
1. Connect AI vocabulary book website; click 'log in'; 
2. User should see id, passward submit box
3. Type 
- name = "admin"
- password = "aivoc"
- User should see text area in redirected web page

## Sprint 2

### User story 1
" As a user, I want to input texts to see the frequencies of the words in the text "

#### scenario 1.
1. Connect AI vocabulary book website; click 'log in'; type
- name = 'admin'
- password = 'aivoc'
- User should see text area in redirected web page
2. Copy CNN articles which I am reading; Paste it in the text area; click 'frequency words'
3. User should see at most 17 words list under the text area

## Sprint 3

### User story 1
"" As a user, I want to review my unknwon words, so that I can see what words were previously unknwon (they still might be unfamiliar). "

#### scenario 1.
1. Connect AI vocabulary book website; click 'log in'; type 
- name = 'admin'
- password = 'aivoc'
- User should see 'Recommandations' button under the text area
2. Click 'Recommandations' button; User should see words list which is unfamiliar.
