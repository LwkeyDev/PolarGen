# PolarGen

This tool is made for generating fake info.  It can generate valid credit card numbers, CVV, experation date, and it can generate fake names, addresses, phone numbers, emails, and even jobs.  You can also use this tool to check if the credit card numbers generated are valid, by using the Credit Card Validator.  After you have generate info, you can then choose to save the info in a txt file which you can access later.  The way the Credit Card Generator works is by using Luhn's algorithim.  By creating a string of numbers that follow this algorithim, we can make credit card numbers that can pass validation.  Unfortunately, these credit cards do not hold any real money, however could pottentialy be used for free trials as they pass as real credit cards.  

# Disclaimer: Using it for the purpose of paying to a place/organization that is not yours is illegal, and should not be done under any circumstances.  The main reason I put it into this tool was for educational purposes, and so that people could test the security of their own websites and buisnesses.  We are not responsible for anything you choose to do with this tool, and any trouble you may get into.  

![Screenshot 2024-03-14 225507](https://github.com/LwkeyDev/PolarGen/assets/95990372/e1507e04-8529-4fa3-962e-a0955500bf65)

# Windows Install:
First you need to download the zip file by clicking code and then clicking download ZIP  
Next, extract the zip file    
Once extracted, open the extracted folder in terminal by right clicking on an empty space while in the folder, and clicking the CMD button
Then run

```
pip install -r req.txt
```
Once the requirements have been installed, simply close out of terminal and double click the PolarGen.BAT file  

# Linux/Mac install
First, make sure you have pip installed  
Then, go into terminal, and type
```
git clone https://github.com/LwkeyDev/PolarGen.git  
```
Once installed, go into the directory (CD for linux) and type
```
pip install -r req.txt
``` 
Now, to run the tool, simply type  

```
python3 PolarGen.py
```



