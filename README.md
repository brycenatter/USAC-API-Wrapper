# USA-Cycling-API
 Wrapper class for accessing results and data from USA Cycling. THIS IS NOT OFFICIALLY SUPPORTED AND SHOULD NOT BE ABUSED.
 
## Usage

### Importing and creating a USACApi object

Ensure the usacapi.py file is in current directory or specify specific path. The constructor takes no arguments.

```python3
from usacapi import USACApi
u = USACApi()
```

### Methods that don't require profile_id

**Get Results by Competition ID**: returns list of all USAC race results by a given rider. Requires a competition id. This can be found on USAC's legacy website as under a given rider's result entry. The competition id is also the rider's USAC license number.

**NOTE**: USAC is inconsistent with their data representation of null. This is the primary reason the values in dicts contain string data types. Some common ways USAC handles null values are "nan", "Nan", or an empty string. Also, the race name contains important information about a given race, but there is not a standard format used, so data parsing is quite difficult.

```python3
u.getResByCompId(string_of_compId)
```

Example of an item in the list:

```
{
	'raceDate': '07/02/2022', 
	'raceName': '2022 USA Cycling Amateur Road National Championships  | CRIT | Junior | 17-18', 
	'place': '20', 
	'finishers': '77', 
	'racePoints': '240.51', 
	'racerName': 'Bryce NATTER', 
	'compId': '538985', 
	'raceTime': '1:02:09', 
	'bibNum': '492', 
	'team': 'JCS'
}
```


**Get Collegiate Clubs**: returns list of json objects that describe all USA Cycling collegiate clubs and teams.

```python3
u.getCollegiateClubs()
```

Example of an item in the list:

```
{
	'club_id': 17157, 
	'club_name': 'Appalachian State University', 
	'club_org_id': None, 
	'club_ncaa_id': 29, 
	'club_updated_by_user': None, 
	'club_aff_type_id': 5, 
	'club_type_id': 2, 
	'club_legacy_id': 6895, 
	'club_aff_type': {'aff_type_id': 5, 'aff_type_description': 'Collegiate'}, 
	'club_aff_type.aff_type_description': 'Collegiate', 
	'club_aff_type_description': 'Collegiate', 
	'club_city': 'BOONE, NC', 
	'club_zip': '28608', 
	'is_active': True, 
	'expiration_date': '2023-12-31'
}
```

**Get UCI Countries**: returns a list of all UCI recognized countries plus a "stateless" category.

```python3
u.getUciCountries()
```

Example of an item in the list:

```
{
	'Code': 'USA', 
	'Icon': None, 'Id': 193, 
	'Name': 'UNITED STATES OF AMERICA'
}
```

**Get PRO Teams**: returns list of all pro teams recognized in the US. Also includes USA Cycling Colligate teams.

```python3
u.getProTeams()

```

Example of an item in the list:

```
{
	'club_id': 24926, 
	'club_name': 'UCI CTM: Jumbo-Visma Academy', 
	'club_org_id': None, 
	'club_ncaa_id': None, 
	'club_updated_by_user': None, 
	'club_aff_type_id': 6, 
	'club_type_id': 1, 
	'club_legacy_id': 17642, 
	'club_aff_type': {'aff_type_id': 6, 'aff_type_description': 'USPRO Team'}, 
	'club_aff_type.aff_type_description': 'USPRO Team', 
	'club_aff_type_description': 'USPRO Team', 
	'club_city': ', ', 
	'club_zip': None, 
	'is_active': True, 
	'expiration_date': '2023-12-31'
}
```

**Get Domestic Clubs**: returns list of all USA Cycling registered clubs including MTB and non-race teams.

```python3
u.getDomesticClubs()
```

Example of an item in the list:

```
{
	'club_id': 24881, 
	'club_name': 'Miami Blazers', 
	'club_org_id': None, 
	'club_ncaa_id': None, 
	'club_updated_by_user': None, 
	'club_aff_type_id': 1, 
	'club_type_id': 1, 
	'club_legacy_id': 17597, 
	'club_aff_type': {'aff_type_id': 1, 'aff_type_description': 'Club/Team'}, 
	'club_aff_type.aff_type_description': 'Club/Team', 
	'club_aff_type_description': 'Club/Team', 
	'club_city': ', ', 
	'club_zip': None, 
	'is_active': True, 
	'expiration_date': '2023-12-31'
}
```

