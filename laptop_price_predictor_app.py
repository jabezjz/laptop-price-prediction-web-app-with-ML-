import numpy as np
import pandas as pd
import streamlit as st
import joblib as jl
import pickle as pk
from sklearn.preprocessing import OneHotEncoder
st.header('laptop price predictor')
############## company name
laptop_company = st.selectbox(
   "desired BRAND of laptop",
   ('lenovo', 'asus', 'hp', 'dell', 'redmibook', 'realme', 'acer','msi', 'apple', 'infinix', 'samsung', 'ultimus', 'vaio','gigabyte', 'nokia', 'alienware'),
   )
st.write("You selected:", laptop_company)
############### model name
if laptop_company=="lenovo":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('ideapad 3 ', 'ideapad 1 ', 'none', 'ideapad gaming ',
       'ideapad gaming 3 ', 'ideapad ', 'ideapad 3 cb ', 'yoga 6 ',
       'ideapad slim 3 ', 'legion 5 ', 'lenovo legion 5 pro ',
       'ideapad slim 3i ', 'yoga slim 7 pro ', 'ideapad 5 ',
       'thinkpad e15 ', 'thinkbook 13s ', 'ideapad slim 5 ',
       'ideapad flex 5 ', 'yoga slim 7 ', 'thinkpad ', 'ideapad 5 pro ',
       'ideapad flex 3 chromebook ', 'ideapad slim 5i ', 'legion 5 pro ')
    )

if laptop_company=="asus":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('vivobook 15 ', 'tuf gaming f15 ', 'vivobook 14 ',
       'tuf gaming a17 ', 'rog strix g15 ', 'rog zephyrus g15 ',
       'vivobook k15 oled ', 'vivobook ultra 14 ',
       'vivobook pro 14x oled ', 'tuf gaming a15 ', 'rog zephyrus ',
       'vivobook pro 15 oled ', 'vivobook flip 14 ', 'vivobook s14 oled ',
       'tuf dash f15 ', 'zenbook 13 ', 'vivobook pro 15 ', 'eeebook 14 ',
       'zenbook duo 14 ', 'zenbook flip 13 oled touch panel ',
       'rog flow x13 ', 'tuf gaming f17 ', 'vivobook ',
       'zenbook s 13 oled ', 'expertbook p2 ', 'chromebook flip touch ',
       'rog flow z13 ', 'rog strix scar 15 ', 'studiobook pro ',
       'expertbook ', 'rog zephyrus g14 ', 'expertbook p1 ',
       'eeebook 12 ', 'rog zephyrus duo 16 ', 'asus tuf dash ',
       'vivobook pro 16x oled ', 'rog flow x16 ', 'zenbook pro 15 ',
       'chromebook ', 'expertbook b9 ', 'zenbook flip 14 oled ')
    
    )

if laptop_company=="hp":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('pavilion ', '14s ', 'victus ', 'athlon ', '15s ', 'none',
       'pavilion gaming ', 'envy x360 ', 'omen ', 'spectre ', 'omen 15 ',
       'laptop ', 'g8 ', 'hp pavilion ')
    
   
    )

if laptop_company=="dell":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('inspiron ', 'none', 'vostro ', 'g15 ', 'inspiron 3501 ',
       'allienware ')
 
  
    )
if laptop_company=="redmibook":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('pro ')

  
    )

if laptop_company=='realme':

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('book ', 'book', 'book prime ')

   
    )

if laptop_company=="acer":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('extensa ', 'aspire 7 ', 'aspire 3 ', 'aspire ', 'nitro 5 ',
       'none', 'aspire vero', 'aspire 5 ', 'predator helios 300 ',
       'aspire 5 gaming ', 'aspire vero ')

    )

if laptop_company=="msi":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('bravo 15 ', 'katana gf66 ', 'delta 15 ', 'none', 'stealth 15m ',
       'alpha 15 ', 'gf63 thin ', 'sword 15 ', 'crosshair 15 ',
       'modern 14 ', 'pulse gl66 ', 'gp66 leopard ', 'vector gp66 ',
       'prestige 14 ', 'stealth gs66 ', 'stealth gs77 ', 'gp65 leopard ',
       'creator 15 ')

   
    )

if laptop_company=="apple":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('2020 macbook air ', '2022 macbook pro ', '2021 macbook pro ',
       '2022 macbook air ', 'macbook air ', 'macbook pro ')

 
    )



if laptop_company=="infinix":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('inbook x1 neo series ', 'x1 slim series ', 'inbook x2 plus ',
       'inbook x1 ', 'x1 series ')
   
    )

if laptop_company=="samsung":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('galaxy book go ', 'galaxy book2 ')

 
    )

if laptop_company=="ultimus":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('s151 ')

 
    )


if laptop_company=="vaio":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('e series ')

    )


if laptop_company=="gigabyte":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('g5 gd ')

 
    )


if laptop_company=="nokia":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('purebook x14 ')

 
    )


