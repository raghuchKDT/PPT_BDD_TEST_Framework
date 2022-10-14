import requests
import json
import jsonpath

# Get Projects
url = "http://127.0.0.1:5004/api/ProjectAPI/GetProjects"

# send GET requests
response = requests.get(url)
print(response)
# print(response.headers)

# json_response = json.loads(response.text)
# print(json_response)

# jsonpath_response = jsonpath.jsonpath(json_response, 'projectId')
# assert jsonpath_response[0] == 142


# Get Projects by Id
url1 = "http://127.0.0.1:5004/api/ProjectAPI/GetProjectDetailsById/?Id=142"

response1 = requests.get(url1)
print(response1)

# get Variants details
url2 = "http://127.0.0.1:5004/api/ProjectAPI/GetVariants"

response2 = requests.get(url2)
print(response2)

# get variant details by Id
url3 = "http://127.0.0.1:5004/api/ProjectAPI/GetVariantDetailsById/?Id=1"

response3 = requests.get(url3)
print(response3)

#  get variant details
url4 = "http://127.0.0.1:5004/api/ProjectAPI/GetVariants"

response4 = requests.get(url4)
print(response4)

# get Workflow details
url5 = "http://127.0.0.1:5004/api/ProjectAPI/GetWorkflows"

response5 = requests.get(url5)
print(response5)

# get Workflow details by Id
url6 = "http://127.0.0.1:5004/api/ProjectAPI/GetWorkflowDetailsById/?Id=1"

response6 = requests.get(url6)
print(response6)

# get global variable details by Id
url7 = "http://127.0.0.1:5004/api/ProjectAPI/GetGlobalVariableDetailsById/?Id=1"

response7 = requests.get(url7)
print(response7)

# get global variables details
url8 = "http://127.0.0.1:5004/api/ProjectAPI/GetGlobalVariables"

response8 = requests.get(url8)
print(response8)

# get system group details by Id
url9 = "http://127.0.0.1:5004/api/ProjectAPI/GetSystemGroupById/?Id=52"

response9 = requests.get(url9)
print(response9)

# get system  group details
url10 = "http://127.0.0.1:5004/api/ProjectAPI/GetSystemGroups"

response10 = requests.get(url10)
print(response10)

# get modules details
url11 = "http://127.0.0.1:5004/api/ProjectAPI/GetModules"

response11 = requests.get(url11)
print(response11)

# get module details by Id
url12 = "http://127.0.0.1:5004/api/ProjectAPI/GetModuleById?Id=49"

response12 = requests.get(url12)
print(response12)

# get remote ID Card details by Id
url13 = "http://127.0.0.1:5004/api/ProjectSettingsAPI/GetRemoteIOCardById/?Id=1"

response13 = requests.get(url13)
print(response13)

# get System logs reports
url14 = "http://127.0.0.1:5004/api/ProjectSettingsAPI/GetSystemLogsNReports"

response14 = requests.get(url14)
print(response14)

# get System Logs Reports by Id
url15 = "http://127.0.0.1:5004/api/ProjectSettingsAPI/GetSystemLogsNReportsById/?Id=1"

response15 = requests.get(url15)
print(response15)

# Get  PPT Master Card Data
url16 = "http://127.0.0.1:5004/api/ProjectSettingsAPI/GetPPTMasterCardData"

response16 = requests.get(url16)
print(response16)

# Get devices info
url17 = "http://127.0.0.1:5004/api/ProjectSettingsAPI/GetDevices"

response17 = requests.get(url17)
print(response17)

# Get Internal Variable Types Info
url18 = "http://127.0.0.1:5004/api/ProjectSettingsAPI/GetInternalVarTypes"

response18 = requests.get(url18)
print(response18)

# Get Pin Definitions Info
url19 = "http://127.0.0.1:5004/api/ProjectSettingsAPI/GetPinDefinitions"

response19 = requests.get(url19)
print(response19)

# Get Access Section Details
url20 = "http://127.0.0.1:5004/api/UserAPI/GetAccessSection"

response20 = requests.get(url20)
print(response20)

# Get Access Section Details by Id
url21 = "http://127.0.0.1:5004/api/UserAPI/GetAccessSectionDetailsById/?Id=1"

response21 = requests.get(url21)
print(response21)

# Get User Details
url22 = "http://127.0.0.1:5004/api/UserAPI/GetUser"

response22 = requests.get(url22)
print(response22)

# Get User Details by Id
url23 = "http://127.0.0.1:5004/api/UserAPI/GetUserDetailsById/?Id=1"

response23 = requests.get(url23)
print(response23)

# Get Xcode Details
url24 = "http://127.0.0.1:5004/api/ProjectAPI/GetXCodes"

response24 = requests.get(url24)
print(response24)

# Get Xcode Details By Id
url25 = "http://127.0.0.1:5004/api/ProjectAPI/GetXCodeDetailsById/?Id=72"

response25 = requests.get(url25)
print(response25)

# Get Splice Details
url26 = "http://127.0.0.1:5004/api/ProjectAPI/GetSplice"

response26 = requests.get(url26)
print(response26)

# Get Splice Details By Id
url27 = "http://127.0.0.1:5004/api/ProjectAPI/GetSpliceDetailsById/?Id=44"

response27 = requests.get(url27)
print(response27)


