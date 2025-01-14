# Introduction 

FitnessTracker is a command-line Python application designed to help users track their fitness exercises and store data in Google Sheets. This allows users to monitor their progress over time effectively.

The application is ideal for individuals who want to record their weekly fitness journey, including:

- The exercises performed
- The number of repetitions per set
- The weight used

By providing a clear record of these details, FitnessTracker encourages the progressive overload technique, helping users steadily increase their performance and achieve their fitness goals.trong they have gotten from the weight and total reps they have done for each exercise. 

## Flowchart

![Flow chart](assets/flow-chart.png)

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
