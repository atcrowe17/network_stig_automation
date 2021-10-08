import pandas as pd
import xml.etree.ElementTree as et

xml_data = open('U_Cisco_IOS_XE_Switch_L2S_STIG_V2R1_Manual-xccdf.xml', 'r').read()  # Read file
root = et.XML(xml_data)  # Parse XML

data = []
cols = []
for i, child in enumerate(root):
    data.append([subchild.text for subchild in child])
    cols.append(child.tag)

df = pd.DataFrame(data).T  # Write in DF and transpose it
df.columns = cols  # Update column names
df.to_csv('stig.csv')
print(df)