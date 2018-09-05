from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def email_doc(inputs):
    subject = 'Your legal Doc from legal assist'
    sender = 'leoigane@gmail.com'
    receiver = inputs['email']

    text_content = render_to_string('email/email.txt',inputs)
    html_content = render_to_string('email/email.html',inputs)
    # text_content = render_to_string('email/email.txt',{"sirname": sirname})
    # html_content = render_to_string('email/email.html',{"sirname": sirname})
    # text_content = render_to_string('email/email.txt',{"othernames": othernames})
    # html_content = render_to_string('email/email.html',{"othernames": othernames})
    # text_content = render_to_string('email/email.txt',{"idnumber":idnumber})
    # html_content = render_to_string('email/email.html',{"idnumber": idnumber})
    # text_content = render_to_string('email/email.txt',{"boxnumber": boxnumber})
    # html_content = render_to_string('email/email.html',{"boxnumber": boxnumber})
    # text_content = render_to_string('email/email.txt',{"town": town})
    # html_content = render_to_string('email/email.html',{"town": town})
    # text_content = render_to_string('email/email.txt',{"dob": dob})
    # html_content = render_to_string('email/email.html',{"dob": dob})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
