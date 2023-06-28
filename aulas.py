from datetime import datetime
import time
import streamlit as st
import streamlit.components.v1 as components

aulas = {"":"",
'Aula1':'https://player.vimeo.com/video/435510262?h=1d9fcc8ac1',
'Aula2':'https://player.vimeo.com/video/265592338?h=c64b3fe448',
'Aula3':'https://player.vimeo.com/video/263751731?h=485bda666e',
'Aula4':'https://player.vimeo.com/video/263752648?h=a8d05a4f80',
'Aula6':'https://player.vimeo.com/video/263765446?h=85e4f3bb52',
'Aula7':'https://player.vimeo.com/video/263765284?h=2a0ab6544e',
'Aula8':'https://player.vimeo.com/video/263751100?h=6bb0132f9f',
'Aula9':'https://player.vimeo.com/video/263750660?h=5e7381931f',
'Aula11':'https://player.vimeo.com/video/267131411?h=6346f0ab24',
'Aula12':'https://player.vimeo.com/video/267131619?h=29ae347f34',
'Aula13':'https://player.vimeo.com/video/267131813?h=62a8802281',
'Aula14':'https://player.vimeo.com/video/267132003?h=60d85e81a1',
'Aula16':'https://player.vimeo.com/video/267132233?h=fec589d09b',
'Aula17':'https://player.vimeo.com/video/267132431?h=3919c3c6c2',
'Aula18':'https://player.vimeo.com/video/267132602?h=3ff356225c',
'Aula19':'https://player.vimeo.com/video/267132956?h=cf5a23a0f4',
'Revisão1':'https://player.vimeo.com/video/268307135?h=8b48c756f3',
'Aula21':'https://player.vimeo.com/video/268308051?h=d4cc8fe118',
'Aula22':'https://player.vimeo.com/video/533309826?h=a97e1b189e',
'Aula23':'https://player.vimeo.com/video/268307663?h=e56e703e01',
'Aula24':'https://player.vimeo.com/video/268307187?h=5b5e76f925',
'Aula26':'https://player.vimeo.com/video/268317102?h=9bc0742480',
'Aula27':'https://player.vimeo.com/video/268316910?h=cbfe9b94be',
'Aula28':'https://player.vimeo.com/video/275857722?h=36aef7b72c',
'Aula29':'https://player.vimeo.com/video/268325398?h=6a4626bc87',
'Aula31':'https://player.vimeo.com/video/269457978?h=0611e0b55d',
'Aula32-1':'https://player.vimeo.com/video/269458804?h=7e514cf8b7',
'Aula32-2':'https://player.vimeo.com/video/269458782?h=7c9be17c86',
'Aula33':'https://player.vimeo.com/video/269458514?h=0688f582fb',
'Aula34':'https://player.vimeo.com/video/269458295?h=195498cf21',
'Aula36':'https://player.vimeo.com/video/269466543?h=2e7adaa0cd',
'Aula37':'https://player.vimeo.com/video/270898067?h=2f80fc886f',
'Aula38':'https://player.vimeo.com/video/269466914?h=042014dfde',
'Aula39':'https://player.vimeo.com/video/270898348?h=ed824e6438',
'Revisão2':'https://player.vimeo.com/video/271003653?h=c063f76ca3',
'Aula41':'https://player.vimeo.com/video/271003667?h=9124687e7a',
'Aula42':'https://player.vimeo.com/video/271003918?h=5db613ce7f',
'Aula43':'https://player.vimeo.com/video/271004101?h=6f8036b6f6',
'Aula44':'https://player.vimeo.com/video/271004297?h=2b4d0ee1e4',
'Aula46':'https://player.vimeo.com/video/272128731?h=e839966d82',
'Aula47':'https://player.vimeo.com/video/272129695?h=ecb2c58cf6',
'Aula48':'https://player.vimeo.com/video/271014588?h=55e0a35cce',
'Aula49':'https://player.vimeo.com/video/272129338?h=1589a2a5e8',
'Aula51':'https://player.vimeo.com/video/272129176?h=50976c6074',
'Aula52':'https://player.vimeo.com/video/272128966?h=6337fb1598',
'Aula53':'https://player.vimeo.com/video/277547952?h=296401a886',
'Aula54':'https://player.vimeo.com/video/277548342?h=f816338640',
'Aula56':'https://player.vimeo.com/video/277547396?h=f9883290b4',
'Aula57':'https://player.vimeo.com/video/263752326?h=1f17390b8c',
'Aula58':'https://player.vimeo.com/video/277546866?h=fa640b743e',
'Aula59':'https://player.vimeo.com/video/277548741?h=08534dd150',
'Aula60':'https://player.vimeo.com/video/269468577?h=7e71714f5d',
'Extra':'https://player.vimeo.com/video/510818116?h=fbfa218aae',
}

#https://cdn.pixabay.com/photo/2015/10/15/03/11/cartoon-988863_1280.jpg");
st.set_page_config("Curso Milena")
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2017/01/28/19/31/landscape-2016308_1280.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
          
with st.container():
    add_bg_from_url() 
    st.title("Aulas Curso de Inglês da Milena")    
    st.write("---")
    aula_escolhida = st.selectbox('Escolha a Aula:', list(aulas.keys())) 
    video = aulas[aula_escolhida]    
    st.write("---") 

    if len(video) == 0:
        st.warning("Por favor, escolha uma aula na caixa de seleção acima!")       
    else:    
        components.iframe(video, width=None, height=None, scrolling=True)
        st.write("---")    
        st.subheader(f'Última Aula Selecionada: {aula_escolhida}')   
    
       
    
    