**Get Teams**: returns list of all teams registered in the US

```python3
u.getTeams()
```

Example of an item in the list:

```
{
	'team_id': 19548, 
	'team_name': 'Zubaz/Tacocat Racing Team', 
	'team_club_id': 22884, 
	'women_only': 0, 
	'masters_only': 0, 
	'juniors_only': 0, 
	'collegiate_only': 0, 
	'under_twenty_three_only': 0, 
	'd_elite': 0, 
	'is_default': 1, 
	'is_novice': 1, 
	'is_intermediate': 1, 
	'is_advanced': 1, 
	'is_pro': 1, 
	'team_legacy_id': None, 
	'team_disciplines': [
		{'category_discipline_id': 19, 'discipline_name': 'Road Racing'}, 
		{'category_discipline_id': 20, 'discipline_name': 'Track Racing'}, 
		{'category_discipline_id': 23, 'discipline_name': 'Cyclocross Racing'},
		{'category_discipline_id': 31, 'discipline_name': 'Mountain Slalom'}, 	
		{'category_discipline_id': 32, 'discipline_name': 'Mountain Gravity'}, 	
		{'category_discipline_id': 33, 'discipline_name': 'Mountain Endurance'}], 
	'category_disciplines': [
		{'cd_id': 19, 'cd_value': 'Road Racing'}, 
		{'cd_id': 20, 'cd_value': 'Track Racing'}, 
		{'cd_id': 23, 'cd_value': 'Cyclocross Racing'}, 
		{'cd_id': 31, 'cd_value': 'Mountain Slalom'}, 
		{'cd_id': 32, 'cd_value': 'Mountain Gravity'}, 
		{'cd_id': 33, 'cd_value': 'Mountain Endurance'}
	], 
	'team_disciplines_names': 'Road Racing, Track Racing, Cyclocross Racing, Mountain Slalom, Mountain Gravity, Mountain Endurance', 
	'team_levels': 'Novice, Intermediate, Advanced, Pro', 
	'team_tags': 'Men, Women, Youth'
}
```

**Get All Events**: returns object of ALL USAC and BikeReg events. **DO NOT RECOMMEND** using this method. This method is incredibly slow as the returned object is very large. There are ways to narrow the search with request parameters, but this method does not use that implementation. 

```python3
u.getAllEvents()
```


### Methods that require profile_id

Profile id is part of USAC's new api that is becoming standard as they move away from their legacy website. Profile id's are not public, so finding information on a specific rider is difficult. You can find your profile is once you log in to your USAC account at https://myaccount.usacycling.org/profile/YOUR\_PROFILE\_ID


**Get Profile Licenses**: returns list of all current and expired USAC licenses for a given profile id.

```python3
u.getProfileLicenses(profile_id)
```

Example of an item in the list with redactions for privacy:

```
{
	'license_id': **REDACTED**, 
	'discipline_id': **REDACTED**, 
	'is_domestic': True, 
	'is_collegiate': False, 
	'is_international': False, 
	'is_professional': False, 
	'club': **REDACTED**, 
	'team': None, 
	'category_id': **REDACTED**, 
	'category_name': 'Road Category 3', 
	'discipline_name': 'Road Racing', 
	'license_type': **REDACTED**, 
	'license_type_name': 'Domestic Race', 
	'license_level': None, 
	'license_level_name': '', 
	'effective_date': '2019-12-30 00:00:00', 
	'expiration_date': **REDACTED**, 
	'status': None, 
	'status_description': None, 
	'club_name': **REDACTED**, 
	'team_name': None, 
	'is_premium': True
}
```

**Get Profile Memberships**: returns list of all memberships associated with a profile id.

```python3
u.getProfileMemberships(profile_id)
```

Example of an item in the list with redactions for privacy:

```
{
	'membership_id': **REDACTED**, 
	'membership_level': 2, 
	'membership_level_name': 'Premium', 
	'membership_status': 'Active', 
	'is_podium': 0, 
	'has_spot_insurance': False, 
	'membership_purchase_date': **REDACTED**, 
	'membership_expiration_date': **REDACTED**, 
	'profile_family': 0, 
	'membership_profile_id': **REDACTED**
}
```

**Get Current Online Or Intl Enrollment**: returns a lot of information for a given profile_id. Most data is personal so no example is shown.


```python3
u.getCurrentOnlineOrIntlEnrollment(profile_id)
```










