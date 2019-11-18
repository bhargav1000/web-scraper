# Python based Web Scrapers

BeautifulSoup based web scrapers written in Python.
These scrapers were used to scrape examination results from the Visvesvaraya Technological University(VTU) [website](http://vtu.ac.in). Script Versions have been made for both CBCS and Non-CBCS category students given that the Result Page URLs are different for either of the categories. The user has to enter a limited set of details to collect the exam results specific to the college department.  

## Requirements:
- BeautifulSoup 4.8.1

## Scripts:
1. ```usnresult.py```: This script was the first script written to scrape the grade point or SGPA for a student based on the University Seat Number(USN).

2. ```scraper.py```: This is a GUI based script which provides input fields for users to enter the USN and semester for a student and displays the result of the student. 

3. ```nayacbcs.py```: An automated scraper which collects details such as Area Code, College Code, Branch and Semester to provide the exam results for **all students in a given semester**. The extracted results are stored in a CSV file. 

4. ```nayadip_cbcs.py```: Same script as above but it is modified for diploma students.

5. ```noncbcs.py```: An automated scraper similar to ```nayacbcs.py``` for Non-CBCS students.

You can pick a script depending on the task and type ```python <script_name>``` in the command line.


## Impact of this project:
- This project saved several hours for the faculty at my college in the result aggregation process. Earlier, professors would collect results for each student one at a time and this would take upto 16 hours to collect a single department's results. This project saved more than 40 hours in result aggregation. 

- It also helped analyze the results to identify at risk/poor performing students and academic help was provided to these students.

- This project scraped results for more than 3000 students in less than an hour's time.

