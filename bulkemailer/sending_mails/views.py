from django.shortcuts import render,HttpResponse

# Create your views here.
from django.views.generic import TemplateView

import os 
import google.generativeai as genai
import io,csv


class EmailSender(TemplateView):
    template_name="email_generator.html"

   

    def post(self,request,*args,**kwargs):
       form_type=request.POST.get("form_type")

       if form_type=="A":
           prompt=request.POST.get("EmailPrompt")
           print(prompt)
           
           API_KEY=os.environ.get("API_KEY")
           genai.configure(api_key=API_KEY)
           
           model = genai.GenerativeModel("gemini-1.5-flash")
           response = model.generate_content(f"Create a personalized email template for the topic: {prompt}. The template should begin with 'Dear  [Name],', where '[Name]' is a placeholder for the recipient's name. The body of the email should convey a warm and professional tone, addressing the specific needs or interests related to the topic. Ensure that the template is engaging and concludes with a strong call to action or a thoughtful closing statement. The final output should be a plain text email template with the following format")
                                            
        
           return render(request,self.template_name,{"email_body":response.text,"email_subject":"greattt"})
       if form_type=="B":
           csv_file=request.POST.get('recipientList')
           print(csv_file)



    




           




