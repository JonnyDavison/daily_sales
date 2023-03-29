# Daily Sales

### [Visit Live Site](https://daily-sales.herokuapp.com/) / [Visit Repository](https://github.com/JonnyDavison/daily_sales)

Daily Sales is a Code Institute Full-stack development program project built in Python. Made with the food indusrty in particular independant restaurants and food stores in mind. Providing a quick and simple analysis to track daily trends and store these in google sheets to refeclt on over time. 

![website image](images/blablabla.webp)
Visit the live site Here.
(link)


## CONTENTS
 - Project Overview
    - Project Goals
- User Experience
    - User Expectations
    - User Stories
- Design Structure
    - Flow chart
- Features
    - Intro
    - Name input
    - Guide
    - Quiz
    - More knowledge
    - Quiz end messages
    - Leaderboard update message and display
    - Quiz replay
    - Secret username
    - Front-end features
- Future Implementations
- Technologies Used
    - Languages Used
    - Programs Used
- Deployment
- Testing
- Credits
    - Code used and adapted
    - Acknowledgments

## Project Overview
Developing 'Daily Sales' has been a been a long time coming from the authors previous career. This daily analysis is essential to the succeful running of small and medium food buisness, where this information is key to decission making ahead of the following day. The development process included, reserach, indusrty knowlege and followed a logic flowchart. There are built in features to assit and guide the user throught the program:

- Error handeling to validate user input
- User feedback on the input (Custom ValueError messages)
- Text spacing for user readability 
- Useful information passed back quickly to the user
- Information stored in order to provide accounts for review

