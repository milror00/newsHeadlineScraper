# newsHeadlineScraper
Tesco Store Location Scrapper
This is a demo project that uses python - request and behave to scrape headlines from published news sites.

This is a demo to demonstrate the skills I have for scraping. This code is not to be used for any reason commercial or personally other than to demonstrate the approach to scraping.

Requirements to run :

Python 3.7 above

behave==1.2.6

requests==2.23.0

lxml==4.5.0

idna==2.9

urlib3==1.25.9

Steps for installation:

Clone git repo

I use PyCharm Professional to I import the project which creates a virtual environment for the project

Install libraries : pip install behave pip install requests pip install lxml

Open the console at the root of project and run the command :  behave ./features

if you are going to use MYSql then run behave ./features -D user=username -D pass = password

MySQL DDL 

create table headlines

(

	id int auto_increment
  
		primary key,
    
	newspaper varchar(200) not null,
  
	headline varchar(200) not null,
  
	imageurl varchar(200) not null,
  
	headlinedate datetime not null
  
);


#Feature

Feature: To capture the TOP headline and image.

  Scenario: Get the headline for a given newspaper

    Given I am I have a list of newspaper urls
    
      |url                         |newspaper    |
      
      |https://foxnews.com         |foxnews      |
      

    And I capture the top headline for each newspaper
    
    Then for each headline I can write it out to stdout
    
  Output:
  
  Show-Me State files landmark suit against Chinese government for coronavirus 'deceit'
  
//a57.foxnews.com/hp.foxnews.com/images/2020/04/1280/533/a61bcb78b52f718e709b9a3f43ea43a1.jpg?tl=1&ve=1

Process finished with exit code 0
  
