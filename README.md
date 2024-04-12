# Welcome to Show Library

## Backend Development Milestone3 Project by Houssem Aoun

A show library or archive is a specialized website in preserving cinematic heritage. These archives tirelessly collect, restore, and maintain various types of films, including:

Feature Films: These are the full-length movies we enjoy in theaters or at home.
Documentaries: Films that provide factual information or explore real-life events.
Short Films: Compact cinematic works that convey powerful messages in a limited duration.
Experimental Works: Creative and unconventional films that push the boundaries of storytelling.

<img src= static/images/responsive-ms3.jpg>

### User Experience (UX) ###

* As a customer, I want to be able to search for shows by category or keyword, so I can easily find the show I am interested in.

* As a customer, I want to be able to add shows to the databse, view the contents of other users.

* As a customer, I want to be able to create an account.

* As a store owner, I want to be able to manage my show inventory, update film details.

* As an Admin user the navigation bar is displayed with a logo on all pages for easy navigation, with a burger menu on mobile devices.

* As an Admin user I can add, delete and edit categories and films.

 ### User Stories
  - #### VIEWING & NAVIGATION
      | User Story Id 	| As a    	| I want to be able to...         	| So that I can...                                                                     	|
      |---------------	|---------	|---------------------------------	|--------------------------------------------------------------------------------------	|
      | 1             	| Shopper 	| Easily navigate the site        	| Find shows and information that I require                                         	|
      | 2             	| Shopper 	| View shows by category       	    | Find specific show I am interested in without having to scroll through all shows 	    |
      | 3             	| Shopper 	| View details of each show     	| Learn more about each show                                                        	|
     

    - #### REGISTRATION & USER ACCOUNTS
        | User Story ID 	| As a    	| I want to be able to ...                    	| So that I can...                                        	|
        |---------------	|---------	|---------------------------------------------	|---------------------------------------------------------	|
        | 1             	| Shopper 	| Register an account                         	| Have an account with the site and view my profile       	|
        | 2             	| Shopper 	| Log in and out                              	| Keep my account information secure                      	|
        | 3             	| Shopper 	| View a profile page                         	| Set a default delivery address and view previous orders 	|
        | 4             	| Shopper 	| Reset my password                           	| Recover my account                                      	|

    - #### SORTING AND SEARCHING
        | User Story ID 	| As a    	| I want to be able to...                     	| So that I can...                             	|
        |---------------	|---------	|---------------------------------------------	|----------------------------------------------	|
        | 1             	| Shopper 	| Search for a show by name or description 	    | Find a specific product I'd like to purchase 	|
        | 2             	| Shopper	| Add a product           	                    | Add new show to the archive                  	|
    - #### CONTACT
      | User Story ID 	| As a              	| I want to be able to... 	| So that I can...                         	|
      |---------------	|-------------------	|-------------------------	|------------------------------------------	|
      | 1             	| Shopper 	            | Contact the admin team   	| Ask questions about the e-shop            |
    
    - #### ADMIN & STORE MANAGEMENT
      | User Story ID 	| As a              	| I want to be able to... 	| So that I can...                         	|
      |---------------	|-------------------	|-------------------------	|------------------------------------------	|
      | 1             	| Store Owner/Admin 	| Add a show           	    | Add new show to the archive               	|
      | 2             	| Store Owner/Admin 	| Edit a show             	| Update show details                   	|
      | 3             	| Store Owner/Admin 	| Delete a show           	| Remove show    	|
      | 4             	| Store Owner/Admin 	| Delete a show review      | Remove show reviews that might have been entered incorrectly 	|


## Features
There are universal features that are present throughout The Show Library website. These feature are:
- Responsive on all device sizes - from 320px upwards to larger desktops reaching 1200px and more.
- Fully-responsive nav bar (including mobile nav bar)
- Mobile-friendly, adusting automatically at specific breakpoints.
- The Show Library logo/name is seen at all times whether tucked to the left, central on reduced screen-sizes or at the top of the mobile menu on smaller and mobile devices. This is vital for brand consistency and serves as a simple way of reminding the user of the website's name. 
- Clear and obvious navbar links to other pages within the website.
- A Flash box appears at the top of the webpage whenever a user or admin completes a task - by either adding, editing or deleting. 


### Potential Features To Include

- Create a web application that allows users to upload thier favorite screenshots of thier favorite film.
- Building a strong cohesive archive of references music/literature/art/film/photography/zines.
- Create a web application that allows users to have their own profile area.

## UX AIMS

