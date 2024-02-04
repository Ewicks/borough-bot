from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
from .bots.richmond_bot import richmond_bot
from .bots.kingston_bot import kingston_bot
from .bots.woking_bot import woking_bot
from .bots.southwark_bot import southwark_bot
from .bots.guildford_bot import guildford_bot
from .bots.epsom_bot import epsom_bot
from .bots.lewisham_bot import lewisham_bot
from .bots.hammersmith_fulham_bot import hammersmith_fulham_bot
from .bots.bromley_bot import bromley_bot
from .bots.merton_bot import merton_bot
from .bots.kensington_chelsea_bot import kensington_chelsea_bot
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.contrib.auth.decorators import login_required
from django.utils import timezone




# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def get_word_objects():
	words = Word.objects.values_list('word', flat=True)
	objectlist = list(words)

	return objectlist

def test(request):
    return render(request, 'test.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def reviews(request):
    return render(request, 'reviews.html', {})


def deleteword(request, pk, redirect_to):
    word = Word.objects.get(id=pk)
    word.delete()
  
    return redirect(reverse(redirect_to))




@login_required
def richmond(request):
    words = Word.objects.filter(user=request.user)
    form = WordForm()
    dateform = DateForm()

    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word_instance = form.save(commit=False)
            word_instance.user = request.user  # Associate the word with the current user
            word_instance.save()
            return redirect('richmond')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'richmond.html', context)


def kensington_chelsea(request):
    words = Word.objects.all()
    form = WordForm()
    dateform = DateForm()

    if request.method == 'POST':
        form = WordForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('kensington_chelsea')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'kensington_chelsea.html', context)

def epsom(request):
    words = Word.objects.all()
    form = WordForm()
    dateform = DateForm()

    if request.method == 'POST':
        form = WordForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('epsom')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'epsom.html', context)

def merton(request):
    words = Word.objects.all()
    form = WordForm()
    dateform = DateForm()

    if request.method == 'POST':
        form = WordForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('merton')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'merton.html', context)

def bromley(request):
    words = Word.objects.all()
    form = WordForm()
    dateform = DateForm()

    if request.method == 'POST':
        form = WordForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('bromley')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'bromley.html', context)

def hammersmith_fulham(request):
    words = Word.objects.all()
    form = WordForm()
    dateform = DateForm()

    if request.method == 'POST':
        form = WordForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('hammersmith_fulham')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'hammersmith_fulham.html', context)

def woking(request):
    words = Word.objects.all()
    form = WordForm()
    dateform = DateForm()

    if request.method == 'POST':
        form = WordForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('woking')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'woking.html', context)

def lewisham(request):
    words = Word.objects.all()
    form = WordForm()
    dateform = DateForm()

    if request.method == 'POST':
        form = WordForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('lewisham')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'lewisham.html', context)

def elmbridge(request):
    words = Word.objects.all()
    form = WordForm()
    dateform = DateForm()

    if request.method == 'POST':
        form = WordForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('elmbridge')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'elmbridge.html', context)

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
        return redirect('kingston')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'kingston.html', context)

def southwark(request):
    words = Word.objects.all()
    form = WordForm()
    dateform = DateForm()


    if request.method == 'POST':
        print(request.POST)
        form = WordForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('southwark')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'southwark.html', context)

def guildford(request):
    words = Word.objects.all()
    form = WordForm()
    dateform = DateForm()


    if request.method == 'POST':
        print(request.POST)
        form = WordForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('guildford')

    context = {
        'form': form,
        'words': words,
        'dateform': dateform,
    }
    return render(request, 'guildford.html', context)




def results(request):
    if request.method == 'POST':
        datesdict = request.POST.dict()
        startdate = datesdict['startdate']
        enddate = datesdict['enddate']
        wordlist = get_word_objects()
        print(request.POST)
        borough = request.POST.get('borough')
        print(borough)


        if borough == 'richmond':
            my_list = richmond_bot(startdate, enddate, wordlist)
        if borough == 'kingston':
            my_list = kingston_bot(startdate, enddate, wordlist)
        if borough == 'woking':
            my_list = woking_bot(startdate, enddate, wordlist)
        if borough == 'southwark':
            my_list = southwark_bot(startdate, enddate, wordlist)
        if borough == 'guildford':
            my_list = guildford_bot(startdate, enddate, wordlist)
        if borough == 'epsom':
            my_list = epsom_bot(startdate, enddate, wordlist)
        if borough == 'lewisham':
            my_list = lewisham_bot(startdate, enddate, wordlist)
        if borough == 'hammersmith_fulham':
            my_list = hammersmith_fulham_bot(startdate, enddate, wordlist)
        if borough == 'bromley':
            my_list = bromley_bot(startdate, enddate, wordlist)
        if borough == 'merton':
            my_list = merton_bot(startdate, enddate, wordlist)
        if borough == 'kensington_chelsea':
            my_list = kensington_chelsea_bot(startdate, enddate, wordlist)

        data_list = my_list[0]
        num_results = my_list[1]
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
        for index, item in enumerate(data_list):
            row_data = [index + 1] + list(item)
            data_to_write.append(row_data)

        # Write data to the spreadsheet
        worksheet.append_rows(data_to_write)

        # Close the connection
        creds = None

        if request.user and request.user.is_authenticated:
            user_instance = request.user

            # Create a new Scrape instance associated with the authenticated user
            new_scrape = Scrape.objects.create(
                user=user_instance,
                borough=borough,
                startdate=startdate,
                enddate=enddate,
                results_number=num_results,
                date_added=timezone.now()  # Add the current date and time
            )
            print(new_scrape.date_added)


        context = {
            'my_list': data_list,
            'num_results': num_results,

        }

        return render(request, 'results.html', context)


