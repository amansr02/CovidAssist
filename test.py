from covid import CovidAssist

def main():

    agent = CovidAssist(country = "IND", date1 = "2020-04-2",date2="2020-04-03")

    #gets all time series data for a country
    print(agent.get_general_country_data())

    #gets latest data for a country
    print(agent.get_latest_country_data())
    
    #gets data of a country by date
    print(agent.get_specific_country_data())

    #gets data of a country between a range
    print(agent.get_range_country_data())

if __name__ == "__main__":
    main()
