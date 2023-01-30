import requests as r
import json
import pandas as pd


class USACApi:

    def __init__(self):
        self.core = 'https://laravel-api.usacycling.org/api/v1'
        self.phpCore = 'https://legacy.usacycling.org'
        pass

    def getCollegiateClubs(self):
        uri = '/collegiate_clubs'
        res = r.get(self.core + uri).text
        return json.loads(res)

    def getUciCountries(self):
        uri = '/uci/proxy/countries'
        res = r.get(self.core + uri).text
        return json.loads(res)

    def getProTeams(self):
        uri = '/pro_teams'
        res = r.get(self.core + uri).text
        return json.loads(res)

    def getDomesticClubs(self):
        uri = '/domestic_clubs'
        res = r.get(self.core + uri).text
        return json.loads(res)

    def getTeams(self):
        uri = '/teams'
        res = r.get(self.core + uri).text
        return json.loads(res)
        
    # NOT WORKING
    # def getLicenseCatagories(self):
    #     uri = '/licenses/categories'
    #     res = r.get(self.core + uri).text
    #     return json.loads(res)

    def getProfileLicenses(self, profile_id):
        uri = '/profiles/{}/licenses'.format(str(profile_id))
        res = r.get(self.core + uri).text
        return json.loads(res)

    def getProfileMemberships(self, profile_id):
        uri = '/profiles/{}/memberships'.format(str(profile_id))
        res = r.get(self.core + uri).text
        return json.loads(res)

    # def getProfileMembershipsFamily(self, profile_id):
    #     uri = '/profiles/{}/memberships/family'.format(str(profile_id))
    #     res = r.get(self.core + uri).text
    #     return json.loads(res)

    def getCurrentOnlineOrIntlEnrollment(self, profile_id):
        uri = '/profiles/{}/current_online_or_intl_enrollment'.format(
            str(profile_id))
        res = r.get(self.core + uri).text
        return json.loads(res)

    def getAllEvents(self):
        uri = '/event_search/'
        res = r.get(self.core + uri).text
        return json.loads(res)

    def getResByCompId(self, compId):
        uri = '/results/index.php'
        payload = {'compid': compId}
        res = r.get(self.phpCore + uri, params=payload).text

        # this parses all the tables in webpages to a list
        df_list = pd.read_html(res)

        df = df_list[0]

        # [col][row]
        # data starts at row 4

        masterList = []
        i = 4
        cur = []
        while True:
            try:
                if((i-4) % 3 == 0):
                    # spliting the date off from the race title string
                    splitFromInfo = df[0][i].split(' - ')

                    # appending both items to the list
                    cur.append(splitFromInfo[0])
                    cur.append(splitFromInfo[1])

                elif((i-4) % 3 == 1):
                    # reading and appending all other data from table
                    for k in range(7):
                        # spliting data for place then appending
                        if(k == 0):

                            splitArr = self.__splitPlaceData(str(df[k][i]))
                            cur.append(splitArr[0])
                            cur.append(splitArr[1])
                        # runs if not place data
                        else:
                            cur.append(df[k][i])
                else:
                    newDict = {
                        "raceDate": str(cur[0]),
                        "raceName": str(cur[1]),
                        "place": str(cur[2]),
                        "finishers": str(cur[3]),
                        "racePoints": str(cur[4]),
                        "racerName": str(cur[5]),
                        "compId": str(cur[6]),
                        "raceTime": str(cur[7]),
                        "bibNum": str(cur[8]),
                        "team": str(cur[9]),
                    }
                    masterList.append(newDict)
                    cur = []
                    pass
                i += 1
            except:
                break

        return masterList

    # helper function for splitting the place from string

    def __splitPlaceData(self, placeString):
        rtnArr = []
        if ' / ' in placeString:
            splitStr = placeString.split(' / ')
            rtnArr.append(splitStr[0])
            rtnArr.append(splitStr[1])
            return rtnArr
        else:
            rtnArr.append(placeString)
            rtnArr.append('nan')
            return rtnArr
