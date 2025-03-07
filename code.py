import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText



def sending_email(to_email, subject, body, from_email, smtp_server, smtp_port, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(from_email, password)
               
        server.sendmail(from_email, to_email, msg.as_string())
        
        server.quit()
        
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {str(e)}")



import csv

def send_bulk_emails(file_path, from_email, smtp_server, smtp_port, password):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        
        for row in reader:
            to_email = row[2]  
            subject = "Ready to Take Your Business to the Next Level?"
            body = f"""Hey {row[0]},
    
I hope you're doing well! My name is XYZ, and I'm the head of XYZ Marketers. We specialize in helping businesses like yours achieve significant growth through tailored marketing strategies that drive results.

Whether you're looking to boost your brand visibility, generate more leads, or improve your online presence, we have the expertise to help you succeed. I'd love to schedule a quick call to discuss how we can support your business goals and elevate your marketing efforts.

Would you be available for a brief chat sometime this week?

Looking forward to hearing from you!

Thanking You
XYZ
CEO
XYZ Marketers"""
            sending_email(to_email, subject, body, from_email, smtp_server, smtp_port, password)


send_bulk_emails('info.csv', 'your_email@gmail.com', 'smtp.gmail.com', 587, 'your_password') 









    
  