# Free Flow

[Responsive Image]()

Free Flow is a freelance project tracker web app centered towards freelance business people who want to track projects and their respective tasks. 
Free Flow is a web app or online tool to track a projects progress with the ability to calculate estimated or final time taken and cost. Free Flow aims to help anyone undertaking a new project, or even estimate a projects cost and time to complete before starting. The app also looks to solve the problem of understanding project scope in terns of cost and time, and provide a useful tool for any business person who may undertake a project of multiple kinds. 
For example a builder could use Free Flow to estimate and track the progress of a building project, a graphic designer may use it to estimate a business branding project or a web developer to calculate the costs of a website project.
In essence Free Flow serves as a way to track multiple projects of any kind by breaking the project into tasks.

[Live App Link]()

[Repo Link]()

## Contents

Contents Here

## User Experience

### First time visitor goals

- First time visitors of the Free Flow app are expected to be anyone looking to undertake or understand a new project. With this in mind the first time visitor goals are to provide clear information of the apps features and showcase the apps versatility with project examples on the landing page with an effort to attract new users to sign up to the app.
- First time users who have signed up and logged in should be impressed with the design elements and intuitive nature of the app. They should be able to make a new project and add tasks quickly and easily from the very first visit with little to no instructions needed. With this in mind the app looks to first time users and convert to a returning or full user by creating a familiar to navigate interface.

### Returning visitor goals

- Returning visitors to Free Flow were likely impressed with their initial logged in interaction and are looking to track a project in some way. Therefore the returning visitor goals are to create an intuitive and versatile app where users can easily create projects and tasks, as well as quickly track their progress.
- Further returning visitor goals are to provide a way to generate a project report of time and cost for analysis or invoicing. This is though the use of custom tasks and reports. With custom tasks a returning user can use single tasks across multiple projects and analyse the time taken to complete a task. Reports would show a breakdown of a projects estimated time taken and cost, as well as the actual time taken and costs. 

### App use goals

- The apps main goal is to provide a versatile and easy to use project management system, through a familiar feeling interface and quickly viewable project information.
- The app should give freelancers and project managers a way to track a projects progress, understand scope and generate a project report or invoice.
- The app should be accessible for a wide range of users, taking full accessibility measures into account for an inclusive approach.

## Design

### Concept and Epics

My inspiration for the concept of the Free Flow app came from the friends or family members who have asked if I could make a website for their business in the future. With this in mind I researched how freelance business people may operate and the challenges they face when undertaking a new project. When researching into technology based freelancers I found there were often many steps to a project that could be broken down into tasks. 

In order to understand the scope of a project I wanted to add an estimated and final time to a tasks. This meant a user could then see the difference in estimated vs actual time to complete a project and provide a more accurate estimate in future projects. It would also allow a user to see which parts of a project took the most time and better understand how to prioritise tasks. The inspiration for assigning a task a time came from my background as a BMW Vehicle Technician and VW Group Warranty Technician, where jobs or tasks are assigned a set time for billing purposes. 
As a basic example a full service may be broken down as shown below.
- Oil and filter change - 20 mins
- Fuel filter change - 15 mins
- Air filter change - 5 mins
- Cabin filter change - 10 mins
- Inspection time - 20 mins
- Total - 1 hour 10 mins

With the ability to add estimated and actual times to tasks all that was needed to provide an hourly cost estimate was a project assigned hourly rate. By adding an hourly rate to a project a user could calculate the cost of a project using the rate and times. Although many freelance business people quote a project cost, there are many instances where an hourly rate is used. With this in mind, I broadened my initial target audience to include another type of freelancer, those paid hourly.

As I wanted to include a hourly rate to the project and calculate costs, I also wanted to generate a report of the project for invoicing or analysis. This would be a way to easily see a full estimated project breakdown and even a completed projects full task and hourly breakdown.