if laptop_company=="alienware":

    laptop_product = st.selectbox(
       "desired MODEL of laptop",
       ('none')


    )

st.write("You selected:", laptop_product)

#################### graphics
laptop_graphics = st.selectbox(
   "desired graphics of laptop",
   ('none', '4 gb graphics', '8 gb graphics', '6 gb graphics',
       '2 gb graphics', '16 gb graphics')
   )
st.write("graphic card size:" , laptop_graphics )
##################### space and type of hard disks
laptop_space_type_emmc = st.selectbox(
   "emmc size",
   ('none', '128 gb emmc', '64 gb emmc', '32 gb emmc')
   )


laptop_space_type_hdd = st.selectbox(
   "hdd size",
   ('none', '1 tb hdd', '256 gb hdd')
   )

laptop_space_type_ssd = st.selectbox(
   "ssd size",
   ('256 gb ssd', '512 gb ssd', '1 tb ssd', 'none', '128 gb ssd',
       '2 tb ssd')
   )

st.write("You selected:", laptop_space_type_emmc,laptop_space_type_hdd,laptop_space_type_ssd)

################################processor

laptop_processor_brand=st.selectbox('select processor brand:', ('intel', 'amd', 'apple', 'qualcomm'))

st.write("You selected:", laptop_processor_brand)

if laptop_processor_brand == 'intel':
    processor_model = st.selectbox('select processor model',('11th gen core i3 processor', '10th gen core i3 processor',
       '10th gen core i5 processor', '11th gen core i5 processor',
       'celeron dual core processor', '12th gen core i5 processor',
       'celeron quad core processor', '11th gen core i7 processor',
       '2 gen pentium silver processor', '12th gen core i7 processor',
       '11th gen core i9 processor',
       '4th gen celeron dual core processor',
       '12th gen core i9 processor', 'pentium silver processor',
       '12th gen core i3 processor', '10th gen core i7 processor',
       '9th gen core i5 processor', '8th gen core i3 processor',
       'pentium quad core processor', '7th gen core i5 processor',
       '10th gen core i9 processor', '8th gen core i7 processor',
       '8th gen core i5 processor'))

if laptop_processor_brand == 'amd':
    processor_model = st.selectbox('select processor model',('ryzen 5 hexa core processor', 'ryzen 7 quad core processor',
       'ryzen 5 quad core processor', 'ryzen 9 octa core processor',
       'ryzen 7 octa core processor', 'ryzen 3 dual core processor',
       'athlon dual core processor', 'ryzen 3 quad core processor',
       '5th gen ryzen 9 octa core processor',
       '2 gen ryzen 3 dual core processor',
       '3rd gen ryzen 3 dual core processor',
       '2 gen ryzen 5 dual core processor',
       '5th gen ryzen 5 dual core processor',
       '4th gen ryzen 7 octa core processor',
       '10th gen ryzen 9 octa core processor',
       '10th gen ryzen 5 hexa core processor', '3020e dual core',
       '4th gen ryzen 3 hexa core processor',
       '9th gen ryzen 9 octa core processor'))

if laptop_processor_brand =='apple':
    processor_model = st.selectbox('select processor model',('m1 processor', 'm2 processor', 'm1 pro processor',
       'm1 max processor'))

if laptop_processor_brand =='qualcomm':
    processor_model = st.selectbox('select processor model',("qualcomm snapdragon 7c gen snapdragon 7c gen 2 processor",))


###### ram


ram=st.selectbox("select ram size",('8 gb ', '16 gb ', '4 gb ', '32 gb ', '128 gb '))

if laptop_processor_brand =='apple':
    ram_type = st.selectbox('select ram type',('unified memory ',))
else:
   ram_type = st.selectbox('select ram type',('ddr4 ', 'ddr5 ', 'lpddr4 ','lpddr4x ',
       'lpddr5 ', 'lpddr3 '))


##### OS
if laptop_processor_brand =='apple':
   os= st.selectbox('select os',('mac os ',))
else:
    os=st.selectbox('select os',('windows 11 ', 'windows 10 ', 'mac os ', 'dos ', 'chrome '))

selected={"Brand":[laptop_company],"model_name":[laptop_product],"graphics":[laptop_graphics],"emmc type":[laptop_space_type_emmc], "ssd type":[laptop_space_type_ssd], "hdd type":[laptop_space_type_hdd],"processor brand" :[laptop_processor_brand],"processor":[processor_model],"ram":[ram],"ram_type":[ram_type],"OS":[os]}
data=pd.DataFrame.from_dict(selected)

st.dataframe(data)


encoder_ = jl.load('encoder.pkl')
data_processed =pd.DataFrame(encoder_.transform(data),columns=encoder_.get_feature_names_out(data.columns), 
                               index = data.index)

st.dataframe(data_processed)


model=jl.load('laptop_predict_model')

st.write('price predictor says that the estimated value of the laptop will be:')
st.write(model.predict(data_processed))