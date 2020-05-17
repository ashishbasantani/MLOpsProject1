import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("email", "password")
message = "Hey developer the file committed by you for training model has some flaws due to which accuracy of model is not good so some tweaks are automatically done to get better accuracy of model"
s.sendmail("ashishbasantani8897@gmail.com", "ashishbasantani77@gmail.com", message)
print("Mail Sent")
s.quit() 