As I have used project tracking apps without a costs feature before, I knew the kind of app I wanted to create but with the added costing feature. This meant I did not have to spend a great deal of time researching design ideas as I had a good idea of how I wanted the app to look, feel and navigate. In order to work with the time frame in mind, I wanted to use Bootstrap for layout, navigation and some interactive features. With using Bootstrap over multiple previous projects I felt I have a reasonable understanding of its uses and opted to use the classic web version of Bootstrap over the React Bootstrap component version. This would save me some time as I already knew how to implement features I have used before and achieve the same results.

### Database
When designing the Free Flow app I wanted to create a database schema that left room for stretch goals but also creating a solid schema was imperative. With this in mind, I spent a reasonable amount of time to ensure my database schema would not need any corrections once I began to code, as this could take up unnecessary time required to complete rhe project in time. I used an example of my previous project database schema and [Excalidraw]() to create my schema and double check it before beginning to code. I also used my wireframe designs of each page to understand the fields that would be required in each database model. Visualising forms and pages helped to write down the required fields of each model and make sure nothing was missing or overlooked.

After designing and checking my database schema I only needed 3 custom models or 4 total, including the user model. The 3 custom models being project, task and custom task. These models would allow plenty of functionality in the app while keeping to the scope of both an MVP and the project time scale. I had considered adding more fields to each model as well as other models I could incorporate, but in trying to keep to the scope of the project they seemed unnecessary or simply too ambitious for this project, although I would like to add further features in the future. Some of the future features can be found further below.

The core of the schema is the user. I will be using the Django Rest Framework that has user authentication and therefore a user model automatically generated when using Django auth. In contrast to my previous projects, I want to make the users first and last name as well as username required, as I may use it when generating reports. This will provide a more professional look for invoicing or reports.

The user can create a project that will contain a title, brief, hourly rate and completion date. I wanted the app to have a reasonable amount of features without being overloaded with things that are unnecessary or not generally used and therefore wanted to keep the model fields as simple as possible, while still being able to provide the required features. I considered adding things such as a client name or contact details, but this type of information can be contained in the brief and allows for more versatility while keeping to a relatively simple model.

Tasks are added to a project and contain fields for a title, description, completion date, estimated time, time taken, custom task link and status. This model allows enough features to track tasks within a project, estimate the amount of time a project will take and how much time it has actually taken. This combined with the projects hourly rate also allows for calculating project and task costs.

The custom tasks model contains fields for a title, description, predicted time, number of uses, and average, quickest and longest time taken. These fields contain enough scope to track when a custom task has been used in a project as well as time based data when a task is complete, meaning the user can view and analyse custom task data.

### Functionality

### Wireframes

### Colour scheme

### Typography

## Agile and kanban

When it came to beginning the project after conceptualisation I wanted to use an agile development methodology to stay flexible throughout the process, while keeping a core feature set to maintain focus. This meant I was able to quickly change things such as design or user experience features to create a better overall experience. I started by creating 2 project boards inside the Github repo. One for user stories and epics and another for the project development to ensure all features are considered and allow me to effectively plan the development process through the use of story points. I found that creating 2 separate project boards helped me to understand the scope of the project and plan my time effectively.

### User stories and epics

### Issues

## Features

### Existing features

#### Favicon

#### Nav bar

#### Landing page

#### Authentication pages

#### Home page / Projects list

#### Create project form

#### Edit project form

#### Project details page

#### Create task form

#### Edit task form

#### Task details

#### Custom tasks page

#### Create custom task form

#### Edit custom task form

#### Custom task details

#### 404 & 500 pages

### Defensive programming

### Future features

## Testing

## Deployment

## Credits

### Django email field

I wanted to add an email field to the profile model when starting the project. After some light research I found Django has a built in email field that conducts basic email validation checks such as an '@' and a '.' after. [Email field documentation](https://www.geeksforgeeks.org/emailfield-django-models/)

### Django decimal field

As I wanted to add an hourly rate and an amount of time in hours, I needed to add a field to my models that contain numbers. I used the decimal field as it also has the use of a max digits and decimal places, which was perfect for an hourly rate and amount of time. [Decimal field documentation](https://www.geeksforgeeks.org/decimalfield-django-models/)