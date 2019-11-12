pb =[{"name": "Alabama", "abbreviation": "AL",
                          "counties": ["Dale", "Autauga", "Baldwin", "Bibb", "Bullock", "Chilton", "Coffee", "Coosa",
                                       "Etowah", "Franklin", "Lamar", "Macon", "Marion", "Morgan", "Randolph", "Sumter",
                                       "Wilcox", "Barbour", "Blount", "Butler", "Calhoun", "Chambers", "Cherokee",
                                       "Choctaw", "Clarke", "Clay", "Cleburne", "Colbert", "Conecuh", "Covington",
                                       "Crenshaw", "Cullman", "Dallas", "DeKalb", "Elmore", "Escambia", "Fayette",
                                       "Geneva", "Greene", "Hale", "Henry", "Houston", "Jefferson", "Lauderdale",
                                       "Lawrence", "Lee", "Lowndes", "Madison", "Marengo", "Marshall", "Mobile",
                                       "Monroe", "Montgomery", "Jackson", "Perry", "Pickens", "Pike", "Russell",
                                       "St. Clair", "Shelby", "Talladega", "Tallapoosa", "Tuscaloosa", "Walker",
                                       "Washington", "Winston", "Limestone"]},
                         {"name": "Alaska", "abbreviation": "AK",
                          "counties": ["Valdez-Cordova",
                                       "Wade Hampton", "Wrangell",
                                       "Yukon-Koyukuk",
                                       "Ketchikan Gateway",
                                       "Aleutians East", "Bethel",
                                       "Hoonah-Angoon", "Sitka",
                                       "Kenai Peninsula",
                                       "Kodiak Island",
                                       "Lake and Peninsula",
                                       "Nome", "Petersburg",
                                       "North Slope",
                                       "Northwest Arctic",
                                       "Southeast Fairbanks",
                                       "Yakutat",
                                       "Aleutians West",
                                       "Anchorage", "Bristol Bay",
                                       "Denali", "Dillingham",
                                       "Fairbanks North Star",
                                       "Haines", "Juneau",
                                       "Matanuska-Susitna",
                                       "Prince of Wales-Hyder",
                                       "Skagway"]},
                         {"name": "Arizona", "abbreviation": "AZ",
                          "counties": ["Mohave", "Santa Cruz", "Cochise", "Graham", "La Paz", "Pima", "Pinal",
                                       "Yavapai", "Yuma", "Apache", "Coconino", "Gila", "Greenlee", "Maricopa",
                                       "Navajo"]},
                         {"name": "Arkansas", "abbreviation": "AR",
                          "counties": ["Cleveland", "Columbia", "Baxter", "Cleburne", "Cross",
                                       "Drew", "Garland", "Hot Spring", "Jackson",
                                       "Little River", "Madison", "Montgomery", "Pike",
                                       "Poinsett", "St. Francis", "Searcy", "Sharp", "Union",
                                       "Van Buren", "Washington", "Woodruff", "Arkansas",
                                       "Ashley", "Benton", "Boone", "Bradley", "Calhoun",
                                       "Carroll", "Chicot", "Clark", "Clay", "Conway",
                                       "Craighead", "Crawford", "Crittenden", "Newton",
                                       "Ouachita", "Perry", "Phillips", "Polk", "Pope",
                                       "Prairie", "Pulaski", "Randolph", "Saline", "Scott",
                                       "Sebastian", "Sevier", "Stone", "Dallas", "Desha",
                                       "Faulkner", "Franklin", "Fulton", "Grant", "Greene",
                                       "Hempstead", "Howard", "Independence", "Izard",
                                       "Jefferson", "Johnson", "Lafayette", "Lawrence", "Lee",
                                       "Logan", "Lonoke", "Marion", "Miller", "Mississippi",
                                       "Monroe", "Nevada", "White", "Yell", "Lincoln"]},
                         {"name": "California", "abbreviation": "CA",
                          "counties": ["Colusa", "Glenn", "Kings", "Mariposa", "Modoc", "Sacramento", "San Bernardino",
                                       "Santa Barbara", "Shasta", "Tulare", "Alameda", "Alpine", "Marin", "Mendocino",
                                       "Merced", "Mono", "Monterey", "Napa", "Nevada", "Orange", "Placer", "Plumas",
                                       "Riverside", "San Benito", "San Diego", "San Francisco", "San Joaquin", "Amador",
                                       "Butte", "Calaveras", "Contra Costa", "Del Norte", "El Dorado", "Fresno",
                                       "Humboldt", "Imperial", "Inyo", "Kern", "Lake", "Lassen", "Los Angeles",
                                       "Madera", "San Luis Obispo", "San Mateo", "Santa Clara", "Santa Cruz", "Sierra",
                                       "Siskiyou", "Solano", "Sonoma", "Stanislaus", "Tehama", "Trinity", "Tuolumne",
                                       "Ventura", "Yolo", "Yuba", "Sutter"]},
                         {"name": "Colorado", "abbreviation": "CO",
                          "counties": ["Hinsdale", "Kiowa", "Lincoln", "Mineral", "Montrose", "Phillips", "Pueblo",
                                       "Rio Grande", "Sedgwick", "Washington", "Adams", "Alamosa", "Bent", "Boulder",
                                       "Broomfield", "Crowley", "Elbert", "Gilpin", "Gunnison", "Huerfano", "Jackson",
                                       "Jefferson", "Kit Carson", "Lake", "La Plata", "Larimer", "Las Animas", "Logan",
                                       "Mesa", "Moffat", "Montezuma", "Morgan", "Otero", "Ouray", "Park", "Pitkin",
                                       "Prowers", "Rio Blanco", "Routt", "Saguache", "San Juan", "San Miguel", "Summit",
                                       "Teller", "Weld", "Yuma", "Cheyenne", "Arapahoe", "Archuleta", "Baca", "Chaffee",
                                       "Clear Creek", "Conejos", "Costilla", "Custer", "Delta", "Denver", "Dolores",
                                       "Eagle", "El Paso", "Fremont", "Garfield", "Grand", "Douglas"]},
                         {"name": "Connecticut", "abbreviation": "CT",
                          "counties": ["Tolland", "Windham", "Fairfield", "Hartford", "Litchfield", "Middlesex",
                                       "New Haven", "New London"]}]

def query1(a, b):
	ret = []
	for state in pb:
		if state["abbreviation"] == a or state["name"].lower() == a.lower():
			for county in state["counties"]:
				if county[0] == b:
					ret.append(county);
			break
	return sorted(ret)

def query2(a):
	ret = []
	for state in pb:
		if a in state["counties"]:
			ret.append(state["abbreviation"])
	return sorted(ret)

N = int(input())
for i in range(N):
	c, *a = input().split()
	c = int(c)
	#print(a)
	if c == 1:
		a, *b = a
		a = a.upper()
		b = b[0].upper()
		print(", ".join(query1(a, b)))
	else:
		a = " ".join(a).lower().title()
		print(", ".join(query2(a)))
	
