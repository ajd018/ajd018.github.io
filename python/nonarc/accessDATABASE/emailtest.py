import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'coolemail@whatever.com'
mail.Subject = 'subject text here'
mail.Body = 'Please print seven copies of this map in 11x17 size format'


#In case you want to attach a file to the email
attachment  = r"\\cool\folder\bro\mapdocument.pdf"
mail.Attachments.Add(attachment)

mail.Send()
