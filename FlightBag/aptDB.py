import key
import requests
from pycountry import countries as iso

aptschema= ['ident','name','latitude_deg','longitude_deg','elevation_ft','iso_country','municipality','iata_code','home_link','runways','freqs','navaids']
rwyschema= ["length_ft","width_ft","surface","lighted","closed","le_ident","le_latitude_deg","le_longitude_deg","le_elevation_ft","le_heading_degT","le_displaced_threshold_ft","he_ident","he_latitude_deg","he_longitude_deg","he_elevation_ft","he_heading_degT","he_displaced_threshold_ft","he_ils","le_ils"]
ilsschema= ['freq','course']
freqschema= ["type","description","frequency_mhz"]
navschema= ["ident","name","type","frequency_khz","latitude_deg","longitude_deg","elevation_ft","dme_frequency_khz","dme_channel","dme_latitude_deg","dme_longitude_deg","slaved_variation_deg","magnetic_variation_deg",]
schema= [aptschema,rwyschema,ilsschema,freqschema,navschema]
ptr= int(0)
info= []
rwys= []
freq= []
navs= []

def formatInfo(info):
    country = iso.get(alpha_2 = f'{info[5]}')
    return [f'Ident: {info[0]} | {info[7]}\nName: {info[1]}\nCountry: {country.name}\nMunicipality: {info[6]}\nWebsite: {info[8]}\nLatitude: {info[2]}°\nLongitude: {info[3]}°\nElevation: {info[4]} ft.\n******************************************************************']

def formatRwy(rwys,rwyschema,ilsschema):
    data= []
    k= int(len(rwyschema)+len(ilsschema))
    loop= int(len(rwys)/k)
    L= ''
    C= ''
    for n in range(0,loop):
        i= n*k
        if int(rwys[i+3]): L = "YES"
        else: L = "NO"
        if int(rwys[i+4]): C= "YES"
        else: C= "NO"
        data.append([f"Runway {rwys[i+5]}/{rwys[i+11]}\nDimensions: {rwys[i]} x {rwys[i+1]} ft.\nSurface: {rwys[i+2]}\nLighted: {L}\nClosed: {C}\n\t\tRUNWAY {rwys[i+5]}\t\t\t\tRUNWAY {rwys[i+11]}\n\t   Latitude: {rwys[i+6]}°\t\t\t\t\t{rwys[i+12]}°\n\t  Longitude: {rwys[i+7]}°\t\t\t\t\t{rwys[i+13]}°\n\t  Elevation: {rwys[i+8]} ft.\t\t\t\t\t{rwys[i+14]} ft.\n\t    Heading: {rwys[i+9]}°\t\t\t\t\t{rwys[i+15]}°\nDisplaced Threshold: {rwys[i+10]} ft.\t\t\t\t\t\t{rwys[i+16]} ft.\n  ILS/DME Frequency: {rwys[i+19]} MHz\t\t\t\t\t\t{rwys[i+17]} MHz\n     ILS/DME Course: {rwys[i+20]}°\t\t\t\t\t\t{rwys[i+18]}°\n******************************************************************"])
    return data

def formatFreq(freq,freqschema):
    data= []
    name = ''
    k= int(len(freqschema))
    loop= int(len(freq)/k)
    for n in range(0,loop):
        i= n*k
        if (freq[i+1] == ''):
            name = freq[i]
        else: name = freq[i+1]
        if (n == loop-1):
            data.append([f"\t{name}:\t\t{freq[i+2]} MHz\n******************************************************************"])
        else:
            data.append([f"\t{name}:\t\t{freq[i+2]} MHz\n"])
    return data

def formatNav(navs,navschema):
    data= []
    k= int(len(navschema))
    loop= int(len(navs)/k)
    for n in range(0,loop):
        i= n*k
        data.append([f"\t     Ident: {navs[i]}\n\t      Name: {navs[i+1]}\n\t      Type: {navs[i+2]}\n\t Frequency: {navs[i+3]} kHz\n\t  Latitude: {navs[i+4]}°\n\t Longitude: {navs[i+5]}°\n\t Elevation: {navs[i+6]} ft.\n     DME Frequency: {navs[i+7]} kHz\n       DME Channel: {navs[i+8]}\n      DME Latitude: {navs[i+9]}°\n     DME Longitude: {navs[i+10]}°\n  Slaved Variation: {navs[i+11]}°\nMagnetic Variation: {navs[i+12]}°\n******************************************************************"])
    return data

def clean(ptr,data,res,schema):
    # Iterate over schemas
    for i in range(ptr,ptr+1):
        # Iterate within Schemas
        for j in range(0,len(schema[i])):
            # Current Schema
            k= schema[i]
            if (k[j] == 'runways'):
                try:
                    for l in range(0,len(res['runways'])):
                        clean(1,rwys,res['runways'][l],schema)
                except: data.append('')
            elif (k[j] == 'freqs'):
                try:
                    for l in range(0,len(res['freqs'])):
                        clean(3,freq,res['freqs'][l],schema)
                except: data.append('')
            elif (k[j] == 'navaids'):
                try:
                    for l in range(0,len(res['navaids'])):
                        clean(4,navs,res['navaids'][l],schema)
                except: data.append('')
            else: 
                try:
                    if (k[j] == 'he_ils'):
                        clean(2,rwys,res['he_ils'],schema)
                    elif (k[j] == 'le_ils'):
                        clean(2,rwys,res['le_ils'],schema)
                    else:
                        data.append(res[f"{k[j]}"])
                except:
                    data.append('')
                    data.append('')
    return data

def aptDB(reset,ICAO):
    if (reset):
        global info
        info.clear()
        global rwys
        rwys.clear()
        global freq
        freq.clear()
        global navs
        navs.clear()
        return
    else:
        token= key.token
        url= f"https://airportdb.io/api/v1/airport/{ICAO}?apiToken={token}"
        try:
            call= requests.get(url=url,timeout= 1.5)
            res= call.json()
            clean(ptr,info,res,schema)
            return [formatInfo(info),formatRwy(rwys,rwyschema,ilsschema),formatFreq(freq,freqschema),formatNav(navs,navschema)]
        except Exception as e:
            return [f"{type(e).__name__}: {e}"]