This main.py file is represent the FastAPI api's
there have 2 api path 
1. "/scrape"
2. "/scrape_results"

before run this file make sure python is installed in your system 
using FastAPI Python 3.8+ require
after now open your cmd or terminal. if python is installed please install FastAPI with help of command 
--> pip install fastapi

after install Fastapi install requests module with help of command 
--> pip install requests

now run the FastAPI server with help of command 
--> python -m unicorn main:app --reload

now open your postman and access this both api according to your requirements
according to assignment first api "/scrape" return the id's and because it is a post api 
so we can pass some data in Body -> raw in the structure of 
{
    "name": "adam",
    "organization": "google"
}
and secound api "/scrape_results" return the complete data of the given id  and because it's a get api so no need to pass anything 
but according to requirements of the assignment pass data in Body -> raw in the structure of 
{
    "job_id": "5900f4a09d7968fdcd093dba"
}

If you facing any error while access the api's please let me know I will make changes according to data that is require in scraping.
Thanks for read 