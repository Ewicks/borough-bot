import requests
from bs4 import BeautifulSoup

URL = "http://planning.merton.gov.uk/Northgate/PlanningExplorerAA/Generic/StdDetails.aspx?PT=Planning%20Applications%20On-Line&TYPE=PL/PlanningPK.xml&PARAM0=%201000124509&XSLT=%20/Northgate/PlanningExplorerAA/SiteFiles/Skins/Merton/xslt/PL/PLDetails.xslt&FT=Planning%20Application%20Details&PUBLIC=%20Y&XMLSIDE=/Northgate/PlanningExplorerAA/SiteFiles/Skins/Merton/Menus/PL.xml&DAURI=PLANNING"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
print(soup)