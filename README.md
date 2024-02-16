# Ticker

![Ticker Logo](trades/static/documentation/ticker-readme-hero.webp)

## Table of Contents

* [Introduction](#introduction)
* [Features](#features)
* [Design](#design)
* [User Stories](#user-stories)
* [Bugs](#bugs)
* [Manual Testing](#manual-testing)
* [Deployment](#deployment)
* [Technologies Used](#technologies-used)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)
<br>
<br>
<br>

<!-- Introduction Section is below, with a 'Back to Top' anchor link, the link will be shown at the bottom of every section -->
## Introduction

Ticker is the 4th project deliverable as part of the Code Institute Diploma in Full Stack Software Development.
<br><br>
It is a lightweight stock trading companion application that is designed to assist stock traders track their activity over time and provide a central repository for all trades across multiple brokers. The application has been built using the Django python framework for the primary functionality, it uses ElephantSQL for database storage, HTML5 for the site structure and the Bootstrap framework for CSS and Javascript components. The overall design followed user centric design principles and the mobile first design philosophy, it also focused on providing user friendly CRUD operations across the site. It should be noted that the project has been deployed as a minimum viable product, additional functionality and enhancements will be included in future updates.
<br><br>
Ticker is aimed at novice, beginner or hobbyist stock traders that require a central repository to keep track of their trades that have been placed across different brokerages, with the goal of providing this audience with a helpful, lightweight and easy to use solution that will retain their information in a persistent location and provide them with insights into their activity over time. 
<br><br>
The deployed site can be found [here](https://ticker-aefd70a6f705.herokuapp.com/).

[Back to Top](#ticker)
<br>
<br>
<br>



<!-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- FEATURES SECTION -->
## Features 

An overview of the key features that have been implemented for this project is shown below, along with several features that will be implemented in future updates.
<br>
<details>
  <summary> <b>Existing Features</b> </summary>
<!-- Feature 1 begins -->
<br>
<table>
<tr><th> <b> Customised Logo</b></th></tr>
<tr>
<td>
<br>
A custom logo has been designed for Ticker, the logo is simple and clear. It also includes a green 'candlestick' symbol that will be instantly recognisable to the target audience and aims communicate the intended use of the application.
<br>
</td>
</tr>
<tr><td Colspan="2">

![Ticker logo](trades/static/documentation/ticker-readme-hero.webp)

</td></tr>
</table>
<!-- Feature 1 ends -->
<br>
<table>
<tr><th> <b>User Log In and Registration</b> </th></tr>
<tr><td>
<br>
The application offers user registration and log in functionality using Django's allauth package.
<br>
</td></tr>
<tr><td Colspan="2">

![Tracker Panel](trades/static/documentation/features_01_registration(a).JPG)

</td></tr>

<tr><td>
<br>
A notification is also disaplyed to the user alerting them to their log in status.
<br>
</td></tr>
<tr><td Colspan="2">

![Tracker Panel](trades/static/documentation/features_01_registration(b).JPG)

</td></tr>
</table>
<!-- spacer -->
<br>
<table>
<tr><th> <b>Question Container</b> </th></tr>
<tr><td>
The question container takes up a prominent space on the screen and clearly displays the text to the user, the high contrast allows for easy readibility and accessibilty.
</td></tr>
<tr><td Colspan="2">

![Question Container](assets/documentation/features03_question_container.webp)

</td></tr>
</table>
<!-- spacer -->
<br>
<table>
<tr><th> <b>Choice Container</b> </th></tr>
<tr><td>
The choices can be selected from easy to use containers utilising radio inputs.
</td></tr>
<tr><td Colspan="2">

![Choice Container](assets/documentation/features04_choice_containers.webp)

</td></tr>
</table>
<!-- spacer -->
<br>
<table>
<tr><th> <b>Main Button</b> </th></tr>
<tr><td>
The user interaction with the quiz is enabled through a simple button that has contextual commands associated with it depending on what screen is currently displayed. The focus is on making the quiz easy to use and accessible.
</td></tr>
<tr><td Colspan="2">

![Main Button](assets/documentation/features05_main_button.webp)

</td></tr>
</table>  
<!-- spacer -->
<br>
<table>
<tr><th Colspan="2"> <b>VAR Assist</b> </th></tr>
<tr><td Colspan="2">
The VAR Assist feature will allow the user to remove two incorrect choices from the screen. When activated, a function will be invoked that replaces the inner HTML of the incorrect choices with 'Offside!', the radio inputs will also be disabled for these choices. The user will be granted 3 VAR Assists at the start of the quiz, and can use 1 per question until they run out.
</td></tr>
<tr><td> <i>Before Use</i> </td><td> <i>After Use</i> </td></tr>

<tr>
<td>

![Before Use](assets/documentation/features07_var_assist_1.webp)

</td>
<td>

![After Use](assets/documentation/features07_var_assist_2.webp)

</td>
</tr>
</table>  
<!-- spacer -->
<br>
<table>
<tr><th> <b>Goals Scored</b> </th></tr>
<tr><td>
A tracker will be visible on the bottom right hand corner of the screen during the quiz that will display the 'Goals Scored' by the user.
</td></tr>
<tr><td Colspan="2">

![Goals Scored](assets/documentation/features08_goals_scored.webp)  

</td></tr>
</table>  
<!-- spacer -->
<br>
<table>
<tr><th> <b>On Hover Changes</b> </th></tr>
<tr><td>
Any items on the screen that the user can interact with will display a subtle colour change on the box shadow when hovered over to convey that the item can be interacted with by tapping or clicking on it.
</td></tr>
<tr><td Colspan="2">

![On Hover](assets/documentation/features09_hover_change.webp)

</td></tr>
</table>
<!-- spacer -->
<br>
<table>
<tr><th Colspan="2"> <b>Answer Feedback</b> </th></tr>
<tr><td Colspan="2">
The Answer Feedback feature provides the user with instant feedback after submitting their answers. An image depicting players in various stages of celebration or desolation are displayed to the user along with a 'MISS!' or 'GOAL!' text caption. 
</td></tr>
<tr><td> <i>Miss!</i> </td><td> <i>Goal!</i> </td></tr>

<tr>
<td>

![Before Use](assets/documentation/features10_answer_feedback_1.webp)

</td>
<td>

![After Use](assets/documentation/features10_answer_feedback_2.webp)

</td>
</tr>
</table>  
<!-- spacer -->
<br>
<table>
<tr><th> <b>No Option Selected Alert</b> </th></tr>
<tr><td>
The No Option Selected Alert feature provides the user with prominent and immediate feedback if they attempt to answer a question without selecting a choice first. This alert will stay on screen for the duration of the current question being asked, and will be removed automatically for the next question.
</td></tr>
<tr><td>

![Official Font](assets/documentation/features11_no_option_alert.webp)

</td></tr>
</table>  
<!-- spacer -->


[Back to Features](#features)
<br>
<br>
<br>
</details>
<!-- The Existing Features section ends here -->
<!-- The Future Features section is shown below, this will be disaplyed in a collapsible format, with each item shown in tabular form -->
<details>
  <summary> <b>Future Features</b></summary>
<br>
<!-- Future Feature 1 begins -->
<table>
<tr><th><b>Substitution</b></th></tr>
<tr><td>
This feature will allow the user to swap out the question and choice set displayed on screen for another set, this may provide them with a question that they may be able to answer instead. This would possibly involve adding a new 'Substitutes' property to the quizEngine object that would contain the alternative questions and choices values, a function would then change the inner HTML of the containers accordingly once called.
</td></tr>
</table>
<!-- Future Feature 1 ends -->
<br>
<table>
<tr><th><b>Match Timer</b></th></tr>
<tr><td>
This feature will add a timer to the quiz with a time limit of perhaps 11 minutes, with subtle on screen hints at different checkpoints (e.g "half-time approaching", "approaching the final minute", "we're in injury time"). This would run 'asynchronously' and when it reaches 'full-time', the quiz would end regardless of the user's progression.
</td></tr>
</table>
<!-- spacer -->
<br>
<table>
<tr><th><b>Home or Away Kit Toggle</b></th></tr>
<tr><td>
This will toggle the colour scheme of the quiz to dark or light modes which will enhance the user experience and aid accessibility.
</td></tr>
</table>
<br>
<!-- spacer -->
<table>
<tr><th><b>Bonus Facts</b></th></tr>
<tr><td>
Initially I wanted to include bonus facts containing bite size pieces of information about the tournament and women's football in general, these would have been displayed in the container along with the 'GOAL!' or 'MISS!' feedback. It will be added in a future update instead.
</td></tr>
</table>
<!-- spacer -->
<br>
<table>
<tr><th><b>Hall of Fame</b></th></tr>
<tr><td>
This feature will create a leaderboard to store user scores, adding a competitive dimension to the quiz and perhaps promote sharing, replayibilty and increase enjoyment.
</td></tr>
</table>
<!-- spacer -->
<br>
<table>
<tr><th><b>Custom Radio Inputs</b></th></tr>
<tr><td>
The project has been deployed with standard/default radio inputs, however these will have customised styling in a future update.
</td></tr>
</table>

[Back to Features](#features)
<br>
<br>
<br>
</details>
<!-- Future Features ends here -->

</details>

[Back to Top](#fifa-2023-womens-world-cup-quiz)
<br>
<br>
<br>
<!-- Features ends here -->