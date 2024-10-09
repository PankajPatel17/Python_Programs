from django.shortcuts import render,redirect
from .models import User , Product,Wishlist
import requests
import random

# Create your views here.

def index(request):
	return render(request,'index.html')

def seller_index(request):
	return render(request,'seller-index.html')

def category(request):
	product=Product.objects.all()
	return render(request,'category.html',{'product':product})

def single_product(request):
	return render(request,'single-product.html')

def checkout(request):
	return render(request,'checkout.html')

def cart(request):
	return render(request,'cart.html')

def blog(request):
	return render(request,'blog.html')

def single_blog(request):
	return render(request,'single-blog.html')

def tracking(request):
	return render(request,'tracking.html')

def elements(request):
	return render(request,'elements.html')

def contact(request):
	return render(request,'contact.html')

def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Already Registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
						profile_picture=request.FILES['profile_picture'],
						usertype=request.POST['usertype'],
						
					)
				msg="User Registered Successfully"
				return render(request,'signup.html',{'msg':msg})
			else:
				msg="Password and Confrim Password Does Not Match"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['profile_picture']=user.profile_picture.url
				if user.usertype=="Buyer":
					return render(request,'index.html')
				else:
					return render(request,'seller-index.html')
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email Not Registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_picture']
		msg="User Logged Out Successfully"
		return render(request,'login.html',{'msg':msg})
	except:
		msg="User Logged Out Successfully"
		return render(request,'login.html',{'msg':msg})

def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		try:
			user.profile_picture=request.FILES['profile_picture']
		except:
			pass
		user.save()
		msg="Profile Updated Successfully"
		if user.usertype=="Buyer":
			return render(request,'profile.html',{'user':user,'msg':msg})
		else:
			return render(request,'seller-profile.html')
	else:
		if user.usertype=="Buyer":
			return render(request,'profile.html',{'user':user})
		else:
			return render(request,'seller-profile.html',{'user':user})
def change_password(request):
		user=User.objects.get(email=request.session['email'])
		if request.method=="POST":
			if user.password==request.POST['old_password']:
				if request.POST['new_password']==request.POST['cnew_password']:
					if user.password!=request.POST['new_password']:
						user.password=request.POST['new_password']
						user.save()
						msg="Password Changed Successfully.Login Again."
						del request.session['email']
						return render(request,'login.html',{'msg':msg})
					else:
						msg="New Password Can't Be Same As Old Password"
						if user.usertype=="Buyer":	
							return render(request,'change-password.html',{'msg':msg})
						else:
							return render(request,'seller-change-password.html',{'msg':msg})
				else:
					msg="New Password and Confirm New Password Does Not Match"
					if user.usertype=="Buyer":
						return render(request,'change-password.html',{'msg':msg})
					else:
						return render(request,'seller-change-password.html',{'msg':msg})
			else:
				msg="Old Password Does Not Match"
				if user.usertype=="Buyer":
					return render(request,'change-password.html',{'msg':msg})
				else:
					return render(request,'seller- change-password.html',{'msg':msg})

		else:
			if user.usertype=="Buyer":
				return render(request,'change-password.html')
			else: 
				return render(request,'seller-change-password.html')

def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(mobile=request.POST['mobile'])
			otp=str(random.randint(1000,9999))
			mobile=str(request.POST['mobile'])
			url = "https://www.fast2sms.com/dev/bulkV2"
			querystring = {"authorization":"YOUR_API_KEY","variables_values":otp,"route":"otp","numbers":mobile}
			headers = {'cache-control': "no-cache"}
			response = requests.request("GET", url, headers=headers, params=querystring)
			print(response.text)
			request.session['otp']=otp
			request.session['mobile']=mobile
			msg="OTP Sent Successfully"
			return render(request,'otp.html',{'msg':msg })
		except:
			msg="Mobile Not Registered"
			return render(request,'forgot-password.html',{'msg':msg})
	else:
		return render(request,'forgot-password.html')

def verify_otp(request):
	return render(request,'otp.html')

def add_product(request):
	seller=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		Product.objects.create(
			seller=seller,
			product_category=request.POST['product_category'],
			product_size=request.POST['product_size'],
			product_name=request.POST['product_name'],
			product_desc=request.POST['product_desc'],
			product_price=request.POST['product_price'],
			product_image=request.FILES['product_image'],

		)
		msg="Product Added Successfully"
		return render(request,'add-product.html',{'msg':msg})

	else:	
		return render(request,'add-product.html')

def view_product(request):
	seller=User.objects.get(email=request.session['email'])
	products=Product.objects.filter(seller=seller)
	return render(request,'view-product.html',{'products':products})

def seller_product_detail(request,pk):
	product=Product.objects.get(pk=pk)
	return render(request,'seller-product-detail.html',{'product':product})

def seller_product_edit(request,pk):
	product=Product.objects.get(pk=pk)
	if request.method=="POST":
		product.product_category=request.POST['product_category']
		product.product_size=request.POST['product_size']
		product.product_name=request.POST['product_name']
		product.product_desc=request.POST['product_desc']
		product.product_price=request.POST['product_price']
		try:
			product.product_image=request.FILES['product_image']
		except:
			pass
		product.save()
		msg="Product Updated Successfully"
		return render(request,'seller-product-edit.html',{'product':product,'msg':msg})
	else:
		return render(request,'seller-product-edit.html',{'product':product})

def seller_product_delete(request,pk):
	product=Product.objects.get(pk=pk)
	product.delete()
	return redirect('view-product')

def product_by_category(request,cat):
	products=[]
	if cat == "all":
		products=Product.objects.all()
	else:
		products=Product.objects.filter(product_category=cat)
	return redirect('category',{'products':products})

def product_detail(request,pk):
	wishlist_flag=False
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	try:
		Wishlist.objects.get(user=user,product=product)
		wishlist_flag=True
	except:
		pass
	return render(request,'product-detail.html',{'product':product,'wishlist_flag':wishlist_flag})

def add_to_wishlist(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Wishlist.objects.create(user=user,product=product)
	return redirect('wishlist')

def remove_from_wishlist(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	wishlist=Wishlist.objects.get(user=user,product=product)
	wishlist.delete()
	return redirect('wishlist')



def wishlist(request):
	user=User.objects.get(email=request.session['email'])
	wishlists=Wishlist.objects.filter(user=user)
	return render(request,'wishlist.html',{'wishlists':wishlists})