import urllib
import urllib.request
from bs4 import BeautifulSoup

usn = input("Enter usn: ")
results_page = 'http://result.vtu.ac.in/cbcs_results2017.aspx?usn=' + usn + '&sem=3'
page = urllib.request.urlopen(results_page)



soup = BeautifulSoup(page, 'html.parser')


sgpa = soup.find('span', attrs={'id':'lblSGPA'})
sgpa = sgpa.text.strip()

print(usn + ': ' + sgpa)
