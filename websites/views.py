from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .bots.richmond_bot import richmond_bot
from .bots.kingston_bot import kingston_bot
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def get_word_objects():
	words = Word.objects.values_list('word', flat=True)
	objectlist = list(words)

	return objectlist



def richmond(request):
    words = Word.objects.all()
    form = WordForm()
    dateform = DateForm()

    if request.method == 'POST':
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

def kingston(request):
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
    return render(request, 'kingston.html', context)




def results(request):
    if request.method == 'POST':
        datesdict = request.POST.dict()
        startdate = datesdict['startdate']
        enddate = datesdict['enddate']
        wordlist = get_word_objects()
        print(request.POST)
        # borough = ''
        borough = request.POST.get('borough')
        print(borough)



        if borough == 'richmond':
            my_list = richmond_bot(startdate, enddate, wordlist)
        if borough == 'kingston':
            my_list = kingston_bot(startdate, enddate, wordlist)
        else:
            print('else')
       
        # my_list = richmond_bot(startdate, enddate, wordlist)

        # Open the Google Spreadsheet using its title
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

        return render(request, 'results.html', context)


