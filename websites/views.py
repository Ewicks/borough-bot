from django.shortcuts import render, redirect
from .models import *
from .forms import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
import time
import pprint

# Fix bugs, get the rows to be searched by word for just the description not everything like the address
# fix data

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def get_word_objects():
	words = Word.objects.values_list('word', flat=True)
	objectlist = list(words)

	return objectlist

def test(request):
    if request.method == 'POST':
        datesdict = request.POST.dict()
        startdate = datesdict['startdate']
        enddate = datesdict['enddate']
        wordlist = get_word_objects()
        my_list = scraper(startdate, enddate, wordlist)

        # Open the Google Spreadsheet using its title
        # Set up the credentials
        # my_list = [('one', 'ethan'), ('two', 'wicks'), ('three', 'ofrm')]

        # Set up the credentials
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/ethanwicks/Desktop/credentials.json", scope)
        client = gspread.authorize(creds)

        # Open the Google Spreadsheet using its title
        spreadsheet = client.open("project")

        # Select the desired worksheet
        worksheet = spreadsheet.get_worksheet(0)  # You can change the index to select a different sheet

        worksheet.clear()

        # Define column titles
        column_titles = ["Index", "Name", "Address"]

        # Initialize data_to_write with header row
        data_to_write = [column_titles]

        # Loop through your_list with index
        for index, item in enumerate(my_list):
            row_data = [index + 1] + list(item)
            data_to_write.append(row_data)

        # Write data to the spreadsheet
        worksheet.append_rows(data_to_write)

        # Close the connection
        creds = None



        context = {
            'my_list': my_list,
        }

        return render(request, 'test.html', context)


def richmond(request):
    words = Word.objects.all()
    form = WordForm()
    dateform = DateForm()

    if request.method == 'POST':
        print(request.POST)
        form = WordForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('richmond')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'richmond.html', context)





def convert(s):
 
    # initialization of string to ""
    new = ""
 
    # traverse in the string
    for x in s:
        new = new + x + '|'
 
    # return string
    return new


row_list = []
address_list = []
name_list = []
data = []

def format_address(addresss):
    formatted_address = addresss.replace('\n', ' ')
    address_list.append(formatted_address)


def scraper(startdate, enddate, wordlist):
    data = []
   
    words = convert(wordlist)
    words_search_for = words.rstrip(words[-1])
 
    parsed_startdate = pd.to_datetime(startdate, format='%Y/%m/%d')
    parsed_enddate = pd.to_datetime(enddate, format='%Y/%m/%d')
    reversed_startdate = parsed_startdate.strftime('%d/%m/%Y')
    reversed_enddate = parsed_enddate.strftime('%d/%m/%Y')

    # Set up the WebDriver (you may need to provide the path to your chromedriver executable)
    driver = webdriver.Chrome()

    url = 'https://www2.richmond.gov.uk/lbrplanning/Planning_Report.aspx'
    driver.get(url)

    # Input start and end dates
    input_element1 = driver.find_element(By.ID, 'ctl00_PageContent_dpValFrom')
    input_element2 = driver.find_element(By.ID, 'ctl00_PageContent_dpValTo')
    input_element1.send_keys(reversed_startdate)
    input_element2.send_keys(reversed_enddate)
    # Click the search button
    search_element = driver.find_element(By.CLASS_NAME, 'btn-primary')


    # Wait for the cookie consent popup to appear
    wait = WebDriverWait(driver, 10)
    cookie_popup = wait.until(EC.presence_of_element_located((By.ID, 'ccc-end')))

    # Locate and click the "Accept" button
    accept_button = cookie_popup.find_element(By.ID, 'ccc-dismiss-button')
    accept_button.click()

    # Select 500 to show max results
    num_results_element = Select(driver.find_element(By.ID, 'ctl00_PageContent_ddLimit'))
    num_results_element.select_by_visible_text('500')

    # Click submit for advanced results page
    search_element.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'infocontent')))
    # driver.execute_script("location.reload(true);")
    # ctl00_PageContent_lbl_APPS


    # Get the page source after the search
    page_source = driver.page_source

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')


    span_div = driver.find_element(By.ID, 'ctl00_PageContent_lbl_APPS')
    num_results = span_div.find_element(By.TAG_NAME, 'strong')

    if (int(num_results.text) == 500):
        print('Results over 500 please alter your search results')
        driver.quit()
    else:
        print('Number of results for this search is: ' + num_results.text)



    searchResultsPage = soup.find('ul', class_='planning-apps')
    searchResults = searchResultsPage.find_all('li')

    # search the description but append all rows with key words in description to row_list
    for row in searchResults:
        address_divs = row.find_all('p')
        address_desc = address_divs[1].text

        if (re.search(words_search_for, address_desc, flags=re.I)):
            row_list.append(row)
    

    for row in row_list:
        # Find the address and add to address_list
        address_div = row.find('h3')
        address = address_div.text.strip()
        format_address(address)

        a_tag = row.find('a')
        href_value = a_tag.get('href')
        element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//a[@href='{href_value}']"))
        )
        element.click()
        try:
            subtab = None
            subtab = driver.find_element(By.ID, 'ctl00_PageContent_btnShowApplicantDetails')
        except:
            driver.back()
            name_list.append('n/a')
            continue

    
        subtab.click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'ctl00_PageContent_lbl_Applic_Name')))
        name_page_source = driver.page_source
        name_soup = BeautifulSoup(name_page_source, 'html.parser')
        name = name_soup.find('span', id='ctl00_PageContent_lbl_Applic_Name')
        name_list.append(name.text.strip())

        driver.back()
        driver.back()


    merge_data = zip(name_list, address_list)

    for item in merge_data:
        data.append(item)

    print(data)

    # Close the browser window
    driver.quit()
    return data




        