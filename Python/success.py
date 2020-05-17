import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("email", "password")
message = "Hey developer the model is ready and giving good accuracy"
s.sendmail("ashishbasantani8897@gmail.com", "ashishbasantani77@gmail.com", message)
print("Mail Sent")
s.quit() 