The project also uses Google Worksheet API for:
- Inputing and storing Data 
- Sales, Costs & Results pages to store financial data
- Pulling data for calulation
- Storing the calulation results
- Providing the user with a large data set
This is the [Google worksheet](https://docs.google.com/spreadsheets/d/1NckZYPLVFrlbqXG2FIFwfhZlNg0fQ67WtQURLmhWKC8/edit?usp=sharing) used to hold the data

## Project Goals
- Develop CLI based Sales analysis application using Python
- Request and present information in a clear and easy to understand manner
- Keep good UX principles regarding layout and interaction
- Robust Python code without issues/bugs

[Back to top ⇧](#daily-sales)

## User Experience
### User Expectations
- Able to quickly understand what the app is for
- Provide additional information directing the user 
- Iteractions have feedback
- Provide format instructions to assit in gathering the correct data
- No logic errors

### User Stories
- I want to know what is this site for
- I want to know what information to provide
- I want to store my information
- I want to get feedback on my interactions
- I want to get relavant information returned to me
- I want no bugs or issues in the program
[Back to top ⇧](#daily-sales)

## Design

### Structure
(images/flowchart.webp)

Flowchart was designed at the start of the project. The final result differs from the flowchart slightly on account of implementing changes for better UX.


[Back to top ⇧](#daily-sales)

## Features
Intro
Intro clear screen, quote and ASCII art

Intro clear screen, quote and ASCII art

Name input
Name input ok, capitalize name

Name input ok, capitalize name

Name input errors



Guide
Guide/rulebook question Y input and display



Guide/rulebook question N input and display

Guide/rulebook question N input and display

Guide/rulebook input error



Quiz
Question/answers display, answer correct



Question/answers display, answer wrong

Question/answers display, answer wrong

Question/answers display, hint input

Question/answers display, hint input

Question/answers display, input error



More knowledge
Know more display, 'Y' input



Know more display, 'N' input



Know more display input error



Quiz end messages
Quiz over message and score

Quiz over message and score

Score colour and message change

Score colour and message change

Leaderboard update message and display
Updating leaderboard



Leaderboard display

Leaderboard display

Quiz replay
Quiz replay 'N' input, outro quote



Quiz replay error input



Quiz replay 'Y', username question 'Y' input



Quiz replay 'Y', username question 'N' input



Quiz replay 'Y', username question error input



Secret username
The secret username is a throwback to a very popular Sci-Fi movie, '2001: A Space Odyssey. In the movie, the AI by the name HAL 9000 is the main antagonist. The secret username is first hinted in the guide/rulebook = '3 LETTERS = ASCII'. At first this means nothing, but as the user finishes the quiz the leaderboard is presented. The rules clearly say there are maximum of 100 points but somehow there is an user by the name 'HAL_9000' with a score of 105 points (present at the time of writing this README). That should give the user incentive to see the rules and replay the quiz again to see what is going on. Upon rechecking the clue '3 LETTERS = ASCII', the user should assume the need to change only the letters of 'HAL_9000' into ASCII code and input that as the username. As there are checks in place for name input against using special characters, meaning '_', the user should not consider '_9000' for input. As ASCII code can be triple or double digits, both 'secret' usernames are allowed:

=====SPOILER=====
If the user enters the secret username, special message prints with change of score calculation. Also, if the user scores more than 100 points, which is possible only using secret username, a special message will display at the end of the quiz.
Secret username input result
=====SPOILER=====
Secret username score message
=====SPOILER=====
Front-end features
Favicon and dynamic background/GIF

Favicon and dynamic background/GIF

GitHub and Youtube icon, 'Run Program' button hover colour change

GitHub and Youtube icon, 'Run Program' button hover colour change

GitHub icon opening page in new tab



Youtube icon opening page in new tab



Future Implementations
The author would like to implement random question order and add a lot more questions/answers/more knowledge. Also, give the user option to use various 'game modes' like easy, medium and hard and corresponding questions. Implement timer that the user can turn on/off for added challenge and more score points.

Back to top ⇧

Technologies Used
Languages Used
HTML - The website content was adjusted using HTML language.
CSS - The webpage was styled using custom CSS internally using 'style' in the head of layout.html.
PYTHON - The project logic and operations inside CLI were developed using Python language.
Programs Used
GitHub - Source code hosted on GitHub, deployed using Git Pages.
GitPod - Used to commit, comment and push code during the development process.
Font Awesome - GitHub icon was obtained from Font Awesome.
Balsamiq - Used to create wireframes and website structure map for the project.
Visual Studio Code + Spell Checker add on - Used to spell-check the html and css code
Google Keep - Used to make notes during the project duration
LanguageTool - Used to spell-check the contents of README.md
Google Fonts - Used to import fonts to the project
GifCap - used to capture gif-s of the project
Heroku - used to deploy the project
XConvert - used to compress GIF file
Imgur - used to host the background image and favicon
Patorjk - used to convert text into ASCII art
Google worksheet - used to host the worksheet to hold data
Lucidchart - used to make the flowchart for the project
[Back to top ⇧](#daily-sales)

Deployment
The project was written and hosted on GitHub. The author used GitHub's terminal output with command 'python3 run.py' to run the program logic/game. After the project was developed enough, it was deployed on Heroku using the following method:

Add dependencies in GitPod to requirements.txt file with command "pip3 freeze > requirements.txt"
Commit and push to GitHub
Go to the Heroku Dashboard
Click "Create new app"
Name app and select location
Add Config Vars for Creds and Port in Settings tab
Add the buildbacks to Python and NodeJS in that order
Select appropriate deployment method, GitHub
Connect to Github and link to repository
Enable automatic deployment and/or deploy manually
Click on Deploy
[Back to top ⇧](#daily-sales)

Testing
Testing information can be found in a separate testing file TESTING.md.

[Back to top ⇧](#daily-sales)

Credits
Code used and adapted
The author used his previous projects, Boudoir Studio ( GithHub repository here ), and Budget Calculator ( GithHub repository here ) as a source for looking up the code for CSS and README purposes mainly.
Code Institute template was used to start the project.
Using Google worksheet to manipulate questions and answers was seen during Code Institute Love Sandwiches project, ( GithHub repository here ).
Pub Quiz Challenge ( GithHub repository here ) was studied in depth to get a sense of how a quiz game in Python would work, and to get a sense of the quiz layout itself. It has also provided the solution for pairing the questions with the right answers.
Football Quiz ( GithHub repository here ) was taken note of because the CLI was centered and the image background was applied. This is also where the author learned about tabular display of the leaderboard.
Wheel of Fortune ( GithHub repository here ) was studied and this is where the author noticed and learned about clearing the screen in CLI.
Harry Potter Adventure Game ( GithHub repository here ) was studied to fix the background issue in HTML, more on this in BUGS section in TESTING.md.
Carl Sagan quotes webpage was used to copy Mr. Sagan's quotes for intro/outro.
Space Trivia Questions was where the author copied the questions, answers and 'more knowledge' info from.
Websites visited to gather knowledge
There were many sites visited during the duration of the project. Google was used to produce results of the specific query, and Stack Overflow proved to be the best source of information for various queries/issues.

The standout webpages are:

This website was used to learn about sorting a string.
This website was used to learn about tabulating the leaderboard.
This website was used to learn about sleep.
This website was used to learn about typing print, input and clear screen.
This website was used to learn about restarting the program.
This website was used to learn about printing on a same line.
Acknowledgments
This whole project is dedicated to Carl Sagan, astronomer, planetary scientist, cosmologist, astrophysicist, astrobiologist, author, and science communicator. His book 'Cosmos' inspired me as a child and geared me towards sciences and astronomy.

Without support I got from other people, this project would never be realized. I'll try and remember to thank everyone and everything I can!

Mirjana, my wife, thank you for your support and cheering me on, lifting me back up when it got hard. Thank you for taking care of all the housework and food, children and numerous other responsibilities while I was busy with full time job and doing this project on the side. Without you this journey into career change would never be possible.
A., G. and V., my three beautiful girls. Thank you for being so understanding during the project work. Thank you from the bottom of my heart for being who you are, wonderful and delightful souls. You make me proud to be your dad.
Boris, my brother, thank you for testing my project so thoroughly, and for your support.
Marija and Boris, my mother and father, thank you for making me feel like a superstar when I announced I'm starting this journey.
John, my friend, thank you for starting me on this path, and for your support, chats and sharing the things you learned.
Helen from Code Institute, thank you believing in me and making this change possible.
Slack community, thank you for being a constant source of good information. Special mentions are Sirinya_5P, Kate L_5P and Tomislav_5P, whose praise lifted my spirits and reinforced the notion that I can do this.
Koko, my mentor, thank you for being an incredible source of solutions and good advice, your support meant a great deal during the project.
C8H10N4O2 in a cup. Thank you for existing.
[Back to top ⇧](#daily-sales)