- Users should easily find their way around the website.
- Clear and intuitive navigation menus, categorized sections, and a user-friendly layout.
- Ensure the website is accessible and functional across various devices and screen sizes.
- Present filmss in an engaging manner to capture user attention.
- Enable users to share their opinions and experiences.


## DATA BASE

**Database**

[MONGODB](https://www.mongodb.com/cloud/atlas/register)

MongoDB is a source-available, cross-platform, document-oriented database program. Classified as a NoSQL database product, MongoDB utilizes JSON-like documents with optional schemas.

To create a MongoDB cluster, you need to:
1. Log in to your MongoDB Atlas account at https://cloud.mongodb.com
2. Click on the “Create” button.
3. Choose your cluster type (dedicated, serverless, shared).
4. Choose your cloud provider and region.
5. Click on “Create cluster”.
Alternatively, you can create a MongoDB database cluster at any time from the Create menu by selecting Databases3.

## TESTING

**HTML AND CSS VALIDATOR**

[W3C](https://validator.w3.org/)

**LIGHTHOUSE**

<img src= static/images/lighthouse-ms3.jpg>


## DEPLOYMENT

### Github

This project is deployed using GitHub pages using the following process:

**Deploying a GitHub Repository via GitHub Pages**

1. In your Repository section, select the Repository you wish to deploy.
2. In the top horizontal Menu, locate and click the Settings link.
3. Inside the Setting page, around halfway down locate the GitHub Pages Section.
4. Under Source, select the None tab and change it to Master and click Save.
5. Finally once the page resets scroll back down to the GitHub Pages Section to see the following message *"Your site is ready to be published at (Link to the GitHub Page Web Address)"*. It can take time for the link to open your project initially, so please don't be worried if it down not load immediately.

**Forking the Github Repository**

You can fork a GitHub Repository to make a copy of the original repository to view or make changes without it affecting the original repository.

- Find the GitHub repository.
- At the top of the page to the right, under your account, click the Fork button.
- You will now have a copy of the repository in your GitHub account.
  
**Making a Local Clone**

1. Find the GitHub Repository.
2. Click the Code button
3. Copy the link shown.
4. In Gitpod, change the directory to the location you would like the cloned directory to be located.
5. Type git clone, and paste the link you copied in step
6. Press Enter to have the local clone created.

[Web link once deployed](https://ms3-re-6da2c447beba.herokuapp.com)


**Heroku process**

Now that you have your database and code in your IDE configured, we will add it to a Heroku app using a new environment variable (Config Var) called DATABASE_URL. Then our Heroku app will be able to connect to the external database.

1. Log into Heroku.com and click “New” and then “Create a new app”
2. Choose a unique name for your app, select the region closest to you and click “Create app”
3. Go to the Settings tab of your new app
4. Click Reveal Config Vars
5. Return to your ElephantSQL tab and copy your database URL
6. Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add”
7. Add each of your other environment variables except DEVELOPMENT and DB_URL from the env.py file as a Config Var. 
**Deploy the app**

1. Navigate to the “Deploy” tab of your app
2. In the Deployment method section, select “Connect to GitHub”
3. Search for your repo and click Connect
4. Optional: You can click Enable Automatic Deploys in case you make any further changes to the project. This will trigger any time code is pushed to your GitHub repository.
5. As we already have all our changes pushed to GitHub, we will use the Manual deploy section and click Deploy Branch. This will start the build process.
6. Now, we have our project in place, and we have an empty database ready for use. As you may remember from our local development, we still need to add our tables to our database. To do this, we can click the “More” button and select “Run console”.
7. Type python3 into the console and click Run
8. This opens the Python terminal, in the same way as it would if we typed python3 into the terminal within our IDE. Let’s now create the tables with the commands we used before.
9. Exit the Python terminal, by typing exit() and hitting enter, and close the console. Our Heroku database should now have the tables and columns created from our models.py file.


## CREDITS

All the code that I have used to create this website was taken from Code Institute learning platform and from the next following sources:

[MATERIALIZE](https://materializecss.com/)

- I used *Materialize 1.0.0* version, mainly I used the gryd system to build layouts, navigation bar, footer.

[W3SCHOOL](https://www.w3schools.com/)

- I wanted to create a shadow background for the text and images: box-shadow and text-shadow.

[stackoverflow](https://stackoverflow.com/)

- is a public platform where i can find and contribute answers to technical challenges.
  
[codeinstitute](https://codeinstitute.net/) 

- Non-Relational Database Management Systems.