---
- title: Derivatives Quiz
- toc: true
- categories: [applab]
---

# Derivatives Quiz: Process

## Link to Project

[Project](https://studio.code.org/projects/applab/Yxq8JLTMe0XcOJuawEgNTwECRPO-t3F6VNlTiwCPq98)

## Design

The base concept was testing something I am currently working on in math that I need to memorize, that being the derivative of inverse trigonometric functions.

#### Components

- 6 questions
- 2 hidden elements
- If functions and variables
- Lose screen, winning screen, hidden page, and the beginning page
- Images for mathematical answers
- Basic, eye pleasing graphics

![]({{ site.baseurl }}/images/in_code_variable_use_hidden_function.png "The way the the hidden element is implement per function, hidden after as to prevent repeated use")
![]({{ site.baseurl }}/images/output_hidden_element_variables_app_lab.png "The way in which one of my hidden elements is outputted, only working at the very end and you are not informed if you failed to find it")
![]({{ site.baseurl }}/images/modern_art_function.png "The function to create the canvas art, as I did not wish it clog up the code below, could be changed to fit other canvases if so desired. Doing this makes it so I do not have to copy and paste 10 lines of code every time I wished to create canvas art, however I only wanted to do it once this time.")

#### Choices

- Background colors were chosen to be mute so they did not distract from content, also chosen to be colors I like
- Chose the first hidden function as a leftover from testing the different elements in the tool box, deciding to not delete one of my tests
- Second hidden function was a way for me to try out canvas mode, and a fun way to not only be focused on calculus, spread through the quiz
  - Also a method to experiment with if functions and variables
- Canvas drawing was after seeing what it could do, and deciding to go out of bounds from what is normally done

#### Individual Question Design

![]({{ site.baseurl }}/images/individual_question_design.png "Code showing the first question in the quiz, and how each one looks basically")

Made to be as simple as possible, easily automated if not using block coding. Each correct answer and wrong answer are written in the same format, with the page name being written afterwards so they would not be mixed up between each other. If clicking the wrong answer you are taken to the "losing_page" where you are stuck forever, or have to restart the program (by design). If the right answer is clicked it takes you to the next page, which can also be automated if not block coding. The last code block is part of the hidden function, which is included in each question page, and you have to click every single one to get an end result.

## Successes

- Using variables and if functions
- Using images as answers
- Implementing hidden components
- Creating quiz properly with score

## Discoveries

I discovered the canvas and how coordinates worked using it, as well as several ways to use functions

## Challenges

My main challenge was in attempting to automate the question format. However, after trying it the code screen broke (I am not sure if it was because of my computer or odd code) with no true error, even messing with the block format, I decided to go with the other route since we are not using this format again, and there was not much code to repeat, however I did learn a method in the future to implement this type situation, as I felt I was on the right path if the coding interface had not broken. My other minor challenges were in making sure each thing was named correctly so it was easy to find, and making sure everything was in a proper place that could be found if I went back to change code.

## Different Concept

I did not have the time to implement this, however making a mini game wherein it is a choose your own adventure would be plausible, maybe making a timeline using the canvas function. with the use of variables and "onEvent" many things can be created, as well as there conveniently being different screens.
