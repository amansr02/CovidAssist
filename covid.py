import requests
import json

URL_COUNTRY = "https://covidapi.info/api/v1/country/"
URL_GLOBAL  = "https://covidapi.info/api/v1/global"

class CovidAssist():

    def __init__(self,country="",date1="",date2=""):
        self.country = country
        self.date = date1
        self.date_range = [date1,date2]
    
    def get_country_data(self,text):
        return requests.get(url = URL_COUNTRY+text) 

    def get_global_data(self,text):
        return requests.get(url = URL_GLOBAL+text)

    def get_latest_date(self):
        return requests.get("https://covidapi.info/api/v1/latest-date")

    def get_general_country_data(self):
        result = ""
        if(self.country == ""):
            return "Invalid"
        else:
            result = self.get_country_data(self.country) 
            return result.text

    def get_latest_country_data(self):
        result = ""
        if(self.country == ""):
            return "Invalid"
        else:
            result = self.get_country_data(text = self.country+"/latest")
            return result.text

    def get_specific_country_data(self):
        result = ""
        if(self.country == "" or self.date == ""):
            return "Invalid"
        else:
            result = self.get_country_data(text = self.country+"/"+self.date)
            return result.text

    def get_range_country_data(self):
        result = ""
        if(self.country == "" or self.date_range[0]=="" or self.date_range[1]==""):
            return "Invalid"
        else:
            result = self.get_country_data(text = self.country+"/timeseries/"+self.date_range[0]+"/"+self.date_range[1])
            return result.text

    def get_latest_global_data(self):
        pass

    def get_specific_global_data(self):
        pass

    def get_range_global_data(self):
        pass

