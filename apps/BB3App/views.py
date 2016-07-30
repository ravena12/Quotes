from django.shortcuts import render, redirect
from .models import User, UserManager, Quotes, QuoteManager
from django.contrib  import messages
import datetime
from django.core.urlresolvers import reverse


####################################################

# PROCESSING DATA 

####################################################

def processregister(request):
	results = User.userManager.isValidReg(request.POST)
	errors = results[1]
	for error in errors:
		messages.error(request, error)
	if results[0]:
		return redirect(reverse('my_quote_index'))
	else: 
		return redirect(reverse('my_quote_index'))

def processlogin(request):
	results = User.userManager.validlog(request.POST)
	print request.POST['username']
	if results[0]:
		request.session['id'] = results[1].id
		print request.session['id']
		
		request.session['username'] = results[1].username

		request.session['first_name'] = results[1].first_name

		return redirect(reverse('my_quote_home'))
	else: 
		errors = results[1]
		for error in errors:
			messages.warning(request, error)
		return redirect(reverse('my_quote_index'))

def processquote(request):
	userid = User.objects.get(id= request.session['id']).id
	results = Quotes.quoteManager.isvalidquote(request.POST, userid)
	if results[0]:
		return redirect(reverse('my_quote_home'))
	else: 
		errors = results[1]
		for error in errors:
			messages.warning(request, error)
		return redirect(reverse('my_quote_home'))








####################################################

# DISPLAY PAGES SECTION  

####################################################

def index(request):
	return render(request, 'BB3Temp/index.html')


def home(request):
	user = User.objects.get(id=request.session["id"])
	print user
	("*"*50)
	for item in Quotes.objects.all():
		print item.quoted_by
		print item.message
	("*"*50)
	print Quotes.objects.all()
	context = {
		'quotes': Quotes.objects.all(),
		'test':Quotes.objects.exclude(other_quotes=user),
		'c': User.objects.get(id=request.session["id"]),
		'thisuser':Quotes.objects.filter(creator_quotes = user)| Quotes.objects.filter(other_quotes=user.id),
		'oo': Quotes.objects.filter(other_quotes = user),
		'oneu': Quotes.objects.filter(creator_quotes=user),
		'other_q': Quotes.objects.exclude(creator_quotes = user)
	}

	return render(request, 'BB3Temp/home.html',context)

def register(request):
	return render(request, 'BB3Temp/registration.html')



def destroy(request, id):
	user = User.objects.get(id=request.session["id"]) 
	wish = Quotes.objects.get(id =id)
	user = User.objects.get(id=request.session['id'])
	wish.other_quotes.remove(user)
	return redirect(reverse('my_quote_home'))

def delete(request, id):
	item = Quotes.objects.get(id = id)
	item.delete()
	return redirect(reverse('my_quote_home'))

def join(request, id):
	wish = Quotes.objects.get(id =id)
	user = User.objects.get(id=request.session['id'])
	wish.other_quotes.add(user)
	return redirect(reverse('my_quote_home'))

def createproduct(request):
	return render(request, 'BB3Temp/add.html')

def product(request, id):
	user = User.objects.get(id=request.session["id"])
	for item in Quotes.objects.filter(id = id):
		count = item.creator_quotes.creator_quotes.all().count()
		messageall = item.creator_quotes.creator_quotes.all()
		arr = []
		test = ""
		print messageall
		for x in messageall:
			quote = x.quoted_by
			message = x.message
			test = quote + " " + ":" + " " + message  
			arr.append(test)
		request.session['arr'] = arr
		request.session['count'] = count
	context =  {
		'wishes': Quotes.objects.get(id = id),
		'quotes': Quotes.objects.all(),
		'count': request.session['count'],
		'quotes': request.session['arr'],

	}
	return render(request, 'BB3Temp/product.html', context)

 
def logout(request):
	request.session.clear()
	return redirect(reverse('my_quote_index'))

