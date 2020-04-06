from django.urls import path
from . import views
urlpatterns=[
 
	path('',views.Index, name="Index"),
	path('<int:question_id>/',views.details,name="detail"),
	#Expect an integer (int) to be present in the URL at this point & bind it to the question_id argument of the views.results method.
	# string by question id is from 0-9 and it is /polls/2 
	path('<int:question_id>/result/',views.result,name="result"),
	path('<int:question_id>/vote/',views.votes,name="votes"),
	
 ]
app_name="polls"